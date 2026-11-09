# Hosted checkout: card form with live card, Bancontact screen, single Back button

Implements the behaviour from the design mockups (split layout family) on top of the existing `public/checkout.html`. Plain HTML/JS, no new dependencies, served by the Go gateway as before.

## What changed

**`public/checkout.html`** (rewritten in place, pay-by-bank flow and API calls kept)
- **Single "Back" button** (top-left of the merchant side). Returns the payer to the merchant (`CONFIG.merchant.returnUrl`, http/https only), stopping any polling or countdown first. The old "Choose another payment method" links are removed from the bank-select pane.
- **Merchant side is neutral grey** (`#F4F4F4`, muted text `#666666`) to separate merchant info from the payment side.
- **Date and time** (`7 November 2026, 14:32`, Europe/Amsterdam) above the order reference, driven by `CONFIG.order.createdAt`. Order, amount and merchant now come from one `CONFIG` object instead of being hard-coded in several places.
- **Method list** is rendered from one `METHODS` array (13 methods). Card, Bancontact, Pay by bank and iDEAL open their screens; the others show an inline "not connected in this demo yet" status instead of `alert()`.
- **Card screen**: live flip card. Number, name, expiry and CVC update the card while typing; the focused field is highlighted; the card flips for CVC; brand detection (Visa, Mastercard, Amex) changes colour and logo and the number grouping (Amex 4-6-5) and CVC length (Amex 4). Luhn and expiry validation; Pay is disabled until valid.
- **Bancontact screen**: Bancontact Pay (QR + steps + waiting indicator) above Bancontact Card (number + expiry only, no name or CVC), per the Bancontact guidelines. Combined tagline on the method tile, beneficiary row shown in the header, footer reads "Powered by CM.com".
- **Footer**: "Secured by CM.com" everywhere, "Powered by CM.com" on the Bancontact screen.
- **Shared success receipt** for every method, with a redirect back to the merchant after 5 s.
- Deep links: `?method=card|bancontact|pay-by-bank`.

**`public/card-utils.js`** (new): pure card helpers (brand, formatting, Luhn, expiry, masking). Unit tests in `public/card-utils.test.js`; run `node --test public/card-utils.test.js` (Node 18+, no dependencies).

**`public/assets/amex.svg`** (new): Amex mark for the card preview.

## Not done / needs follow-up
- **No PSP integration for cards or Bancontact.** `CONFIG.demoMode = true` simulates approval. Marked with `TODO(PSP)` / `TODO(Bancontact)`. In production the PAN and CVC must be captured by the PSP's hosted fields (PCI SAQ-A) and never sent to this gateway.
- **Bancontact QR** is a placeholder (demo URL). `renderQr()` must be given the exact payload returned by the Bancontact Pay API, unmodified.
- **Bancontact logo**: `assets/bancontact.svg` must be replaced with the 2026 logo set (old logos must be gone by 31 Dec 2026). The "Powered by CM.com" footer on that screen departs from Bancontact's "footer shows only the Bancontact logo" rule; confirm with Bancontact / compliance.
- Express wallet buttons (Apple Pay, PayPal, Google Pay) are static visuals; real integrations need each provider's official buttons.
- `merchant.returnUrl` is a placeholder (`https://amnesia.es`). The gateway should inject the real return URL per order. Signed status parameters on return are not implemented.
- Only the split layout is implemented. The narrow single-column design variants (Main, Scroll, Grid, Card) are not.

## Testing
- `node --test public/card-utils.test.js`: 8/8 passing.
- Page behaviour exercised in jsdom: method selection, card live preview and validation, Bancontact screen and footer, pay-by-bank flow through to the receipt, single Back control. Not yet checked visually in a real browser or on mobile widths.

## Deploy note
Merging to `main` triggers `.github/workflows/deploy.yml`. No server, Dockerfile or workflow changes are included.
