#!/usr/bin/env python3
import sys
import json
import urllib.request
import urllib.error

BASE_URL = "http://localhost:8088"

def test_gateway():
    print("--- 1. Testing Bank Directory Listing ---")
    req = urllib.request.Request(f"{BASE_URL}/api/v1/banks")
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 200, f"Expected 200, got {resp.status}"
        banks = json.loads(resp.read().decode())
        assert "ing" in banks, "ING bank missing from directory"
        print("✓ Bank directory verified (ING, Rabo, ABN, Volksbank present)")

    print("\n--- 2. Testing Payment Creation (Live mTLS to ING) ---")
    pay_payload = {
        "bank_id": "ing",
        "amount": 149.00,
        "currency": "EUR",
        "merchant_reference": "ORD-AUTOMATED-TEST",
        "creditor_iban": "NL99CMCO0123456789",
        "description": "Payment for ORD-AUTOMATED-TEST"
    }
    req = urllib.request.Request(
        f"{BASE_URL}/api/v1/payments",
        data=json.dumps(pay_payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 201, f"Expected 201, got {resp.status}"
        data = json.loads(resp.read().decode())
        payment_id = data["payment_id"]
        sca_url = data["sca_redirect_url"]
        telemetry = data["live_telemetry"]
        
        assert payment_id.startswith("PAY-GO-"), f"Unexpected payment ID format: {payment_id}"
        assert sca_url != "", "Missing SCA redirect URL"
        assert telemetry["is_live_network_call"] is True, "Live network call flag not set"
        assert telemetry["hostname"] == "api.sandbox.ing.com", "Target host mismatch"
        print(f"✓ Payment created: {payment_id}")
        print(f"✓ Live mTLS to ING: {telemetry['tls_info']['resolved_ip']} ({telemetry['tls_info']['tls_version']})")
        print(f"✓ SCA Redirect URL: {sca_url}")

    print("\n--- 3. Testing Payment Retrieval ---")
    req = urllib.request.Request(f"{BASE_URL}/api/v1/payments/{payment_id}")
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 200, f"Expected 200, got {resp.status}"
        rec = json.loads(resp.read().decode())
        assert rec["payment_id"] == payment_id
        print(f"✓ Payment record retrieved by ID: {payment_id}")

    print("\n--- 4. Testing SCA Authorization Endpoint ---")
    # Parse payment_id from sca_url
    from urllib.parse import urlparse, parse_qs
    parsed = urlparse(sca_url)
    qs = parse_qs(parsed.fragment.split("?")[1])
    param_pid = qs.get("payment_id", [""])[0]
    print(f"Extracted parameter payment_id from redirect URL: '{param_pid}'")

    auth_req = urllib.request.Request(
        f"{BASE_URL}/api/v1/payments/{param_pid}/authorize",
        data=b"{}",
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(auth_req) as resp:
        assert resp.status == 200, f"Expected 200, got {resp.status}"
        auth_data = json.loads(resp.read().decode())
        assert auth_data["status"] == "ACSC_SETTLED", f"Expected ACSC_SETTLED, got {auth_data['status']}"
        assert "SCT Inst" in auth_data["settlement_rail"], f"Missing SEPA Instant rail: {auth_data['settlement_rail']}"
        assert "clearing_reference" in auth_data, "Missing clearing reference"
        print(f"✓ Authorization Successful!")
        print(f"  - Status: {auth_data['status']}")
        print(f"  - Rail: {auth_data['settlement_rail']}")
        print(f"  - Clearing Ref: {auth_data['clearing_reference']}")
        print(f"  - Authorized At: {auth_data['authorized_at']}")

    print("\n--- 5. Testing Static Assets & SCA Modal HTML ---")
    with urllib.request.urlopen(f"{BASE_URL}/index.html") as resp:
        html = resp.read().decode()
        assert "scaModal" in html, "SCA Modal element missing in HTML"
        assert "confirmSCAAuthorization" in html, "confirmSCAAuthorization JS function missing in HTML"
        print("✓ Frontend HTML contains scaModal and confirmation handler")

    print("\n=======================================================")
    print("🎉 ALL 5 END-TO-END GATEWAY TESTS PASSED WITH ZERO ERRORS!")
    print("=======================================================")

if __name__ == "__main__":
    try:
        test_gateway()
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}", file=sys.stderr)
        sys.exit(1)
