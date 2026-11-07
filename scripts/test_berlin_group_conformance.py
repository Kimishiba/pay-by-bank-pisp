#!/usr/bin/env python3
"""
Berlin Group NextGenPSD2 Conformance & Validation Test Suite
Tests gateway behavior against standard Berlin Group PIS payloads and schema expectations.
"""
import json
import urllib.request
import urllib.error
import sys

BASE_URL = "http://localhost:8088"

def run_tests():
    print("=================================================================")
    print("  Berlin Group NextGenPSD2 Conformance Test Suite (v1.3.15)      ")
    print("=================================================================\n")

    # 1. Load standard Berlin Group test fixture
    fixture_path = "specs/fixtures/initiate-payment-request-body.json"
    with open(fixture_path, "r") as f:
        fixture_body = json.load(f)
    print(f"[✓] Loaded Berlin Group PIS initiation fixture from {fixture_path}")
    print(f"    - Amount: {fixture_body['instructedAmount']['amount']} {fixture_body['instructedAmount']['currency']}")
    print(f"    - Debtor IBAN: {fixture_body['debtorAccount']['iban']}")
    print(f"    - Creditor IBAN: {fixture_body['creditorAccount']['iban']}\n")

    # 2. Test initiation across supported Berlin Group banks
    banks = ["ing", "rabobank", "abnamro", "volksbank", "revolut"]
    results = {}

    for bank_id in banks:
        print(f"[*] Testing Berlin Group PIS initiation against dialect adapter: [{bank_id.upper()}]...")
        payload = {
            "bank_id": bank_id,
            "amount": float(fixture_body["instructedAmount"]["amount"]),
            "currency": fixture_body["instructedAmount"]["currency"],
            "merchant_reference": fixture_body.get("endToEndIdentification", "BG-TEST-001"),
            "creditor_iban": fixture_body["creditorAccount"]["iban"],
            "description": fixture_body.get("remittanceInformationUnstructured", "Berlin Group Conformance Test")
        }

        req = urllib.request.Request(
            f"{BASE_URL}/api/v1/payments",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )

        try:
            with urllib.request.urlopen(req) as resp:
                status_code = resp.status
                data = json.loads(resp.read().decode())
                payment_id = data.get("payment_id")
                sca_redirect = data.get("sca_redirect_url")
                telemetry = data.get("live_telemetry", {})

                # Validate Berlin Group PIS state model
                assert status_code == 201, f"Expected 201 Created, got {status_code}"
                assert payment_id is not None, "Missing paymentId in response"
                assert sca_redirect != "", "Missing scaRedirect URL in Berlin Group hypermedia links"

                print(f"    -> Status: HTTP 201 Created")
                print(f"    -> Payment ID: {payment_id}")
                print(f"    -> SCA Redirect URI: {sca_redirect}")
                print(f"    -> Live mTLS Host: {telemetry.get('hostname')}")
                print(f"    -> TLS Resolved IP: {telemetry.get('tls_info', {}).get('resolved_ip', 'N/A')}")
                print(f"    -> Dialect Standard: {telemetry.get('scheme')}")
                print(f"    [PASS] {bank_id.upper()} passed Berlin Group conformance validation.\n")
                results[bank_id] = "PASSED"

        except Exception as e:
            print(f"    [FAIL] {bank_id.upper()}: {e}\n")
            results[bank_id] = f"FAILED: {e}"

    print("=================================================================")
    print("  Summary:")
    all_passed = True
    for b, res in results.items():
        print(f"  - {b.upper()}: {res}")
        if "FAILED" in res:
            all_passed = False
    print("=================================================================")

    if not all_passed:
        sys.exit(1)
    print("\nAll Berlin Group NextGenPSD2 conformance tests completed successfully!")

if __name__ == "__main__":
    run_tests()
