# French Banks Sandbox Environments & STET Testing Guide for CM.com
**Target:** Payment Initiation Services (PISP) Integration via STET PSD2  
**Legal Mandate:** PSD2 RTS Article 32 (Mandatory Testing Facilities for ASPSPs)  
**Standard:** STET PSD2 (v1.4.2.31 / v1.4.2.15)

---

## 1. Overview of the French Open Banking Sandbox Landscape

Unlike the Berlin Group standard used across Germany and the Netherlands, **France operates under the STET standard (~95% market coverage)**. Under STET, payment endpoints use `POST /payment-requests` with nested ISO 20022 JSON payloads instead of flat Berlin Group attributes.

---

## 2. French Banks Sandbox Matrix

| Bank | Brand / Group | Portal URL | Sandbox Status | DCR / Onboarding Model |
| :--- | :--- | :--- | :--- | :--- |
| **Société Générale** | SG Network, BoursoBank | [developer.societegenerale.fr](https://developer.societegenerale.fr) | **Active & Provisioned** | Direct developer portal app creation; Client ID + Secret |
| **BNP Paribas** | BNP Paribas Retail, Hello bank!, CIB | [bcef.devportal.api.bnpparibas](https://bcef.devportal.api.bnpparibas) | Available via DCR | RFC 7591 automated DCR endpoint (`POST /register`) / TPP Desk |
| **Groupe BPCE** | Banque Populaire, Caisse d'Épargne | [apistore.groupebpce.com](https://apistore.groupebpce.com) | Available via DCR | Automated STET PSD2 Registration API (v1.0.6) |
| **Crédit Agricole** | 39 Regional Caisses, LCL | [developer.credit-agricole.fr](https://developer.credit-agricole.fr) | Gated | Requires EBA/GURN regulatory authorization number |
| **Crédit Mutuel** | Crédit Mutuel, CIC | [openbanking.creditmutuel.fr](https://openbanking.creditmutuel.fr) | Gated | Euro-Information TPP portal onboarding |

---

## 3. Société Générale Sandbox Configuration (CM Payments B.V.)

### 3.1 Organization & Application
* **Consumer Organization:** `CM Payments B.V.` (`db60e124-6912-4d05-911e-90a74231b861`)
* **Application Name:** `CM Payments` (`cm-payments-gateway`)
* **API In Scope:** `payment-requests-pri:1.4.2.31` (STET v1.4.2.15 model)
* **Redirect URI:** `https://paybybank.homeassistantkrooswijkhof.duckdns.org/redirect.html`

### 3.2 Gateway Endpoints
* **Base API Endpoint:** `https://mtls.api.sb.sg.fr/sg/sb/dsp2/pisp/pri/v1.4.2.15`
* **OAuth2 Token Endpoint:** `https://mtls.sg-signin.sb.societegenerale.fr/oauth2/token`
* **OAuth2 Authorization URL:** `https://sg-signin.sb.societegenerale.fr/oauth2/authorize`
* **Credentials:** Managed securely in `.env` (`SG_SANDBOX_CLIENT_ID` and `SG_SANDBOX_CLIENT_SECRET`).

---

## 4. Mock PSU Test Personas for SCA Simulation

Société Générale provides pre-configured test users for Strong Customer Authentication (SCA) scenarios against the `payment-requests-pri` endpoint:

| Login (PSU-ID) | Password | SCA Mechanism Simulated | Expected Gateway Outcome |
| :--- | :--- | :--- | :--- |
| `55000001` | `111111` | Security Pass (Biometric App Approval) | `Accepted` / Success |
| `55000002` | `111111` | SMS OTP Validation (Code: `ABC123`) | `Accepted` / Success |
| `55000003` | `111111` | Standard Security Check | `Accepted` / Success |
| `55000004` | `111111` | Instant Payment SCA Validation (Code: `ABC123`) | `Settled` (Instant SCT) |
| `55000010` | `111111` | Security Pass Failed / Declined | `Rejected` (Biometric failure) |
| `55000011` | `111111` | SMS OTP Code Invalid | `Rejected` (Invalid code) |
| `55000012` | `111111` | No Security / Frictionless Exemption | Instant `Accepted` |

---

## 5. Sample STET Initiation Call

```http
POST /payment-requests HTTP/1.1
Host: mtls.api.sb.sg.fr
Client-Id: 5fbc1941-779f-45ac-990e-73ba959568b4
Authorization: Bearer <access_token>
Date: Sat, 07 Nov 2026 14:25:00 GMT
X-Request-ID: e62bc780-e847-4952-b9cf-2b02e7b51e08
Digest: SHA-256=...
Signature: keyId="5fbc1941-779f-45ac-990e-73ba959568b4",algorithm="rsa-sha256",headers="date (request-target) digest x-request-id",signature="..."
Content-Type: application/json; charset=utf-8

{
  "initiatingParty": {
    "name": "CM Payments B.V."
  },
  "beneficiary": {
    "name": "CM Payments B.V. - Stichting Derdengelden",
    "creditorAccount": {
      "iban": "FR7630003000501234567890123",
      "currency": "EUR"
    }
  },
  "creditTransferTransaction": [
    {
      "paymentId": {
        "instructionIdentification": "INST-20261107-SG01",
        "endToEndIdentification": "ORD-991823"
      },
      "instructedAmount": {
        "amount": 49.50,
        "currency": "EUR"
      },
      "remittanceInformation": {
        "unstructured": [
          "Payment for Order ORD-991823"
        ]
      }
    }
  ]
}
```
