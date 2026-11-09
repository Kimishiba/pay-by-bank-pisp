# CM.com Hosted Checkout: implementation handoff

Merchant used in all mocks: **Amnesia Ibiza** (amnesia.es), order `AMN-2026-08421`, 2 × General admission, **€120.00**, date shown as `7 November 2026, 14:32` (the Main/Scroll/Grid/Card boards use merchant data from a props enum; see Main).

Eight boards, 1440×1000 desktop frames (updated 9 Nov 2026: single Back button, grey merchant side, Bancontact footer, new `FramerList` board). Live visual reference (org-shared): https://claude.ai/artifact/8N4ovJW9rwzx3Y1Zo5x9yN (canvas "Design" artifact; the hosted URL is the source of truth for how each board looks).

## 1. What is in this bundle

| Path | Purpose |
|---|---|
| `source/*.dc.html` | The 7 boards as prototype source (authoritative for exact CSS values, copy, sizes, state logic). |
| `source/canvas.json` | Board titles, sizes, canvas positions. |
| `assets-named/` | All logo/image assets with readable names. |
| `asset-map.json` | Maps the `/_blob/<id>` URLs used in the sources to files in `assets-named/`. |
| `design-system/` | CM.com tokens (`colors_and_type.css`, README). Montserrat is the CM.com font. |

### About the `.dc.html` format
These are prototype files for a canvas tool, not production code. They are plain HTML/inline CSS plus:
- `{{value}}` bindings, `<sc-if value="{{x}}">`, `<sc-for list="{{xs}}" as="x">`.
- A `class Component extends DCLogic` block at the bottom with `this.state` and `renderVals()` (returns values and event handlers like `onInput`). Treat it as a React-style component: state in, view-model out.
- `<script src="./support.js">` is the prototype runtime. Do not port it.
- `/_blob/<id>` image URLs are resolved through `asset-map.json`.
Re-implement in the target stack (React or whatever the checkout uses). Keep the visuals, copy and behaviour below.

## 2. Boards

| File | Title | Layout | Notes |
|---|---|---|---|
| `Main` | Checkout, web | Single 480px card on grey | Order summary panel (Date, Order reference, Amount). Express row (Apple Pay, PayPal, Google Pay), then "Or pay with" list of 5 methods. Footer: dark grey `#2B2F36`, "Secured by" + white CM.com logo. |
| `Scroll` | Many payment methods | Same as Main | 12 methods in a scrollable list: iDEAL, Wero, Card (Visa/MC, Click to Pay), Bancontact, Klarna, BLIK, Przelewy24, SOFORT, Amex, in3, Riverty, KBC, Alipay. |
| `Grid` | Logo-only grid | Same as Main | Methods as a 2-wide grid of logo tiles, no names. |
| `Card` | Card details | 480px card | Click to Pay button, "Or enter card details", dynamic flip-card preview, form (number, name, expiry, CVC), Pay button. |
| `FramerList` | Split layout, 1-wide list | Copy of `Framer` with the payment methods in a single column (scroll area 360px) | Same behaviour as `Framer`. |
| `Framer` | Split layout | 1000px floating box, two halves | Left: merchant, "Complete your payment", date + order reference, amount. Right: express row, 2-column scrollable method list (13 methods), dark-blue footer. |
| `FramerCard` | Split layout, card details | Same split box | Right half: back link to `Framer`, flip-card preview, form, Pay €120.00. |
| `Bancontact` | Bancontact (QR + card) | Same split box | Right half: Bancontact Pay (QR plus steps), divider, Bancontact Card (number + expiry only), footer. |

**Navigation (updated):** every board has exactly one "Back" control, top-left, that returns the payer to the merchant shop (placeholder `https://amnesia.es`; production uses the merchant's return/cancel URL). The old "Choose another payment method" links were removed. Boards are no longer linked to each other.

## 3. Design tokens

Narrow boards (Main, Scroll, Grid, Card) use the CM.com design system:
- Text `#101E1E`, secondary `#5A6372`, labels `#344055`, borders `#E6E8EB`/`#DADCE0`, accent `#007FFF`.
- Pay button gradient `linear-gradient(60deg, #0074E8, #5D11DC)`, success `#1F7A4D`, error `#B42318`/`#E5484D`.
- Font: Montserrat (`design-system/colors_and_type.css`).

Split boards (Framer, FramerList, FramerCard, Bancontact) use a neutral palette and Inter:
- Page bg `#F5F5EF`, box white, radius 20px, shadow `0 2px 6px rgba(25,32,16,.03), 0 20px 70px -16px rgba(25,32,16,.16)`.
- Text `#20221F`, muted `#797C74`, borders `#E3E4DE`/`#ECEDE7`, selected border `#20221F`.
- **Merchant (left) side background `#F4F4F4`, muted text `#666666`**, to separate merchant info from the payment side.
- Right-half footer `#0D314B` (dark blue) with "Secured by CM.com"; on Bancontact it reads "Powered by CM.com" with the Bancontact logo removed from the footer (see 6).
- Pay button `#20221F`, success `#1F7A4D`. Inputs: 48px high, radius 10px, 1px border, focus ring `0 0 0 3px rgba(32,34,31,.1)`.
- Box: max-width 1000px, min-height 740px, centred vertically, 48px/24px page padding, halves wrap below ~840px.

Read exact values from the source files rather than this summary.

## 4. Behaviour

### Payment method list (Main, Scroll, Grid, Framer)
- Single selection, `picked` state, selected tile gets a darker border / tint. Entries are buttons with `aria-pressed`.
- Framer list (13): Credit or debit card, Pay by bank, Klarna, iDEAL, Wero, Sofort, Bancontact, Riverty, Billink, EPS, Przelewy24, Multibanco, Paysafecard. Descriptions are in `Framer.dc.html`.
- Placeholder "Logo" tiles (no asset yet): Billink, EPS, Multibanco, Paysafecard (Framer), plus Maestro, Carte Bancaire, SEPA where present.
- Express row: Apple Pay (black button, white glyph), PayPal in the middle (yellow `#FFC439`), Google Pay (white, outlined). See 6 for button rules.

### Card form (Card, FramerCard)
- Brand detection from the leading digits: Visa `4`, Mastercard `51-55` / `2221-2720`, Amex `34`/`37`.
- Number grouping 4-4-4-4, Amex 4-6-5. Max length 16 (Amex 15). Luhn check once complete; error "Check your card number and try again."
- Expiry `MM/YY`, auto-inserts `/`, month clamped to 1-12, error if in the past: "This card has expired or the date is not valid."
- Name: digits stripped, max 26. CVC: 3 digits, Amex 4.
- Pay is disabled until number, expiry, name and CVC are valid. Status `idle` → `paying` ("Processing…") → `done` ("Payment complete", green). The prototype fakes this with a timeout; replace with the real flow.
- **The card preview updates live as the user types**, with the focused field highlighted on the card (`rgba(255,255,255,.2)`). Card background gradient changes by brand. When the CVC field is focused the card flips (rotateY 180°, 600ms ease; disabled under `prefers-reduced-motion`). The card preview is decorative (`aria-hidden`).
- Inputs need per-keystroke handlers (`onInput`), not only change events.
- Never store or log PAN/CVC outside the hosted fields; use the PSP's secure fields in production.

### Bancontact board
- Two stacked sections, no alternative payment methods once Bancontact is chosen.
- Bancontact Pay: QR, 3 steps ("Open the Bancontact Pay app or your banking app", "Scan this code", "Confirm the payment on your phone"), "Waiting for your payment" pulse indicator.
- Bancontact Card: card number + expiry only (no name, no CVC, no card preview). Bancontact cards start `6703` in the placeholder; validation is Luhn + expiry.
- **The QR in the mock is a decorative random pattern (`makeQr()`). In production render exactly the QR returned by the API, unmodified.**
- Date/time and order reference are in the left panel as the guideline requires on the payment page: date, order reference, total price, beneficiary.
- Footer: "Powered by CM.com" only (the Bancontact logo is shown next to each section heading, not in the footer). Added at the product owner's request, see 6.

## 5. Assets
- `asset-map.json` lists every `/_blob/` id → file. Logos are SVG except Wero, Amnesia and CM.com (PNG).
- `bancontact-OLD-replace-by-2026-12-31.svg` is the **pre-2026 Bancontact logo and must be replaced** with the current Bancontact Brand Portal files (see 6) before launch. It is used for the Bancontact tile in Framer, in the Bancontact board (Pay tile, Card tile, footer) and in Main/Scroll/Grid.
- `cm-logo-horizontal-white.png` is the logo in the "Secured by" footers; `cm-logo-horizontal-dark-unused.png` is not referenced.
- Sofort currently shows the Klarna-branded logo from the design system.
- Click to Pay icon, Apple Pay/Google Pay glyphs and the QR are placeholders or hand-drawn SVG. Replace with licensed/official assets (below).

## 6. Brand and compliance rules to honour
- **Apple Pay**: the mark is not a button; use Apple's official buttons (black, white, white with outline), unaltered. Custom buttons must not show the logo.
- **Google Pay**: official buttons only, dark button on light backgrounds, no white-on-white, no changes to font, colour, radius or padding.
- **Click to Pay (EMVCo v2.0)**: licensed icon, solid colour, minimum 20px height (12px in tight spaces), clear space 0.25×, shown with network logos, helper image for card buttons. Never write "click 2 pay".
- **Bancontact** (brand.bancontact.com, online acceptance):
  - Acceptance mark required on the selection page. Combined tagline (English): "Pay with your Bancontact Pay app, your banking app supporting Bancontact payments or Bancontact Card." Separate: Pay = "Pay with your Bancontact Pay app or your banking app supporting Bancontact payments"; Card = "Pay with your Bancontact card".
  - Card page asks only card number and expiry. Payment page header must show date, order reference, total price and beneficiary.
  - Footer should show only the Bancontact/Pay/Card logo, no other brands. **The current mock instead shows only "Powered by CM.com" in the footer at the owner's request, which departs from this; confirm with Bancontact/compliance before launch.**
  - Logos were updated in 2026; old versions must be replaced by **31 Dec 2026**. Download: `Bancontact_LogoSet.zip` on the portal logo page. Each product needs its own logo (Bancontact Pay, Bancontact Card). Min sizes: horizontal 20px high, vertical 50px wide. The Bancontact logo must not be visually smaller than partner logos.
  - QR must be rendered exactly as the API returns it.

## 7. Known gaps / open items
1. Replace the old Bancontact logos with the official 2026 set (not yet downloaded; needs the zip from the Bancontact Brand Portal).
2. Replace placeholder tiles (Billink, EPS, Multibanco, Paysafecard, Maestro, Carte Bancaire, SEPA) with real logos.
3. Express buttons on Main/Scroll/Grid are logo-in-box, not the official Apple Pay/Google Pay buttons; the Framer board uses closer-to-spec buttons. Use the official SDK buttons everywhere.
4. Order-summary copy and amounts differ between merchants in the Main-family boards (`merchant` prop: home/coffee/furniture/outdoor); the split boards are hard-coded to Amnesia.
5. The date/time is a static string; wire to the real order timestamp (locale-formatted) and add the beneficiary name to the Bancontact header.
6. Accessibility already in the prototype: labelled inputs, `aria-pressed` on method buttons, visible focus rings, reduced-motion support. Keep them.
7. Responsive: the split box wraps at narrow widths; only desktop (1440) boards were designed. Mobile views still need to be done.

8. A reference implementation of the split layout (card form with live card, Bancontact screen, Back button) exists in `../hosted-checkout-implementation/`.
