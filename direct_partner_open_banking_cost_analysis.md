# Direct Partner / Aggregator Integration: Cost & Strategic Analysis
**Focus:** Cost to Integrate with an Existing Authorized Open Banking Partner (PISP Aggregator / BaaS) vs. Direct In-House Bank Connectivity  
**Target Entity:** CM Payments B.V. (Relation: R129862 / KvK: 62095757)  
**Leading Partner Benchmarks:** Tink (Visa), Yapily, TrueLayer, Token.io, Salt Edge, kevin., Volt  

---

## Executive Summary

Instead of securing an incremental DNB PISP scope extension and building custom direct bank connectors (such as the Berlin Group engine for ING, Rabobank, and ABN AMRO), CM.com can integrate with a **direct third-party Open Banking partner** that already has full European bank connectivity and regulatory infrastructure in place.

### Key Takeaways
1. **Upfront Speed & Minimal Capital Risk:**
   * **Time-to-Market:** **2 to 4 weeks** (single REST API integration) vs. **4 to 6 months** (DNB regulatory application and audit).
   * **One-off Cash Outlay:** **€8,000 – €15,000** (almost entirely 1–2 internal engineering sprints) vs. **€17,700 – €30,700** for direct DNB license extension + security audits.
2. **Zero Regulatory & Certificate Overhead:**
   * **€0 DNB Application Fee** (saves €2,700).
   * **€0 Mandatory PII Insurance Rider** (saves €5,000 – €15,000/yr).
   * **€0 eIDAS QWAC / QSealC Certificates** (saves €1,500 – €2,500/yr).
3. **The Hidden Maintenance Offset:**
   * Direct bank connectivity requires **0.5 to 1.0 FTE maintenance engineer** (~€45,000 – €75,000/yr) to handle constant bank API breaking changes, downtime failovers, and cert rotations across 10+ Dutch banks and hundreds of EU banks. A partner absorbs 100% of this operational burden.
4. **The Economic Crossover Point:**
   * **Below ~60,000 transactions/month:** Integrating with a direct partner is **substantially cheaper, faster, and lower risk**.
   * **Above ~80,000 – 100,000 transactions/month:** The partner's per-transaction variable fee (€0.02 – €0.05/tx) surpasses the fixed in-house regulatory run-rate, making a direct license or hybrid model more margin-accretive.

---

## 1. Operating Models with a Direct Partner

A partner integration can be executed under three distinct models:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   THREE OPEN BANKING ROLLOUT PATHS                     │
├───────────────────────┬────────────────────────┬───────────────────────┤
│ Model A: Agent /      │ Model B: Hybrid TSP    │ Model C: Full Direct  │
│ Turnkey Partner       │ (License + Gateway)    │ In-House (Build/Own)  │
├───────────────────────┼────────────────────────┼───────────────────────┤
│ • Partner license used│ • CM holds DNB S7      │ • CM holds DNB S7     │
│ • Partner eIDAS certs │ • CM eIDAS certs       │ • CM eIDAS certs      │
│ • Partner UI/Consent  │ • CM branding on banks │ • CM branding on banks│
│ • Zero DNB delta cost │ • Partner handles pipes│ • CM builds all pipes │
│ • 2–4 weeks launch    │ • Reduced routing fee  │ • 4–6 months launch   │
└───────────────────────┴────────────────────────┴───────────────────────┘
```

### Model A: Turnkey Aggregator / Agent Model (Zero License Needed)
* **How it works:** CM embeds the partner's PISP engine (e.g. Yapily Connect, Tink, TrueLayer). The partner acts as the authorized PISP on record.
* **Consent Screen:** Shows the partner's regulated entity name authorizing the payment on behalf of CM / the merchant.
* **Regulatory Burden:** Zero. CM needs no DNB PISP authorization, no eIDAS certs, and no PII policy.

### Model B: Technical Service Provider (TSP) Model (Hybrid)
* **How it works:** CM secures the DNB Service 7 scope extension (incremental delta: ~€20k setup, ~€15k–€25k/yr running). However, instead of writing custom connectors for 50+ European banks, CM routes API calls through a software-only partner (e.g. Yapily or Token.io in TSP mode).
* **Consent Screen:** Displays **CM Payments B.V.** directly on ING, Rabobank, and ABN AMRO screens.
* **Pricing:** Partner waives the regulatory risk premium and charges a heavily discounted pure software routing fee (~€0.015 – €0.03/tx).

---

## 2. Direct Partner Cost Breakdown

Based on prevailing commercial terms from major European Open Banking providers (Tink, Yapily, TrueLayer, Token.io, Salt Edge):

### A. One-Off Upfront Onboarding & Setup

| Cost Element | Partner Model (Standard) | In-House DNB Delta | Cost Advantage / Notes |
| :--- | :---: | :---: | :--- |
| **Partner Onboarding & Setup Fee** | **€0 – €3,500** | €0.00 | Often waived or credited against first-year volume for established PSPs like CM.com. |
| **DNB Scope Extension Fee** | **€0.00** | €2,700 | Statutory DNB filing fee saved. |
| **PIS Regulatory Legal Counsel** | **€0.00** | €10,000 – €20,000 | No regulatory policies, terms, or DNB Q&A required. |
| **eIDAS Certificate Issuance** | **€0.00** | €1,500 – €2,500 | Partner provides certified QWAC/QSealC to banks. |
| **Engineering Integration Effort** | **€8,000 – €14,000** | €25,000 – €50,000 | 1 unified REST API (2–3 weeks) vs. 10+ bank-specific bespoke APIs (2–4 months). |
| **External Pen-Testing** | **€0 – €2,500** | €5,000 – €8,000 | Only standard web application pen-test needed; no mTLS/KMS cryptographic audit. |
| **Total One-Off Setup Cost** | **€8,000 – €20,000** | **€44,200 – €83,200** | **Saves €35,000 – €63,000 upfront & accelerates go-to-market by ~4 months.** |

---

### B. Annual Fixed / Recurring Platform Costs

| Cost Element | Partner Model | In-House DNB Delta | Operational Impact |
| :--- | :---: | :---: | :--- |
| **Platform SaaS / Minimum Commitment** | **€12,000 – €30,000 / yr** | €0.00 | Billed as €1,000 – €2,500/month minimum commitment (typically absorbs initial transaction fees). |
| **Bank Connector Maintenance (FTE)** | **€0.00** | €45,000 – €75,000 / yr | **Critical hidden cost:** Banks regularly break APIs, deprecate endpoints, and alter SCA flows. In-house requires ~0.5–1.0 FTE. Partner includes 24/7 bank connectivity maintenance. |
| **Mandatory PII Insurance** | **€0.00** | €5,000 – €15,000 / yr | Covered by the partner's regulated balance sheet. |
| **eIDAS Annual Renewals** | **€0.00** | €1,500 – €2,500 / yr | Handled by partner. |
| **Cloud KMS & Key HSM** | **€500 – €1,000 / yr** | €2,000 – €4,000 / yr | Standard API token management instead of dedicated hardware security modules for QSeal keys. |
| **Net Annual Fixed Run-Rate** | **€12,500 – €31,000 / yr** | **€53,500 – €96,500 / yr** *(incl. maint. FTE)* | **Partner fixed platform cost is comparable to or lower than maintaining direct bank connectors.** |

---

### C. Variable Transaction Pricing (Tiered by Monthly Volume)

Partners bill primarily on **successful payment initiations**:

| Monthly Payment Volume | Approximate Unit Fee (Tink / TrueLayer / Yapily) | Wholesale / TSP Mode (Software Only) | In-House Direct Bank |
| :--- | :---: | :---: | :---: |
| **< 25,000 payments/mo** | **€0.06 – €0.08** / tx | €0.035 – €0.050 / tx | €0.00 / tx (PSD2 Art. 66) |
| **25,000 – 100,000 payments/mo** | **€0.04 – €0.06** / tx | €0.025 – €0.035 / tx | €0.00 / tx |
| **100,000 – 500,000 payments/mo** | **€0.025 – €0.04** / tx | €0.015 – €0.022 / tx | €0.00 / tx |
| **> 500,000 payments/mo (Enterprise)** | **€0.012 – €0.02** / tx | €0.008 – €0.012 / tx | €0.00 / tx |

---

## 3. Total Cost of Ownership (TCO) & Breakeven Modeling

The table below calculates the **All-In Annual Cost** across transaction volume scenarios, comparing:
1. **Direct Partner (Model A - Turnkey)**: €18,000 base MMC + tiered per-tx fees. Zero internal bank maintenance.
2. **In-House Direct DNB Delta (Model C)**: €25,000 regulatory delta (PII, eIDAS, DNB, KMS) + €50,000 bank maintenance engineer (0.7 FTE) = **€75,000 fixed / yr**, €0.00 per-transaction fee.
3. **Hybrid TSP (Model B)**: €25,000 regulatory delta + €12,000 partner base + wholesale per-tx fees (€0.02/tx). Zero internal bank maintenance.

| Annual Payment Volume (Monthly Volume) | Direct Partner (Turnkey) | In-House Direct (Delta + Maint) | Hybrid TSP (License + Partner Pipes) | Lowest Cost Recommendation |
| :--- | :---: | :---: | :---: | :--- |
| **60,000 / yr** *(5k / mo)* | **€21,600** *(€0.360/tx)* | €75,000 *(€1.250/tx)* | €38,200 *(€0.637/tx)* | **Direct Partner wins (3.5x cheaper)** |
| **300,000 / yr** *(25k / mo)* | **€33,000** *(€0.110/tx)* | €75,000 *(€0.250/tx)* | €44,500 *(€0.148/tx)* | **Direct Partner wins (2.3x cheaper)** |
| **600,000 / yr** *(50k / mo)* | **€45,000** *(€0.075/tx)* | €75,000 *(€0.125/tx)* | €52,000 *(€0.087/tx)* | **Direct Partner wins (1.7x cheaper)** |
| **1,200,000 / yr** *(100k / mo)* | **€63,000** *(€0.053/tx)* | **€75,000** *(€0.063/tx)* | **€61,000** *(€0.051/tx)* | **Crossover Zone (~100k payments/month)** |
| **3,000,000 / yr** *(250k / mo)* | €99,000 *(€0.033/tx)* | **€75,000** *(€0.025/tx)* | €82,000 *(€0.027/tx)* | **In-House Direct / Hybrid wins** |
| **6,000,000 / yr** *(500k / mo)* | €138,000 *(€0.023/tx)* | **€75,000** *(€0.013/tx)* | €97,000 *(€0.016/tx)* | **In-House Direct wins (Economies of scale)** |

```
Annual Cost (€)
  ▲
150k │                                             / Direct Partner (Turnkey)
     │                                           /
100k │                            ┌────────────/── Hybrid TSP
     │                          / │          /
 75k ┼─────────────────────────/──┼────────/──────── In-House Direct Fixed Line (€75k)
     │                       /    │      /
 50k │                     /      │    /
     │                   /        │  /
 25k │  ═══════════════/          │/
     │
   0 └───────┬────────────┬───────┴────┬───────────► Annual Volume
           300k         600k         1.2M         3.0M
                           ▲
                     BREAKEVEN ZONE (~1.0M - 1.2M tx/yr)
```

---

## 4. Feature & Strategic Trade-Off Matrix

| Strategic Evaluation Criteria | Direct In-House (CM DNB Rails) | Direct Partner (Turnkey Aggregator) | Hybrid TSP (CM DNB + Partner Engine) |
| :--- | :--- | :--- | :--- |
| **Time to Market** | 4 to 6 months (DNB vetting + bank certs) | **2 to 4 weeks (Instant sandbox)** | 2 to 3 months |
| **Bank Reach (NL)** | Top 3 banks in-house (ING, Rabo, ABN) | **All 10+ Dutch banks live on Day 1** | All 10+ Dutch banks live on Day 1 |
| **Bank Reach (Europe)** | Must build bank-by-bank connectors | **3,000+ banks across 20+ EU states** | 3,000+ banks across 20+ EU states |
| **Checkout Branding** | Pure **CM Payments B.V.** on bank screen | Partner name appears on consent screen | Pure **CM Payments B.V.** on bank screen |
| **Maintenance Burden** | High (0.5–1.0 FTE monitoring bank APIs) | **Zero (Covered by Partner SLA)** | **Zero (Covered by Partner SLA)** |
| **Marginal Transaction Fee** | **€0.00** | €0.015 – €0.060 per transaction | €0.010 – €0.025 per transaction |
| **Vendor Independence** | **100% sovereign** | Dependent on partner gateway | Low lock-in (standard eIDAS certs) |

---

## 5. Recommended Phased Implementation Strategy

For CM.com, the most capital-efficient and risk-mitigated strategy is a **two-phase phased rollout**:

### Phase 1: Launch Immediately with a Direct Partner (Months 1 – 6)
* **Action:** Contract a partner (e.g. Yapily, Tink, or Token.io) under turnkey/agent mode or fast-track integration.
* **Cost:** ~€1,500/mo base commitment + ~€0.04/tx + 2 engineering weeks.
* **Benefit:** Go live with Pay by Bank across the Netherlands and Europe immediately. Validate merchant demand and transaction conversion without waiting for DNB approval or building 10 bank connectors.

### Phase 2: File DNB Scope Extension & Transition to Hybrid TSP / Direct Rails (Months 6+)
* **Action:** Once monthly volume approaches **50,000 – 100,000 transactions/month**, file the DNB scope extension (€2,700 fee + PII rider).
* **Cost:** Switch to wholesale TSP pricing (~€0.015/tx) or route top Dutch banks (ING, Rabo, ABN AMRO) directly via the in-house Berlin Group engine developed in this project, while keeping the partner for long-tail European banks.
* **Result:** Maximizes gross profit margins at scale while preserving speed and instant European reach today.