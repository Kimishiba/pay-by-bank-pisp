# PISP License Extension: Incremental Cost & Delta Analysis
**Applicant:** CM Payments B.V. (Relation Number: R129862 / KvK: 62095757)  
**Supervisory Authority:** De Nederlandsche Bank (DNB) & European Banking Authority (EBA)  
**Scope:** Net Extra Costs to add Service 7 (PISP) to existing Payment Institution License (Services 3 & 5)  
**Applicable Legal Framework:** PSD2 (Directive (EU) 2015/2366), Wft Section 2:3b, EBA/GL/2017/08 (PII)  

---

## Executive Summary: The Baseline vs. Delta Principle

CM Payments B.V. is already fully authorized by **De Nederlandsche Bank (DNB)** as a Payment Institution (*Betaalinstelling*) for **Service 3** (execution of payment transactions) and **Service 5** (issuing and acquiring). As an active regulated institution, CM.com already absorbs the baseline corporate, prudential, and supervisory overhead of holding a financial license.

Adding **Payment Initiation Services (PISP - Service 7)** does *not* require creating a new financial institution. It is executed via a formal **Application for Scope Extension (*Aanvraag tot uitbreiding van de vergunning*)** under Section 2:3b of the Dutch Financial Supervision Act (*Wft*).

### The Key Finding
* **Zero Extra Capital:** The initial capital for standalone PISP (€50,000) is already exceeded by CM Payments B.V.'s existing regulatory capital (€125,000+).
* **Zero Extra Base Levy:** DNB's annual base supervision levy (*Vast toezichttarief*) is charged per institution, not per service.
* **Zero Extra Governance Costs:** Existing executive directors and board are already vetted under DNB *Betrouwbaarheid en Geschiktheid*.
* **Net Extra Annual Run-Rate:** Strictly **+€19,500 to +€48,500 / year**, driven exclusively by mandatory PISP Professional Indemnity Insurance (PII), eIDAS certificates, and cloud KMS infrastructure.

---

## 1. Upfront Setup Costs: Baseline vs. Incremental Delta

| Cost Component | De Novo (New PI) | CM Payments B.V. Base | Net Extra Delta to Add PISP | Notes & Regulatory Drivers |
| :--- | :---: | :---: | :---: | :--- |
| **DNB Application Fee** | €10,400 – €15,000 | Already Licensed | **€2,700** | Statutory scope extension tariff (*Regeling bekostiging*). |
| **Initial Capital (Art. 7a)** | €50,000 (Paid-up) | €125,000+ (Capitalized) | **€0.00** | Existing capital already covers Service 7 requirements. |
| **Director Fit & Proper Vetting** | €4,000 – €6,000 | Board already vetted | **€0.00** | No new directors required for scope extension. |
| **PIS Regulatory Legal Counsel** | €30,000 – €60,000 | In-house legal team | **€10,000 – €20,000** | Specialized DNB PIS policies & Q&A representation. |
| **PIS Pen-Testing & Security** | €10,000 – €20,000 | Corporate ISMS exists | **€5,000 – €8,000** | Independent audit of Berlin Group mTLS & KMS engine. |
| **Total One-Off Upfront Outlay** | **€104,400 – €151,000** | **Baseline Absorbed** | **€17,700 – €30,700** | **Pure one-off cash outlay to secure approval.** |

---

## 2. Annual Recurring Costs: Baseline vs. Incremental Delta

| Cost Component | CM Baseline (Services 3 & 5) | Combined with Service 7 | Net Extra Delta to Hold PISP | Governing Rule / Explanation |
| :--- | :---: | :---: | :---: | :--- |
| **DNB Fixed Base Supervision Levy** | €4,500 – €7,500 / yr | €4,500 – €7,500 / yr | **€0.00** | Charged per licensed entity under Wbft, not per service. |
| **DNB Variable Supervision Levy** | Based on acquiring volume | Acquiring + PIS fee revenue | **+ €1,000 – €5,000** | Levied on incremental PIS gross commission income (~0.05%–0.2%). |
| **Mandatory PII Insurance** | €0 (Not required for S3/S5) | Mandatory PISP coverage | **+ €15,000 – €35,000** | Standalone policy, mandatory under PSD2 Art. 5(2) & EBA/GL/2017/08 formula. A rider on the existing tech E&O policy is €5,000 – €15,000 (see `psd2_pii_insurance_analysis.md`). |
| **eIDAS Certificates (QWAC/QSealC)** | €0 (Not used in acquiring) | Annual QTSP renewals | **+ €1,500 – €2,500** | Required for bank mTLS and request signing (ETSI TS 119 495). |
| **External Financial & DORA Audit** | Already conducted annually | PIS module audited | **€0 – €2,000** | Marginal delta to audit new PIS API controls. |
| **Compliance Officer & MLRO** | Active Risk & MLRO team | Same team handles PIS | **€0.00** | No incremental compliance headcount required. |
| **Cloud KMS Key Storage & Proxy** | Existing AWS/Azure cloud | QSealC private key HSM | **+ €2,000 – €4,000** | Secure cloud vault for signing keys and mTLS tunnels. |
| **Total Annual Running Cost** | **Existing PI Overhead** | **Combined PI Overhead** | **+ €19,500 – €48,500 / yr** | **Net ongoing annual run-rate to hold Service 7.** |

> **With a PII rider instead of a standalone policy** (€5,000 – €15,000), the annual run-rate falls to **+€9,500 – €28,500 / yr**.

---

## 3. Incremental Delta vs. Partner Aggregator Economics

With an annual incremental overhead of only **~€20k to €50k / year**, the economic crossover point against third-party aggregators (Tink, Yapily, TrueLayer) drops dramatically:

| Metric | Direct PISP Extension (Net Delta) | Partner Aggregator (External) |
| :--- | :---: | :---: |
| **Upfront Setup Outlay** | **€17,700 – €30,700** | €0 – €5,000 |
| **Net Annual Fixed Cost** | **€19,500 – €48,500 / yr** | €12,000 – €36,000 / yr |
| **Marginal Fee per Payment** | **€0.00** *(PSD2 Art. 66)* | **€0.04 – €0.08** per transaction |
| **Cost at 500k Payments / Year** | **€34,000** total cost *(€0.068/tx)* | **€49,000** total cost *(€0.098/tx)* |
| **Cost at 2M Payments / Year** | **€34,000** total cost *(€0.017/tx)* | **€136,000** total cost *(€0.068/tx)* |
| **Economic Breakeven Threshold** | **~40,000 to 50,000 payments/month** | Optimal below 40k payments/month |

---

## 4. Key Steps to Execute Scope Extension

1. **Procure PII Policy Rider:** Obtain binding quotation under EBA/GL/2017/08 and generate the official DNB Insurance Declaration (*Verzekeringsverklaring*).
2. **Draft Program of Operations:** Finalize technical and operational flows adhering to PSD2 Article 66 (no customer fund handling) and DORA ICT risk standards.
3. **Submit via MijnDNB:** Formally lodge Form *Uitbreiding vergunning betaalinstelling* in DNB’s Digital Supervision Portal and settle the statutory **€2,700** tariff.
4. **Acquire eIDAS Certificates:** Upon receiving DNB's decree, order QWAC and QSealC certificates from an accredited QTSP (QuoVadis / DigiCert) with the `PSP_PI` role.
