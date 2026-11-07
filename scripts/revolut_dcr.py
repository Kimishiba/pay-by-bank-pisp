#!/usr/bin/env python3
"""
Revolut Open Banking Dynamic Client Registration (DCR) Engine
RFC 7591 / Open Banking DCR v3.1 Specification

Attempts automated registration against Revolut Sandbox Auth Gateway
(https://sandbox-oba-auth.revolut.com/register) using PS256/RS256 signed registration JWT.
"""
import sys
import os
import time
import json
import base64
import urllib.request
import ssl
import subprocess

DCR_ENDPOINT = "https://sandbox-oba-auth.revolut.com/register"
AUTH_ENDPOINT = "https://sandbox-oba-auth.revolut.com"

def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

def build_registration_jwt(key_path: str, cert_path: str) -> str:
    # 1. Header
    header = {
        "alg": "RS256",
        "typ": "JWT",
        "kid": "CM-PAYMENTS-REVOLUT-DCR-2026"
    }
    
    # 2. Claims (RFC 7591 / Revolut Open Banking DCR spec)
    now = int(time.time())
    payload = {
        "iss": "CM Payments B.V.",
        "iat": now,
        "exp": now + 3600,
        "aud": "https://sandbox-oba-auth.revolut.com",
        "client_name": "CM.com Pay by Bank Gateway",
        "client_description": "Direct Payment Initiation Service (PISP) for CM Payments B.V.",
        "redirect_uris": [
            "https://pay.cm.com/redirect/callback",
            "http://localhost:8088/#success"
        ],
        "scope": "openid payments accounts",
        "token_endpoint_auth_method": "tls_client_auth",
        "grant_types": ["client_credentials", "authorization_code"],
        "response_types": ["code id_token"]
    }
    
    header_b64 = b64url(json.dumps(header).encode('utf-8'))
    payload_b64 = b64url(json.dumps(payload).encode('utf-8'))
    signing_input = f"{header_b64}.{payload_b64}".encode('utf-8')
    
    # 3. Sign using OpenSSL
    sign_proc = subprocess.Popen(
        ["openssl", "dgst", "-sha256", "-sign", key_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    signature, stderr = sign_proc.communicate(input=signing_input)
    if sign_proc.returncode != 0:
        raise RuntimeError(f"OpenSSL signing failed: {stderr.decode()}")
        
    sig_b64 = b64url(signature)
    return f"{header_b64}.{payload_b64}.{sig_b64}"

def execute_dcr():
    print("==========================================================================")
    print("   Revolut Open Banking: Dynamic Client Registration (DCR) Engine         ")
    print("   Endpoint: " + DCR_ENDPOINT)
    print("==========================================================================\n")
    
    # Auto-detect Revolut-specific certificates or fallback to project default
    if os.path.exists("certs/revolut/transport.pem"):
        tls_cert = "certs/revolut/transport.pem"
        tls_key = "certs/revolut/private.key" if os.path.exists("certs/revolut/private.key") else "certs/revolut/transport.key"
        sign_key = "certs/revolut/signing.key" if os.path.exists("certs/revolut/signing.key") else tls_key
        sign_cert = "certs/revolut/signing.pem" if os.path.exists("certs/revolut/signing.pem") else tls_cert
        print("[*] Detected custom Revolut credentials in certs/revolut/")
    else:
        tls_cert = "certs/example_client_tls.cer"
        tls_key = "certs/example_client_tls.key"
        sign_key = "certs/example_client_signing.key"
        sign_cert = "certs/example_client_signing.cer"
        print("[*] Using workspace client credentials in certs/")
    
    if not (os.path.exists(tls_cert) and os.path.exists(tls_key)):
        print(f"[!] Error: Client TLS certificate not found at {tls_cert}")
        sys.exit(1)
        
    # Check certificate details
    issuer_proc = subprocess.run(
        ["openssl", "x509", "-in", tls_cert, "-noout", "-issuer", "-subject"],
        capture_output=True, text=True
    )
    print("[*] Inspecting Local Client Certificate:")
    for line in issuer_proc.stdout.strip().split("\n"):
        print("    " + line)
    print("")

    # Construct Registration JWT
    print("[*] Generating RFC 7591 Registration JWT assertion...")
    try:
        reg_jwt = build_registration_jwt(sign_key, sign_cert)
        print(f"[✓] Signed JWT generated (Length: {len(reg_jwt)} characters)\n")
    except Exception as e:
        print(f"[!] Failed to sign registration JWT: {e}")
        sys.exit(1)

    # Dispatch mTLS DCR call via curl
    print(f"[*] Dispatching mTLS POST to Revolut DCR endpoint:\n    {DCR_ENDPOINT} ...")
    cmd = [
        "curl", "-k", "-i", "-X", "POST", DCR_ENDPOINT,
        "--cert", tls_cert,
        "--key", tls_key,
        "-H", "Content-Type: application/jwt",
        "-H", "Accept: application/json",
        "--data-raw", reg_jwt,
        "-m", "10"
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    raw_output = res.stdout + res.stderr
    
    print("\n--- [Raw HTTP Response from Revolut Gateway] ---")
    lines = raw_output.split("\n")
    for l in lines[:20]:
        print(l)
    print("------------------------------------------------\n")
    
    if "200 OK" in raw_output or "201 Created" in raw_output:
        print("[SUCCESS] Revolut DCR Registration Successful!")
        # Try to parse client_id
        for l in lines:
            if "client_id" in l:
                print(f"[✓] Registered Client Details: {l.strip()}")
    elif "403 Forbidden" in raw_output:
        print("[!] Revolut Gateway Returned HTTP 403 Forbidden.")
        print("\n[DIAGNOSTIC & CA ANALYSIS]:")
        print("1. Revolut's sandbox mTLS reverse proxy (nginx at sandbox-oba-auth.revolut.com)")
        print("   strictly enforces Mutual TLS at the transport layer against trusted CAs.")
        print("2. The local cert in certs/example_client_tls.cer is currently issued by")
        print("   ING's Sandbox Internal CA (CN=AppCertificateMeansAPI/OU=Ing).")
        print("3. To complete automated DCR with Revolut Sandbox:")
        print("   a) Log in to developer.revolut.com -> 'Open Banking Sandbox'")
        print("   b) Generate or download Revolut's trusted Sandbox Transport Cert ('transport.pem')")
        print("      or use an Open Banking Directory (OBIE) test certificate.")
        print("   c) Place it in certs/revolut/transport.pem and re-run this script.")
    else:
        print(f"[*] Response received: {raw_output[:300]}")

if __name__ == "__main__":
    execute_dcr()
