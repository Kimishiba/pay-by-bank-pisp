# Dutch Banks Sandbox Environments & Testing Guide for CM.com
**Target:** Payment Initiation Services (PISP) Integration  
**Legal Mandate:** PSD2 RTS Article 32 (Mandatory Testing Facilities for ASPSPs)  

---

## 1. Regulatory Guarantee: Are Sandboxes Available?

**Yes.** Under **Article 32 of the PSD2 Regulatory Technical Standards (RTS) on SCA & CSC**, all European banks are **legally mandated by the European Banking Authority (EBA)** to provide a functional testing environment (sandbox) to Third Party Providers (TPPs).

* **No Production License Required to Start:** In sandbox mode, banks allow testing using **self-signed or sandbox test certificates** instead of live €3,000 eIDAS QWAC/QSealC certificates.
* **Simulated SCA:** Sandboxes provide test user credentials (mock PSUs) and simulated mobile app redirect pages to mimic Face ID and biometric approvals.

---

## 2. Sandbox Matrix for Key Dutch Banks

| Bank | Sandbox Base URL | Developer Registration | Test Certificate Model | Test PSU / Tooling |
| :--- | :--- | :--- | :--- | :--- |
| **ING Bank** | `https://api.sandbox.ing.com` | [developer.ing.com](https://developer.ing.com) | Self-generated test certificate uploaded to portal | Mock PSU credentials; pre-populated balances |
| **Rabobank** | `https://api-sandbox.rabobank.nl/openapi/sandbox` | [docs.developer.rabobank.com](https://docs.developer.rabobank.com) | Sandbox API Key + Developer portal test cert | Mock sandbox app & simulated authentication screen |
| **ABN AMRO** | `https://api-sandbox.abnamro.com` | [developer.abnamro.com](https://developer.abnamro.com) | Portal-generated test client credentials | Mock accounts and simulated e.dentifier QR codes |
| **De Volksbank**<br>*(SNS, ASN, Regio)* | `https://psd.bancairediensten.nl/psd2/{brand}/sandbox` | [openbanking.devolksbank.nl](https://openbanking.devolksbank.nl) | Pre-configured sandbox certificate bundle | Postman collections with pre-built mock environments |
| **bunq** | `https://public-api.sandbox.bunq.com/v1` | [developer.bunq.com](https://developer.bunq.com) | Instant sandbox API key generation via Tinker CLI | Full virtual bank account generation with mock funds |
| **Revolut** | `https://sandbox-oba.revolut.com`<br>`https://sandbox-oba-auth.revolut.com` | [developer.revolut.com](https://developer.revolut.com) | Sandbox directory / test eIDAS certs | Postman collections & sandbox test portal |
| **Wise** | `https://openbanking.wise-sandbox.com` | [wise.com/help/articles/2978044](https://wise.com/help/articles/2978044) | Open Banking sandbox directory certs | Simulated consent authorization portal |

---

## 3. How to Start Testing Immediately (Without Waiting for DNB)

1. **Step 1: Create Developer Accounts:**
   * Register CM.com engineering accounts on [developer.ing.com](https://developer.ing.com) and [developer.rabobank.nl](https://docs.developer.rabobank.com).
2. **Step 2: Generate Self-Signed Test Certificates:**
   * Generate an OpenSSL test RSA keypair and certificate:
     ```bash
     openssl req -x509 -newkey rsa:2048 -keyout test_key.pem -out test_cert.pem -days 365 -nodes
     ```
   * Upload `test_cert.pem` to ING's portal to receive a sandbox `Client-Id` and `Client-Secret`.
3. **Step 3: Test Payment Initiation:**
   * Execute the `POST /v2/payments/sepa-credit-transfers` call against the sandbox endpoint.
   * Verify response handling for `RCVD` status and mock `scaRedirect` links.
