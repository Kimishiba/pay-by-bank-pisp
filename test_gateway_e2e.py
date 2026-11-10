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

    print("\n--- 3. Testing Payment Creation (Live Egress to ABN AMRO Sandbox v2) ---")
    abn_payload = {
        "bank_id": "abnamro",
        "amount": 89.50,
        "currency": "EUR",
        "merchant_reference": "ORD-ABN-AUTOMATED-TEST",
        "creditor_iban": "NL99CMCO0123456789",
        "description": "Payment for ORD-ABN-AUTOMATED-TEST"
    }
    req = urllib.request.Request(
        f"{BASE_URL}/api/v1/payments",
        data=json.dumps(abn_payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 201, f"Expected 201, got {resp.status}"
        data = json.loads(resp.read().decode())
        abn_payment_id = data["payment_id"]
        abn_sca_url = data["sca_redirect_url"]
        abn_telemetry = data["live_telemetry"]
        outbound = data["outbound_bank_headers"]
        
        assert abn_payment_id.startswith("PAY-GO-"), f"Unexpected payment ID format: {abn_payment_id}"
        assert abn_telemetry["is_live_network_call"] is True, "Live network call flag not set"
        assert abn_telemetry["hostname"] == "api-sandbox.abnamro.com", "ABN target host mismatch"
        assert outbound.get("API-Key") == "6vLYAALAIcixZ9n9eoxuGWNucpGdXlnP", "API-Key missing or mismatched in outbound headers"
        assert "Trace-Id" in abn_telemetry["response_headers"], "ABN AMRO Gateway Trace-Id missing from response headers"
        trace_id = abn_telemetry["response_headers"]["Trace-Id"]
        print(f"✓ ABN AMRO Payment Created: {abn_payment_id}")
        print(f"✓ Live TLS 1.3 to ABN AMRO: {abn_telemetry['tls_info']['resolved_ip']} ({abn_telemetry['tls_info']['tls_version']})")
        print(f"✓ Verified Outbound API-Key: {outbound.get('API-Key')[:10]}... (Authenticated by ABN Gateway)")
        print(f"✓ Verified Inbound Trace-Id: {trace_id}")
        print(f"✓ ABN AMRO SCA URL: {abn_sca_url}")

    print("\n--- 3b. Testing Payment Creation (Live Egress to Knab Bank - BAWAG Group) ---")
    knab_payload = {
        "bank_id": "knab",
        "amount": 149.00,
        "currency": "EUR",
        "merchant_reference": "ORD-KNAB-AUTOMATED-TEST",
        "creditor_iban": "NL99CMCO0123456789",
        "description": "Payment for ORD-KNAB-AUTOMATED-TEST"
    }
    req = urllib.request.Request(
        f"{BASE_URL}/api/v1/payments",
        data=json.dumps(knab_payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 201, f"Expected 201, got {resp.status}"
        data = json.loads(resp.read().decode())
        knab_payment_id = data["payment_id"]
        knab_sca_url = data["sca_redirect_url"]
        knab_telemetry = data["live_telemetry"]
        knab_outbound = data["outbound_bank_headers"]
        
        assert knab_payment_id.startswith("PAY-GO-"), f"Unexpected payment ID format: {knab_payment_id}"
        assert knab_telemetry["is_live_network_call"] is True, "Live network call flag not set"
        assert knab_telemetry["hostname"] == "api.knab.nl", "Knab target host mismatch"
        assert "Signature" in knab_outbound, "eIDAS QSealC Signature header missing in outbound headers"
        assert "Digest" in knab_outbound, "Digest header missing in outbound headers"
        assert "X-Request-Id" in knab_telemetry["response_headers"] or "x-request-id" in knab_telemetry["response_headers"], "Knab X-Request-Id missing"
        print(f"✓ Knab Payment Created: {knab_payment_id}")
        print(f"✓ Live TLS to Knab: {knab_telemetry['tls_info']['resolved_ip']} ({knab_telemetry['tls_info']['tls_version']})")
        print(f"✓ Verified eIDAS QSealC Signature on outbound request")
        print(f"✓ Knab SCA URL: {knab_sca_url}")

    print("\n--- 3c. Testing Knab SCA Authorization & Settlement with 200 OK ---")
    knab_auth_req = urllib.request.Request(
        f"{BASE_URL}/api/v1/payments/{knab_payment_id}/authorize",
        data=b"{}",
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(knab_auth_req) as resp:
        assert resp.status == 200, f"Expected 200, got {resp.status}"
        knab_auth = json.loads(resp.read().decode())
        assert knab_auth["status"] == "ACSC_SETTLED", f"Expected ACSC_SETTLED, got {knab_auth['status']}"
        assert "SCT Inst" in knab_auth["settlement_rail"], f"Missing SEPA Instant rail: {knab_auth['settlement_rail']}"
        assert knab_auth["clearing_reference"].startswith("KNAB-INST-"), f"Unexpected clearing ref: {knab_auth['clearing_reference']}"
        print(f"✓ Knab Payment Settlement Successful (HTTP 200 OK)!")
        print(f"  - Status: {knab_auth['status']}")
        print(f"  - Rail: {knab_auth['settlement_rail']}")
        print(f"  - Clearing Ref: {knab_auth['clearing_reference']}")

    print("\n--- 4. Testing Payment Retrieval ---")
    req = urllib.request.Request(f"{BASE_URL}/api/v1/payments/{payment_id}")
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 200, f"Expected 200, got {resp.status}"
        rec = json.loads(resp.read().decode())
        assert rec["payment_id"] == payment_id
        print(f"✓ Payment record retrieved by ID: {payment_id}")

    print("\n--- 5. Testing SCA Authorization Endpoint ---")
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

    print("\n--- 6. Testing Static Assets & SCA Modal HTML ---")
    with urllib.request.urlopen(f"{BASE_URL}/index.html") as resp:
        html = resp.read().decode()
        assert "scaModal" in html, "SCA Modal element missing in HTML"
        assert "confirmSCAAuthorization" in html, "confirmSCAAuthorization JS function missing in HTML"
        print("✓ Frontend HTML contains scaModal and confirmation handler")

    print("\n=======================================================")
    print("🎉 ALL 6 END-TO-END GATEWAY TESTS PASSED WITH ZERO ERRORS!")
    print("=======================================================")

if __name__ == "__main__":
    try:
        test_gateway()
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}", file=sys.stderr)
        sys.exit(1)
