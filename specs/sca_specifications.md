# Bank SCA Specifications: Rabobank, ABN AMRO, and Revolut
**Standard Framework:** Berlin Group NextGenPSD2 XS2A v1.3.x / EBA RTS Article 32  
**Scope:** Payment Initiation Services (PISP) Strong Customer Authentication (SCA) Flows  
**Storage Path:** `specs/sca_specifications.md`  

---

## 1. Rabobank Strong Customer Authentication (SCA) Specs

### Architecture & Standards
* **Protocol:** Berlin Group NextGenPSD2 v1.3.6
* **Developer Portal:** `https://docs.developer.rabobank.com`
* **Sandbox Endpoint:** `https://api-sandbox.rabobank.nl/openapi/sandbox/payments/sepa-credit-transfers`
* **Production Endpoint:** `https://api.rabobank.nl/openapi/payments/payment-initiation/pis/v1/payments/sepa-credit-transfers`
* **SCA Method:** **Redirect SCA** (`TPP-Redirect-Preferred: true`)
* **Transport & Message Security:**
  * Transport: Mutual TLS (mTLS) with QWAC (or sandbox test certificate).
  * Request Signature: **Cavage HTTP Signature** (`Signature` header) signed with RSA-SHA256 across `(request-target)`, `Date`, `Digest`, and `X-Request-ID`.

### Payment Initiation & SCA Redirect Flow
1. **Initiate Payment Request (`POST`):**
   ```http
   POST /openapi/sandbox/payments/sepa-credit-transfers HTTP/1.1
   Host: api-sandbox.rabobank.nl
   X-Request-ID: 7a82c611-306f-40e1-bbcb-7c70e7df6501
   Date: Sat, 07 Nov 2026 10:15:00 GMT
   Digest: SHA-256=47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=
   Signature: keyId="CM-PAYMENTS-QSEAL",algorithm="rsa-sha256",headers="(request-target) date digest x-request-id",signature="b2Qx..."
   TPP-Redirect-Preferred: true
   TPP-Redirect-URI: https://checkout.cm.com/pay-by-bank/callback
   PSU-IP-Address: 82.161.45.12
   Content-Type: application/json

   {
     "instructedAmount": { "currency": "EUR", "amount": "149.00" },
     "creditorAccount": { "iban": "NL99CMCO0123456789" },
     "creditorName": "CM Payments B.V.",
     "remittanceInformationUnstructured": "Order ORD-99214"
   }
   ```
2. **Rabobank Response (HTTP 201 Created):**
   ```json
   {
     "transactionStatus": "RCVD",
     "paymentId": "rabo-pis-883921-992",
     "_links": {
       "scaRedirect": {
         "href": "https://api-sandbox.rabobank.nl/openapi/sandbox/oauth2/authorize?response_type=code&client_id=CM_APP_ID&scope=payment-initiation&redirect_uri=https%3A%2F%2Fcheckout.cm.com%2Fcallback"
       },
       "status": {
         "href": "/openapi/sandbox/payments/sepa-credit-transfers/rabo-pis-883921-992/status"
       }
     }
   }
   ```
3. **PSU SCA Experience:**
   * **Mobile Banking:** Universal App link opens **Rabo App** directly. The customer authenticates using their 5-digit PIN or biometrics (Face ID / Fingerprint).
   * **Desktop Web:** Displays color QR code scanned using the physical **Rabo Scanner** handheld optical device.
4. **Execution & Settlement:**
   * Once approved, PSU is redirected to `TPP-Redirect-URI`.
   * TPP checks status via `GET .../status`: transitions to `ACCP` (AcceptedCustomerProfile) or `ACSC` (AcceptedSettlementCompleted).

---

## 2. ABN AMRO Strong Customer Authentication (SCA) Specs

### Architecture & Standards
* **Protocol:** Berlin Group NextGenPSD2 v1.3 with OpenID Connect (OIDC) Authorization Code Flow
* **Developer Portal:** `https://developer.abnamro.com`
* **Sandbox Endpoint:** `https://api-sandbox.abnamro.com/v1/payments/sepa-credit-transfers`
* **Production Endpoint:** `https://api.abnamro.com/v1/payments/sepa-credit-transfers`
* **SCA Method:** **Redirect SCA with App Deep-Linking & e.dentifier**
* **Transport & Security:**
  * Transport: TLS 1.3 with API Key (`API-Key` header) + mTLS QWAC.
  * Message Signature: PKCE + OAuth2 Bearer Token.

### Payment Initiation & SCA Redirect Flow
1. **Initiate Payment Request (`POST`):**
   ```http
   POST /v1/payments/sepa-credit-transfers HTTP/1.1
   Host: api-sandbox.abnamro.com
   API-Key: sandbox_api_key_abn_cm_9912
   Authorization: Bearer <tpp_access_token>
   X-Request-ID: abn-req-8842104-aa2
   Content-Type: application/json
   TPP-Redirect-URI: https://checkout.cm.com/pay-by-bank/callback

   {
     "instructedAmount": { "currency": "EUR", "amount": "149.00" },
     "creditorAccount": { "iban": "NL99CMCO0123456789" },
     "creditorName": "CM Payments B.V.",
     "remittanceInformationUnstructured": "Invoice 2026-99"
   }
   ```
2. **ABN AMRO Response (HTTP 201 Created):**
   ```json
   {
     "transactionStatus": "PATC",
     "paymentId": "abn-pay-55192-384",
     "_links": {
       "scaRedirect": {
         "href": "https://auth-sandbox.abnamro.com/as/authorization.oauth2?client_id=abn_cm_sandbox&response_type=code&scope=psd2:payment:initiation&redirect_uri=https%3A%2F%2Fcheckout.cm.com%2Fcallback"
       },
       "scaStatus": {
         "href": "/v1/payments/sepa-credit-transfers/abn-pay-55192-384/authorisations"
       }
     }
   }
   ```
3. **PSU SCA Experience:**
   * **ABN AMRO Mobiel:** Automatic app switch on iOS/Android; push authentication prompt requiring biometric confirmation.
   * **e.dentifier 2:** Web fallback where customer inserts debit card into USB/standalone e.dentifier device, enters PIN, and inputs generated numeric token.

---

## 3. Revolut Strong Customer Authentication (SCA) Specs

### Architecture & Standards
* **Protocol:** Open Banking UK / Berlin Group XS2A Hybrid
* **Developer Portal:** `https://developer.revolut.com`
* **Sandbox Base:** `https://sandbox-oba.revolut.com` / `https://sandbox-oba-auth.revolut.com`
* **Production Base:** `https://oba.revolut.com` / `https://oba-auth.revolut.com`
* **SCA Method:** **Decoupled & Mobile App Redirect SCA** (Biometric First)
* **Transport & Security:**
  * Transport: mTLS with Open Banking / eIDAS QWAC.
  * Signing: JWS (PS256) signature header.

### Payment Initiation & SCA Flow
1. **Initiate Payment (`POST`):**
   * Endpoint: `POST https://sandbox-oba.revolut.com/v1/payments/sepa-credit-transfers`
   * Body contains SEPA credit transfer parameters.
2. **Revolut Response (HTTP 201):**
   ```json
   {
     "transactionStatus": "RCVD",
     "paymentId": "rev-pis-99382104",
     "_links": {
       "scaRedirect": {
         "href": "https://sandbox-oba-auth.revolut.com/consent?id=rev-pis-99382104&redirect_uri=https%3A%2F%2Fcheckout.cm.com%2Fcallback"
       },
       "scaOAuth": {
         "href": "revolut://app/open-banking/consent?id=rev-pis-99382104"
       }
     }
   }
   ```
3. **PSU SCA Experience:**
   * **Universal App Link:** Immediately opens the native Revolut app (`revolut://app/...` or HTTPS Universal Link).
   * **Biometric Auth:** Customer is presented with the Pay by Bank transfer sheet and confirms via **Face ID / Touch ID**.
   * **Instant Confirmation:** Revolut routes transfer over SEPA Instant (instant fund settlement in <2 seconds).
   * **Auto-Redirect:** The Revolut app automatically bounces the PSU back to CM's callback URL.

---

## 4. Comparison Summary Matrix for CM Gateway Implementation

| Specification Criteria | ING Bank | Rabobank | ABN AMRO | Revolut |
| :--- | :--- | :--- | :--- | :--- |
| **API Architecture** | Berlin Group v2.0 | Berlin Group v1.3.6 | Berlin Group v1.3 / OIDC | Open Banking / Berlin Group Hybrid |
| **Signing Header** | `x-jws-signature` (PS256 JWS) | `Signature` (Cavage RSA-SHA256) | OAuth2 PKCE Token | `x-jws-signature` (PS256 JWS) |
| **SCA Redirect Style** | Web & ING App Universal Link | Rabo App & Rabo Scanner | ABN AMRO Mobiel & e.dentifier | Revolut App Biometric Deep-Link |
| **Sandbox Hostname** | `api.sandbox.ing.com` | `api-sandbox.rabobank.nl` | `api-sandbox.abnamro.com` | `sandbox-oba.revolut.com` |
| **Settlement Speed** | SEPA Instant / Standard | SEPA Instant / Standard | SEPA Instant / Standard | **Native SEPA Instant (< 2 sec)** |
| **Gateway Connector** | Implemented (`certs/example_client_*`) | Cavage Adapter Ready | OIDC Adapter Ready | JWS Adapter Ready |
