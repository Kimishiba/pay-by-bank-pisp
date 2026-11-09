#!/usr/bin/env python3
"""
Generate ETSI TS 119 495 Compliant eIDAS PSD2 Certificates for Sandbox & Local Testing
Entity: CM Payments B.V.
NCA: De Nederlandsche Bank (NL-DNB)
NCA Authorisation Number: R136611
Roles: PSP_PI (Payment Initiation), PSP_AI (Account Information)
"""

import os
import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from pyasn1.type import univ, char, namedtype
from pyasn1.codec.der import encoder

# ASN.1 Schema for ETSI TS 119 495 PSD2 QCStatements
class RoleOfPspInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('roleInfoRoleCheck', univ.ObjectIdentifier()),
        namedtype.NamedType('roleInfoRoleName', char.UTF8String())
    )

class RolesOfPSP(univ.SequenceOf):
    componentType = RoleOfPspInfo()

class PSD2QcType(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('rolesOfPSP', RolesOfPSP()),
        namedtype.NamedType('ncaName', char.UTF8String()),
        namedtype.NamedType('ncaId', char.PrintableString())
    )

class QCStatement(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('statementId', univ.ObjectIdentifier()),
        namedtype.OptionalNamedType('statementInfo', univ.Any())
    )

class QCStatements(univ.SequenceOf):
    componentType = QCStatement()

def build_qc_statements_der(is_qwac: bool) -> bytes:
    qcs = QCStatements()
    
    # 1. id-etsi-qcs-QcCompliance (0.4.0.1862.1.1)
    s1 = QCStatement()
    s1['statementId'] = univ.ObjectIdentifier('0.4.0.1862.1.1')
    qcs.append(s1)
    
    # 2. id-etsi-qcs-QcType (0.4.0.1862.1.6)
    # id-etsi-qct-web = 0.4.0.1862.1.6.3 (QWAC)
    # id-etsi-qct-eseal = 0.4.0.1862.1.6.2 (QSealC)
    s2 = QCStatement()
    s2['statementId'] = univ.ObjectIdentifier('0.4.0.1862.1.6')
    qc_type_oid = '0.4.0.1862.1.6.3' if is_qwac else '0.4.0.1862.1.6.2'
    type_seq = univ.SequenceOf(componentType=univ.ObjectIdentifier())
    type_seq.append(univ.ObjectIdentifier(qc_type_oid))
    s2['statementInfo'] = univ.Any(encoder.encode(type_seq))
    qcs.append(s2)
    
    # 3. id-etsi-psd2-qcStatement (0.4.0.19495.2)
    psd2_payload = PSD2QcType()
    roles = RolesOfPSP()
    
    # PSP_PI = Payment Initiation (0.4.0.19495.1.2)
    r_pi = RoleOfPspInfo()
    r_pi['roleInfoRoleCheck'] = univ.ObjectIdentifier('0.4.0.19495.1.2')
    r_pi['roleInfoRoleName'] = char.UTF8String('PSP_PI')
    roles.append(r_pi)
    
    # PSP_AI = Account Information (0.4.0.19495.1.3)
    r_ai = RoleOfPspInfo()
    r_ai['roleInfoRoleCheck'] = univ.ObjectIdentifier('0.4.0.19495.1.3')
    r_ai['roleInfoRoleName'] = char.UTF8String('PSP_AI')
    roles.append(r_ai)
    
    psd2_payload['rolesOfPSP'] = roles
    psd2_payload['ncaName'] = char.UTF8String('De Nederlandsche Bank')
    psd2_payload['ncaId'] = char.PrintableString('NL-DNB')
    
    s3 = QCStatement()
    s3['statementId'] = univ.ObjectIdentifier('0.4.0.19495.2')
    s3['statementInfo'] = univ.Any(encoder.encode(psd2_payload))
    qcs.append(s3)
    
    return encoder.encode(qcs)

def main():
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "certs", "cm"))
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"Generating ETSI TS 119 495 certificates in: {out_dir}")
    
    # 1. Generate Root CA
    ca_key = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    ca_subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "NL"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "CM Payments Sandbox CA"),
        x509.NameAttribute(NameOID.COMMON_NAME, "CM Payments Test Root CA G1"),
    ])
    now = datetime.datetime.now(datetime.timezone.utc)
    ca_cert = (
        x509.CertificateBuilder()
        .subject_name(ca_subject)
        .issuer_name(ca_subject)
        .public_key(ca_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(days=1))
        .not_valid_after(now + datetime.timedelta(days=3650))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .add_extension(x509.KeyUsage(digital_signature=True, key_cert_sign=True, crl_sign=True,
                                    content_commitment=False, key_encipherment=False, data_encipherment=False,
                                    key_agreement=False, encipher_only=False, decipher_only=False), critical=True)
        .sign(ca_key, hashes.SHA256())
    )
    
    with open(os.path.join(out_dir, "cm_root_ca.key"), "wb") as f:
        f.write(ca_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    with open(os.path.join(out_dir, "cm_root_ca.crt"), "wb") as f:
        f.write(ca_cert.public_bytes(serialization.Encoding.PEM))
    print("  [✓] cm_root_ca.crt & cm_root_ca.key created")
    
    # 2. Generate QWAC (mTLS Client & Server Certificate)
    qwac_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    # organizationIdentifier OID is 2.5.4.97
    org_id_oid = x509.ObjectIdentifier("2.5.4.97")
    qwac_subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "NL"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "CM Payments B.V."),
        x509.NameAttribute(org_id_oid, "PSDNL-DNB-R136611"),
        x509.NameAttribute(NameOID.COMMON_NAME, "pay.cm.com"),
    ])
    
    qwac_der = build_qc_statements_der(is_qwac=True)
    qc_statements_oid = x509.ObjectIdentifier("1.3.6.1.5.5.7.1.3")
    
    qwac_cert = (
        x509.CertificateBuilder()
        .subject_name(qwac_subject)
        .issuer_name(ca_subject)
        .public_key(qwac_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(days=1))
        .not_valid_after(now + datetime.timedelta(days=730))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .add_extension(x509.KeyUsage(digital_signature=True, key_encipherment=True,
                                    content_commitment=False, data_encipherment=False,
                                    key_agreement=False, key_cert_sign=False, crl_sign=False,
                                    encipher_only=False, decipher_only=False), critical=True)
        .add_extension(x509.ExtendedKeyUsage([ExtendedKeyUsageOID.CLIENT_AUTH, ExtendedKeyUsageOID.SERVER_AUTH]), critical=False)
        .add_extension(x509.UnrecognizedExtension(qc_statements_oid, qwac_der), critical=False)
        .sign(ca_key, hashes.SHA256())
    )
    
    with open(os.path.join(out_dir, "cm_qwac.key"), "wb") as f:
        f.write(qwac_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    with open(os.path.join(out_dir, "cm_qwac.crt"), "wb") as f:
        f.write(qwac_cert.public_bytes(serialization.Encoding.PEM))
    print("  [✓] cm_qwac.crt & cm_qwac.key created (PSD2 QWAC mTLS)")
    
    # 3. Generate QSealC (Signing Certificate for JWS / HTTP Signatures)
    qseal_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    qseal_subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "NL"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "CM Payments B.V."),
        x509.NameAttribute(org_id_oid, "PSDNL-DNB-R136611"),
        x509.NameAttribute(NameOID.COMMON_NAME, "seal.cm.com"),
    ])
    
    qseal_der = build_qc_statements_der(is_qwac=False)
    qseal_cert = (
        x509.CertificateBuilder()
        .subject_name(qseal_subject)
        .issuer_name(ca_subject)
        .public_key(qseal_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(days=1))
        .not_valid_after(now + datetime.timedelta(days=730))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .add_extension(x509.KeyUsage(digital_signature=True, content_commitment=True,
                                    key_encipherment=False, data_encipherment=False,
                                    key_agreement=False, key_cert_sign=False, crl_sign=False,
                                    encipher_only=False, decipher_only=False), critical=True)
        .add_extension(x509.UnrecognizedExtension(qc_statements_oid, qseal_der), critical=False)
        .sign(ca_key, hashes.SHA256())
    )
    
    with open(os.path.join(out_dir, "cm_qsealc.key"), "wb") as f:
        f.write(qseal_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    with open(os.path.join(out_dir, "cm_qsealc.crt"), "wb") as f:
        f.write(qseal_cert.public_bytes(serialization.Encoding.PEM))
    print("  [✓] cm_qsealc.crt & cm_qsealc.key created (PSD2 QSealC Signing)")
    
    print("\nAll certificates generated successfully!")

if __name__ == "__main__":
    main()
