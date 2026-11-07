# Pay by Bank (PISP) Checkout UI Specification: High-Converting UX Requirements
**Document Version:** 1.1.0  
**Target Audience:** Frontend Engineers, UI/UX Designers, Product Managers  
**Scope:** Design-Agnostic Functional, UX, and Conversion Requirements  
**Target Entity:** CM Payments B.V. (Licensed Payment Institution, DNB Relation: R129862)  
**Target Conversion Benchmark:** ≥ 92% (matching or exceeding iDEAL 2.0 / Apple Pay authorization benchmarks)  

---

## 1. Executive Summary & Conversion Objectives

Account-to-Account (A2A) / Pay by Bank payments eliminate card interchange fees, chargebacks, and intermediary processors. However, consumer drop-off typically occurs at three critical friction points:
1. **Bank Selection Friction:** Payer is overwhelmed by a long, unorganized list of banks or cannot quickly locate their institution.
2. **SCA Anxiety / Redirection Shock:** Payer is startled by an abrupt redirect to an external bank domain or fears phishing.
3. **App-to-App Breakage:** On mobile devices, in-app webviews (Instagram, WhatsApp, TikTok) fail to trigger native banking app universal links.

**Core Objective:** Deliver a frictionless, mobile-optimized checkout component that loads in **< 100ms**, enables bank selection in **under 2 taps**, handles Strong Customer Authentication (SCA) seamlessly across mobile and desktop, and provides real-time settlement feedback.

---

## 2. Core Screen States & User Journey

The checkout UI consists of four unified functional states:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PAY BY BANK STATE ENGINE                        │
├────────────────────┬────────────────────┬──────────────────────────────┤
│ State 1: Select    │ State 2: SCA       │ State 3: Waiting / Status    │
│ Bank & Search      │ Handoff            │ Polling & Real-Time Feedback │
├────────────────────┼────────────────────┼──────────────────────────────┤
│ • Merchant summary │ • Mobile: Direct   │ • WebSocket / Polling status │
│ • Top quick-grid   │   Universal Link   │ • Step-by-step progress      │
│ • Instant search   │ • Desktop: Dual    │ • Bank response listener     │
│ • Local persistence│   QR code + web    │ • Auto-timeout guard (15 min)│
└────────────────────┴────────────────────┴──────────────────────────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │ State 4: Settlement    │
                     │ Confirmed / Success    │
                     └────────────────────────┘
```

---

## 3. Detailed Component Specifications

### 3.1 Order Summary & Trust Header
* **Order Context:** Prominently display the merchant name, merchant logo/avatar, order reference number (`ORD-xxxxx`), and payment total in clear currency format (`€ 149.00`).
* **Payment Method Indicator:** A clear label identifying the rail: `Pay by Bank • Direct Bank Transfer`.
* **Consumer Guarantee Tag:** Clear reassuring micro-copy: *"Direct transfer from your bank account. No credit card surcharges. 100% encrypted."*

---

### 3.2 Bank Selection Engine (Search & Quick-Pick)

To avoid cognitive overload while supporting dozens of European banks, the bank selector is organized into a **tiered layout**:

#### Tier A: Recent Bank Memory (Local Persistence)
* **Behavior:** On first visit, standard default order is shown.
* **On Return Visits:** Read `localStorage.getItem("cm_pisp_preferred_bank")`. If a bank was previously used, display a dedicated **"Your Preferred Bank"** pinned card at the very top with a `RECENTLY USED` badge.
* **Conversion Impact:** Reduces repeat checkout to a **single tap**.

#### Tier B: Top National Quick-Select Grid
* Displays the primary market banks (covering >85% of market volume) as prominent interactive cards:
  * **ING Bank**
  * **Rabobank**
  * **ABN AMRO**
  * **De Volksbank** (SNS / ASN / RegioBank)
* **Card Structure:**
  * Official vector bank SVG logo.
  * Clear bank brand name.
  * Supporting feature tag: `Instant Transfer Supported`.
  * Single-click selection toggles an active state and updates the primary action button.

#### Tier C: Instant Multi-Attribute Search Bar
* **Position:** Prominently positioned with the bank list.
* **Placeholder:** `"Search your bank (e.g. bunq, Revolut, Knab, BIC)..."`
* **Keystroke Performance:** Debounced by 40ms, client-side filtering executing in < 5ms.
* **Multi-Attribute Matching:** Matches against:
  1. Primary bank name (e.g., `Rabobank`, `ABN AMRO`).
  2. Informal colloquial nicknames (e.g., typing `Rabo` matches `Rabobank`; typing `ASN` or `SNS` matches `De Volksbank`).
  3. Bank Identifier Codes (e.g., typing `INGBNL2A` matches `ING Bank`).
  4. Country filter tabs (e.g., `Netherlands`, `Belgium`, `Germany`).
* **Empty State:** If no bank matches, show an informative fallback:
  > *"Can't find your bank? Ensure the name is spelled correctly or enter your IBAN directly to auto-detect your bank."*

---

### 3.3 Strong Customer Authentication (SCA) Handoff

When the user clicks the primary CTA (`[Continue with <Bank Name>]`), the frontend initiates the transaction with the gateway and transitions to the SCA handoff screen:

#### Mobile Mode: App-to-App Deep Linking
* **Primary Flow:** Mobile devices must launch the bank's native mobile banking app directly using **iOS Universal Links** or **Android App Links** (e.g. ING Mobiel Bankieren, Rabo App, ABN AMRO Mobiel).
* **CTA Button:** Large full-width primary button: `[Open <Bank Name> App to Authorize]`.
* **In-App Browser (IAB) Protection:** If the user is inside an embedded webview (Instagram, Facebook, LinkedIn, TikTok), render a prominent notice:
  > *"Tap the menu (⋮ or ···) in the corner and select 'Open in Safari / Chrome' to allow your bank app to open securely."*

#### Desktop Mode: Hybrid Dual-Handoff (QR Code + Browser Redirect)
On desktop screens, provide two parallel options to satisfy both mobile-app preference and desktop web users:
1. **Scannable Companion QR Code (Primary):**
   * High-contrast QR code generated client-side from the bank's `scaRedirect` URL.
   * Clear instructions: *"Scan with your phone camera or banking app to approve with Face ID / PIN."*
2. **Direct Browser Login (Secondary):**
   * A secondary button / link: `[Open Online Banking in New Tab]`.
   * For desktop users with physical authenticators (e.g. Rabo Scanner, ABN e.dentifier, or SMS TAN).

---

### 3.4 Real-Time Settlement Polling & State Feedback

While the payer is in their banking app, the checkout page **must never reload or go blank**.

* **Polling / WebSocket Listener:** Gateway polls `GET /api/v1/payments/{paymentId}/status` every 2.0 seconds (or listens on a WebSocket/SSE topic).
* **Visual Status Animation:**
  * Animated progress indicator showing: `Waiting for Bank Approval`.
  * Step progression:
    * Step 1: Bank selected (Completed).
    * Step 2: Confirm transfer in bank app (In Progress).
    * Step 3: Instant settlement confirmation (Pending).
* **Cancel / Change Bank Option:** Provide an easy option to abort and change bank: *"Cancel or select a different bank"*, returning to Step 1 without page refresh.
* **Auto-Timeout Guard:** If no response is received within 15 minutes, transition to an expired screen with a one-click `[Retry Payment]` option.

---

### 3.5 Confirmation & Success Screen

The moment the bank confirms authorization (`ACCP` / `ACSC`):

* **Celebration Banner:** Clear visual confirmation of payment success.
* **Transaction Receipt Block:**
  * Merchant Name
  * Payment Reference
  * Bank Reference ID
  * Execution Timestamp
  * Payment Rail (`SEPA Instant Credit Transfer`)
* **Auto-Redirect Countdown:** *"Redirecting to merchant confirmation in 4 seconds..."* with a manual button `[Return to Merchant Now]`.

---

## 4. Trust, Security & Regulatory Signaling

Because consumers are cautious about banking authentication, the UI must prominently display authoritative trust anchors:

1. **Regulatory Statement:**
   > *"CM Payments B.V. is authorized and supervised by De Nederlandsche Bank (DNB) as a licensed Payment Institution (Relation: R129862)."*
2. **Data Privacy Reassurance:**
   * *"We never see, store, or ask for your bank login credentials or PIN."*
   * *"Authentication occurs exclusively on your bank's official secure portal or mobile app."*
3. **Security Indicators:**
   * 256-bit bank-grade encryption indicator.
   * PSD2 / RTS compliance confirmation.

---

## 5. Accessibility & Responsive Specifications

* **WCAG Compliance:** Strict **WCAG 2.1 AA** conformance:
  * Minimum touch target size: **48px × 48px** for all bank cards and buttons on mobile.
  * Contrast ratio meeting accessibility standards.
* **Keyboard Navigation:** Full arrow-key navigation through the bank list, with `Tab` focusing into search and `Enter` triggering bank selection.
* **Screen Reader Support:** ARIA attributes (`role="radiogroup"`, `aria-checked="true"`, `aria-live="polite"` on status updates).
* **Responsive Layout:**
  * **Mobile (< 640px):** Single-column stacked layout, full-width sticky bottom CTA, deep link app handoff prioritized.
  * **Tablet / Desktop (≥ 640px):** Multi-column bank grid, dual QR + web redirect view, and persistent order summary.

---

## 6. Frontend Technical Architecture & API Contracts

```
1. Bank Directory Listing:
   GET /api/v1/banks?country=NL
   Response: Array<{ id, name, bic, logo_url, instant_supported, popular }>

2. Create Payment Initiation:
   POST /api/v1/payments
   Body: { bank_id: "ing", amount: 149.00, currency: "EUR", merchant_ref: "ORD-123" }
   Response: { payment_id, status: "RCVD", sca_redirect_url, qr_payload, expires_at }

3. Check Payment Status:
   GET /api/v1/payments/{payment_id}/status
   Response: { payment_id, status: "ACSC" | "ACCP" | "RJCT" | "PDNG", settled_at }
```
