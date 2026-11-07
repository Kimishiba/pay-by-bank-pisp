# CM.com Pay by Bank // Direct PISP Gateway Engine

Direct Account-to-Account (A2A) Payment Initiation Services (PISP) engine connecting CM.com merchants to major Dutch banks (**ING Bank**, **Rabobank**, **ABN AMRO**, and **De Volksbank**) over **Berlin Group NextGenPSD2** and **SEPA Instant Credit Transfer (SCT Inst)** rails.

---

## ⚡ Architecture & Capabilities

* **High-Performance Go Engine (`main.go`):** Built in Go 1.22+ with zero third-party dependencies, leveraging Go's native `net/http` and `crypto/tls` for high-throughput concurrency.
* **Real Egress Wire Telemetry:** Establishes genuine outbound TCP/TLS connections to live bank API gateways, capturing DNS resolution, TLS 1.3 cipher suites, peer certificate issuers, exact millisecond latency, and live bank response headers (`X-ING-Response-ID`, Akamai `Reference ID`, ABN `Trace-Id`).
* **Cryptographic Standards:** Implements Berlin Group NextGenPSD2 specifications, SHA-256 payload digests, and simulated eIDAS QSealC HTTP signatures.
* **Interactive Egress Inspector (`public/index.html`):** Real-time web console designed under the **Neo-Raw / Neo-Brutalist Orange** design system.

---

## 🚀 Quick Start

### 1. Build and Run
```bash
# Build Go binary
go build -o pay-by-bank-gateway .

# Start gateway server
./pay-by-bank-gateway
```
The gateway listens on `http://localhost:8088`.

### 2. Live Bank Egress API Call
```bash
curl -i -X POST http://localhost:8088/api/v1/payments \
  -H "Content-Type: application/json" \
  -d '{
    "bank_id": "ing",
    "amount": 149.00,
    "merchant_reference": "ORD-LIVE-7719",
    "description": "Order #7719"
  }'
```

---

## 📚 Technical & Regulatory Documentation

1. [`direct_dutch_banks_pisp_architecture.md`](./direct_dutch_banks_pisp_architecture.md) — Production mTLS, KMS signing, and CAMT.054 settlement architecture.
2. [`top_10_dutch_banks_api_analysis.md`](./top_10_dutch_banks_api_analysis.md) — Endpoint mappings for Top 10 Dutch banks, Revolut, and Wise.
3. [`dutch_banks_api_endpoints_analysis.md`](./dutch_banks_api_endpoints_analysis.md) — Granular HTTP headers, JWS schemas, and universal deep links.
4. [`psd2_pisp_regulatory_analysis.md`](./psd2_pisp_regulatory_analysis.md) — DNB / Wft analysis for CM Payments B.V. (Relation R129862) and Service 7 requirements.
5. [`dnb_pisp_extension_costs_and_fees.md`](./dnb_pisp_extension_costs_and_fees.md) — Statutory €2,700 DNB fee schedule and annual supervision levies.
6. [`psd2_pii_insurance_analysis.md`](./psd2_pii_insurance_analysis.md) — Professional Indemnity Insurance market guide (Marsh/Aon, Chubb/AIG, EBA formula).
7. [`dutch_banks_sandbox_guide.md`](./dutch_banks_sandbox_guide.md) — Bank sandbox onboarding and test certificate generation.
