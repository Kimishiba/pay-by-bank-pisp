# DNB License Extension & Ongoing Maintenance Costs (Service 7 - PISP)
**Target Authority:** De Nederlandsche Bank (DNB) & European Banking Authority (EBA)  
**Applicant:** CM Payments B.V. (Relation Number: R129862)  
**Scope:** Adding Payment Initiation Services (PISP - Annex I, Service 7)  

---

## 1. Summary of All Costs (One-Off & Annual)

| Cost Category | Item | One-off / Upfront | Annual Recurring | Governing Law / Source |
| :--- | :--- | :---: | :---: | :--- |
| **DNB Direct Fees** | Scope Extension Application (*Wijzigingsaanvraag*) | **€2,700** | — | *Regeling bekostiging financieel toezicht eenmalige handelingen* |
| **DNB Ongoing** | Fixed Base Supervision (*Vast toezichttarief*) | — | **€4,500 – €7,500** | *Wet bekostiging financieel toezicht (Wbft)* |
| **DNB Ongoing** | Variable Supervision (*Variabel deel toezicht*) | — | Proportion of PIS Gross Revenue (~0.05% - 0.2%) | Based on annual DNB sector budget |
| **Mandatory PII** | Professional Indemnity Insurance | — | **€15,000 – €35,000** | Mandatory under PSD2 Art. 5(2) & EBA/GL/2017/08 |
| **eIDAS Cryptography** | QWAC & QSealC Certificates (QuoVadis / DigiCert) | — | **€1,500 – €3,000** | Qualified Trust Service Providers (QTSP) |
| **Optional DNB** | Retesting Board Members (*Toetsing beleidsbepalers*) | €2,000 – €3,000 *(only if new directors are added)* | — | DNB Fit & Proper vetting |

---

## 2. Granular Breakdown of DNB Regulatory Fees

### A. One-Off Extension Application Fee (€2,700)
* **Legal Basis:** Governed by the *Regeling bekostiging financieel toezicht eenmalige handelingen* (under Article 13 of the Wbft).
* **Scope:** Because CM Payments B.V. is already fully authorized as a Payment Institution (*Betaalinstelling*), you do **not** pay the full initial authorization fee (€10,400). Instead, an application to extend the scope of services (to add Service 7) incurs the standard statutory scope amendment tariff of **€2,700**.
* **Conditions:** Non-refundable upon submission, regardless of DNB's final decision or withdrawal.

### B. Annual DNB Supervision Fees (*Doorlopend Toezicht*)
Under the *Wet bekostiging financieel toezicht (Wbft)*, DNB recovers the operational costs of its banking and fintech supervision directly from market participants through an annual levy consisting of:
1. **Fixed Base Component (*Vast Bedrag*):**
   * Licensed payment institutions pay an annual base levy, typically ranging between **€4,500 and €7,500 per year** depending on the specific supervisory cluster.
2. **Variable Revenue-Based Component (*Variabel Bedrag*):**
   * DNB allocates its annual supervision budget across the payment sector. Each institution pays a variable levy proportional to its **gross commission and fee income (*bruto provisie-inkomsten*)** or processed volume reported in the annual DNB regulatory filings.
   * *Impact on CM.com:* Since CM Payments B.V. already pays this annual supervision levy for acquiring, adding Service 7 will only increase the variable portion in proportion to the new revenues generated from Pay by Bank transactions.

---

## 3. Mandatory External Cost: Professional Indemnity Insurance (PII)

The largest recurring financial obligation of a PISP license is **not** the central bank fee, but the mandatory **Professional Indemnity Insurance (PII)**:

* **Legal Requirement:** Under **Article 5(2) of PSD2** and **EBA Guidelines (EBA/GL/2017/08)**, a PISP must maintain an active PII policy or comparable bank guarantee covering liability toward ASPSPs (banks) and payment service users for unauthorized, non-executed, or defectively executed payment transactions.
* **Calculation Formula:** Based on value of transactions initiated, risk profile, and historical claims.
* **Commercial Cost:** Underwritten by specialized financial lines brokers (Marsh, Aon, Lloyd's). For an enterprise payment volume, annual premiums for a standalone policy typically range between **€15,000 and €35,000 per year**; adding a rider to CM.com's existing tech E&O policy is cheaper at **€5,000 – €15,000 per year** (see `psd2_pii_insurance_analysis.md`).
* **DNB Gate:** DNB will **not** grant the Service 7 license extension until a binding insurance cover note meeting the exact EBA calculation threshold is uploaded to the DNB Digital Supervision Portal (*MijnDNB*).

---

## 4. Total Cost of Ownership (Year 1 vs. Year 2+)

* **Year 1 Total Investment:** **~€24,000 – €48,000** (DNB €2,700 application + €15k–35k standalone PII + €1.5k–3k eIDAS certs + €4.5k–7.5k base DNB supervision; excludes the variable levy). Gross figures: CM already pays the base levy, so the incremental delta is in the dossier.
* **Subsequent Years Recurring:** **~€21,000 – €46,000 / year** (PII insurance + eIDAS certificates + DNB annual supervisory levy; excludes the variable levy).
