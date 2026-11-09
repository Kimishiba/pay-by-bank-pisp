# CM.com Design System

> The only AI platform that runs the whole conversation and everything it leads to.

This is a working design system for **CM.com** (AMS: CMCOM) — a leading European technology company that helps organizations worldwide improve customer interactions through integrated solutions for **communications, payments, and AI**. CM.com is headquartered in Breda, The Netherlands, serves customers in 100+ countries, and has ~650 employees and 15 offices globally.

---

## What's in this system

### Foundations
- `colors_and_type.css` — CSS custom properties for the full color scale, semantic text styles, shadow + radius tokens, plus a small utility layer (`.btn-primary`, `.chip`, `.card`, …)
- `fonts/` — **Montserrat** (Thin → Black + italics), **Noto Sans Arabic** (Thin → Black), **Noto Sans Simplified Chinese** (Thin → Black), **Noto Sans Traditional Chinese** (Thin → Black on request), and **Noto Sans Japanese** (Thin → Black). Montserrat for Latin/English. Non-Latin scripts use their corresponding Noto Sans family.
- `assets/logos/` — CM.com horizontal / vertical / symbol-only lockups, as PNG. Three variants per lockup: **default (dark)** for light backgrounds, **outlined** (white outline) for dark backgrounds (preferred), and **all-white** (filled white) as a contrast-fallback for very busy or near-white dark backgrounds.
- `assets/icons/` — **354 Aurora Icon SVGs** (24×24, default fill `#344055` — a reference color, recolor freely).
- `assets/app-icons/` — **~60 App Icons** (PNG, 64px source). One per CM.com app product. Duotone (blue→purple gradient + Black 120 or white). `*-positive.png` for light surfaces, `*-negative.png` for dark surfaces.
- `assets/solution-icons/` — **12 Solution Icons** (SVG, 160 + 96px). Illustrative icons for CM.com's named solutions: CAIC, MSC, MMC, CPaaS, PSP, Sign, Ticketing, TraceDock, Voice, HALO, Mobile Identity Services, Central Services. Ship in **light positive**, **light diapositive**, and (for some) **dark diapositive** variants.
- `assets/channels/` — Channel logos (**SVG**): WhatsApp, Messenger, Instagram, Telegram, Viber, LINE, RCS, Push, Mail, SMS, MMS, Voice, X. Full-colour trademarks — use as-is, never recolour.
- `assets/channels/` — **41 Channel logos** (SVG, full-color trademarks): 20 primary channels (WhatsApp, Messenger, Instagram, Telegram, Viber, LINE, RCS, SMS, MMS, Voice, Push, Mail, Verified SMS, WeChat, Live Chat, Apple Messages, Slack, Teams, TikTok, Google) + 20 greyscale variants + X. Use as-is, never recolor.
- `assets/partners/` — Meta lockup.
- `assets/mockups/` — **Full device mockup library** (PNG, transparent backgrounds): iPhone / Android / iPad / MacBook / iMac in front + 3 dynamic angles + side views, plus a pre-branded CM.com test credit card and a 3-phone hero cover.

### Preview cards (`preview/`)
Bite-sized HTML cards for the Design System tab — color scales, type specimens, button states, channel icons, logo lockups, tone-of-voice examples.

### UI kits (`ui_kits/`)
(No UI kits currently in the system.)

### Research
- `research/communication-guidelines.txt` — Full extracted text of the internal Communication Guidelines.docx.
- `research/brandbook-summary.md` — Distilled summary of the attached Brand Book v2.3 (May 2026).
- `research/brandbook-attached.txt` — Raw text extracted from the PDF.

### Sources received
- **CM.com Brand Book v2.3 (May 2026)** — attached PDF, parsed in full.
- **Communication Guidelines.docx** — internal voice/tone document.
- **Logo SVG pack** — horizontal/vertical/symbol × RGB / all-white / white-outlined.
- **Channel logo bundle** — WhatsApp, Messenger, Instagram, Telegram, Viber, RCS, Push, Mail, SMS, MMS, Voice, X, Meta lockups.
- **Web Icons.zip** — 354 SVGs.
- **Montserrat TTF family** — full weight range, the only font now used.
- **Primary / Secondary / Tertiary button reference images.**
- **Full device mockup library (PNG)** — iPhone / Android / iPad / MacBook / iMac in front + 3 dynamic angles + side views, plus a pre-branded CM.com credit card and a 3-phone hero cover.

---

## Content Fundamentals

CM.com's voice is **approachable, positive, professional with a personal touch**. The instruction is explicit: *"We're a personal company, so don't write too formal. However, refrain from making jokes."* That balance — warm but never goofy — is the whole tone in one sentence.

### Voice characteristics
- **Person:** Second person, always. "Address your reader. Don't be afraid to say *you/your*." First-person plural ("we", "our") for CM.com itself.
- **Brand name:** **CM.com**, never "CM". The casing is fixed: **`CM`** in capitals, **`.com`** in lowercase — always exactly **CM.com**. Never `Cm.com`, never `cm.com`, never `CM.COM`. Product names always start with a capital and don't take "the" (write "Marketing Cloud", not "the Marketing Cloud"). Product names are **never abbreviated externally** (Marketing Cloud, Service Cloud, Conversational AI Cloud).
- **Title capitalization** — Capitalize Titles per **APA rules**, with one CM.com tweak:
  - Capitalize the **first word** of the title/heading and of any subtitle/subheading.
  - Capitalize all **major words**: nouns, verbs (including phrasal verbs like "play with"), adjectives, adverbs, pronouns. Including the **second part of hyphenated** major words (`Self-Report`, not `Self-report`).
  - Capitalize all **words of four letters or more**.
  - **CM.com override:** always capitalize the **last word**, regardless of part of speech. APA leaves some sentence-ending prepositions lowercase ("When the Lights Go on") — CM.com style is "When the Lights Go On."
- **Product-name shortcuts** — Always write **Service Cloud** and **Marketing Cloud**. Never *"Mobile Service Cloud"* or *"Mobile Marketing Cloud"* — the "Mobile" prefix is dropped externally.
- **Product-name capitalization** — Product names always start with a capital letter. **Exceptions:** **iDIN** and **iDEAL** keep the lowercase-i.
- **Language default:** US English globally. UK/SA English in those regions only.
- **Emoji:** Not used. The visual identity carries the warmth.
- **Imperatives:** Avoid in body copy ("ought to", "should", "must"). The exception is **CTA buttons** where short imperatives are correct: *Apply Now*, *Read more*, *Get started*, *Book a demo*.
- **Humor / sarcasm / metaphors:** Avoid — they translate badly.
- **Comparisons to competitors:** Don't speak negatively. Avoid statements that put one CM.com product above another (don't say "SMS open rate is higher than email" — say "SMS open rate is xx%").
- **Active over passive.** Present/future over past. *"The developer updated X"*, not *"X was updated by the developer."*
- **Abbreviations:** Spell out on first use: *"Rich Communication Services (RCS). RCS is…"*
- **Numbers:** Be concrete. Don't say "many" if you can say exactly how many.
- **Connectives:** Use "because" — research shows it's more persuasive than "for this reason".
- **Partner-name rules** (legal):
  - **WhatsApp** — "WhatsApp" or "WhatsApp Business". We are a **WhatsApp Business Solution Provider**, *never* "partner".
  - **Apple** — "Apple Messages for Business". **Never** "iMessage". Don't claim we partner with Apple.
  - **People** — "Jeroen (van Glabbeek)" — first name + parenthetical surname.

### Specific examples
- ✅ *"If you compare X and Y…"* &nbsp; ❌ *"Compare X and Y"* (avoid the imperative).
- ✅ *"the open rate of SMS is xx%"* &nbsp; ❌ *"the open rate of SMS is much higher than email"*.
- ✅ *"For this purpose you can use Rich Communication Services (RCS). RCS is…"* (spell-then-abbreviate).
- ✅ *"Register now"* on a CTA. &nbsp; ❌ *"You must register now"* in body copy.
- ✅ *"Discover research insights"* link text. &nbsp; ❌ *"Read more"* link text.

### Sub-brand tone variations
- **General / SaaS** — the baseline tone above.
- **Payments & POS** — same tone, *slightly* more corporate. More specific, more detailed.
- **LIVE / AppMiral** (festivals, parks, venues, sport events) — "writes like a festival operator with taste — energetic, confident, sharp, human, slightly edgy. Never enterprise or corporate SaaS."

---

## Visual Foundations

### Colors
The brand is built on a **purple–blue–cyan** identity with **orange as the dedicated CTA accent**. The color system uses a numeric-tier scheme (`Purple 100`, `Blue 130`, etc.) where 100 is the canonical brand value; higher numbers darken, lower numbers lighten.

The hierarchy:
1. **Purple 100** `#6610F2` — primary identity color ("ambition, creativity, innovation")
2. **Blue 100** `#007FFF` — trust, support color
3. **Cyan 100** `#04E4F4` — highlight only (small details, accents — never large surfaces)
4. **Black 140** `#101E1E` — body text (deliberately softened from pure black)
5. **Orange 100** `#FFA400` — **standard CTA button color**, plus emphasis highlights

**The 60/40 rule.** All compositions should be roughly 60% purple + 40% blue/cyan.

### Typography (v2.3 May 2026 — Montserrat-only)
- **Titles** — **Montserrat Black** (weight 900). Letter-spacing **−15 / ≈ −0.015em**.
- **Subtitles / longer titles** — Montserrat SemiBold (600). Tracking 0.
- **Lighter subtitles** (paired with a Black title for hierarchy) — Montserrat Light (300). Tracking 0.
- **Quotes / citations** — Montserrat Bold Italic.
- **Body text** — **Montserrat Regular** (400).
- **Highlighted text** — Montserrat Bold (700).
- **Versatile** — Montserrat Light (300) / Medium (500).
- **Non-Latin alternates** — Noto Sans Arabic, Noto Sans TC, Noto Sans JP. Only for non-Latin scripts; Latin alphabet always uses Montserrat.
- **Leading** — "airy, slightly oversized" — text should never feel crowded.

### Backgrounds
- **Title / cover surfaces** are saturated: purple→blue gradient.
- **Content surfaces** are mostly white with the dark text color (`#101E1E`).
- Hero photography uses **circular masks** with bright cyan rim accents.

### Buttons (precise spec from p.27 of v2.3 May 2026)

All buttons are pill-shaped, **30° gradient**, with three color stops at 0% / 25% / 100%.

| Variant | Default stops | Hover stops |
|---|---|---|
| **Primary · Blue–Purple** | Blue 110 → Purple 110, white text | Blue 120 → Purple 120 + glow |
| **Tertiary · Blue–Blue** | Blue 100 / Blue 120@25% / Blue 100, white text | 110 / 130@25% / 110 |
| **Tertiary · Purple–Purple** | Purple 100 / Purple 120@25% / Purple 100, white text | 110 / 130@25% / 110 |
| **Secondary · Cyan–Blue** | Cyan 080 / 080@25% / Blue 080, black text | 090/090/090 |
| **Secondary · Yellow–Orange** | Yellow 080 / 080@25% / Orange 100, black text | 090/090/110 |
| **CTA · Orange** | Orange 100 (per color page — the "standard CTA") | + glow |

All buttons fully rounded (pill). Outlined variants exist for each; the gradient becomes the border.

### Animation
The brand book doesn't legislate motion; the implied feel is **forward and upward**. In this system that translates to:
- Subtle ease-out transitions (180–240ms for hovers, ~400ms for entering elements).
- Buttons gain a soft shadow on hover; no scale jumps, no bouncy springs.

### Hover & press states
- **Hover** — gradient stops shift one tier darker. A soft, low-spread shadow appears (`0 12px 32px rgba(102, 16, 242, 0.32)` purple, or blue/orange equivalent).
- **Press / active** — drop the shadow, no scale change.
- **Focus-visible** — outline ring in `Blue 100` at 2px with 2px offset.
- **Disabled** — 40% opacity, no shadow.

### Borders, radii, shadows
- **Pill radius** — 9999px on all interactive elements.
- **Card radius** — 16px (medium), 24px (large hero cards), 8px (compact controls).
- **Borders** — usually transparent. When visible, 1px solid in `Black 40` for neutral or `Purple 100`/`Blue 100` for accent.
- **Outer shadows** — soft, colored to the brand:
  - `shadow-sm`: `0 1px 2px rgba(16, 30, 30, 0.06)`
  - `shadow-md`: `0 8px 24px rgba(16, 30, 30, 0.08)`
  - `shadow-lg`: `0 24px 56px rgba(102, 16, 242, 0.18)` (purple-tinted)
- **Inner shadows** — not used.

### Layout
- 12-column grid on the marketing site; 8px base spacing unit.
- Hero block is full-bleed gradient; content blocks alternate white and "Purple 180 / 100" backgrounds.
- Section header pattern: **eyebrow** (Montserrat SemiBold uppercase in Cyan 110) → **title** (Montserrat Black) → optional **subtitle** (Montserrat Regular).

### Text containment (mandatory)
**Text must never run outside the page, frame, slide, card or container.** This is the most common breakage in CM.com deliverables — long titles (`One Platform. Every Step of the Customer Journey.`) clip off the bottom of a slide, body copy overflows a card. Before shipping any asset, verify every text block fits inside its container.

How to enforce it:
- **Always size headlines responsively.** Use `clamp(min, preferred, max)` for hero/display sizes so they scale down on smaller frames instead of overflowing. Never pin a display headline to a single huge fixed `font-size`.
- **Reserve a safe area.** Keep a minimum 48px padding inside slides/cards; titles cannot extend into that gutter.
- **Use `text-wrap: balance`** on headings — keeps line breaks even, avoids one short trailing word that pushes height.
- **Test with the longest realistic copy.** Don't lay out with "Lorem" — drop in the actual longest title the deck/page will ever carry, and let CSS reflow.
- **For slides specifically:** the title block has a fixed height. If the title needs more lines, the font size shrinks — the slide does not grow. PowerPoint's "Shrink text on overflow" is acceptable on title placeholders; never on body.
- **For cards in a grid:** set `min-height` on the card, not `height`. Let the card grow vertically with its content. Use `overflow: visible` (never `hidden`) on text containers unless you genuinely intend to clip.
- **Never use a `height` taller than `100vh`** on a section that has body copy — the content can't escape downward and will clip.
- **No `position: absolute`** on text inside a positioned parent unless you've explicitly accounted for overflow.

If a title is still overflowing after sizing fixes, shorten the copy. The container is the rule; the copy adapts.

### Transparency & blur
- Cyan and purple shapes layered at **20–40% opacity** behind hero photos and titles.
- Backdrop blur (`backdrop-filter: blur(17px)`) is direct from the brand-book "Blurred Variant" spec.
- **Glass cards** — for surfaces placed on dark / brand-gradient backgrounds, use the `.glass` (white 5% bg + border 10%) or `.glass-strong` (white 8% bg + border 18%) utility classes. Both apply a 17px backdrop blur, so they pick up colour from whatever's behind them. Use `glass-strong` when the card needs more presence; default `.glass` for ambient overlays.

### Imagery
- Warm, real people, slightly saturated, **never B&W**.
- People typically masked into a **circle** with a 4–8px cyan ring or partial cyan arc.
- Subjects often holding a phone — emphasizes CM.com's mobile-channel positioning.

### Devices (Brand Book rules)
- Use only the **provided device mockups** (`assets/mockups/`) — iPhone, Android, iPad, MacBook, iMac. Front + 3 dynamic angles + side views are shipped.
  - **Actively check channel × OS availability per request.** Channel support changes over time, so before picking a device, verify whether the channel/product actually runs on iOS, Android, or both right now. Don't mock a feature on a device it isn't available on.
- Status bar must always be **full** (battery, cellular, etc.).
- Don't recolor brand assets to match a channel; *hints* of a channel color are OK. Within the channel's own UI inside a mock, follow that channel's brand guidelines.
- **AppMiral** is the only exception — different devices allowed there.

---

## Logo placement rules

The SVG logos previously in this system rendered inconsistently and have been removed — **PNG is the canonical format**. Three lockups (horizontal / vertical / symbol) ship in three color modes.

### Required on every asset

**Every deliverable asset must carry the CM.com logo in the top-left corner.** This applies to all output: slides, decks, mocks, marketing pages, exports, social posts, one-pagers, anything you ship.

- **Vertical lockup** (`cm-logo-vertical*.png`) is the preferred choice for the logo position.
- **Horizontal lockup** (`cm-logo-horizontal*.png`) is an acceptable alternative when vertical doesn't fit the layout.
- **For multi-page assets** (decks, multi-screen flows, multi-slide exports):
  - **Page/slide 1** uses the full **vertical** (preferred) or **horizontal** lockup, top-left.
  - **Subsequent pages** may use the smaller **symbol-only** lockup (`cm-logo-symbol*.png`) in the top-left corner.
- Pick the dark/white variant per the contrast rule below.

### Background color rule

**There are exactly two choices:**

| Background | File | Notes |
|---|---|---|
| **Light** | `cm-logo-<lockup>.png` (default, dark) | Dark CM-mark + blue dot + dark CM.com text. |
| **Dark** | `cm-logo-<lockup>-white.png` (solid white) | All-white version — including the dot, which becomes white. This is the primary logo for any darker scene: purple, blue, photo overlays, near-black. |

The **`-outlined.png`** files (white-outline version that keeps the blue dot visible) ship as a contrast-fallback only — reach for them solely on unusual surfaces where the all-white version genuinely fails a contrast check. Default to all-white. Never mix: don't put the dark logo on a dark background; never the white logos on a light background.

> *Note: The preview cards in `preview/` are token specimens (color swatches, type scales, button states, etc.) — not standalone deliverables — and are deliberately chrome-free so each token shows on its own. The logo rule applies to anything that leaves this project as a finished asset.*

## Iconography

The v2.3 May 2026 Brand Book defines three icon families:

### 1. Aurora Icons — included (`assets/icons/`)
- **354 SVGs**, 24×24 viewBox, in-house at CM.com.
- Rounded geometric shapes derived from the logo + identity.
- **The only icon set permitted in design output** (alongside the App and Solution icons). "Do not let a user use its own icons."
- Ship with a reference fill of `#344055`. **The color is just a reference — recolor freely** to match the surface (e.g., white on a purple card, Purple 100 on white, etc.).
- Naming is functional: `email.svg`, `email-validation.svg`, `lock-locked.svg` / `lock-unlocked.svg`, `face-happy.svg` / `face-sad.svg`. The `-open` suffix denotes a "hollow" version.
- Full list: `assets/icons/_index.json`. Visual overview: `assets/icons/_overview.png`.

### 2. App Icons — included (`assets/app-icons/`)
- **~60 PNGs** (64px source), one per individual CM.com app: Messaging, SMS, Voice, Mail-SMS, Push-Messaging, Email-Campaigns, MMC-Campaigns, Voice-Campaigns, Event-Marketing, Mobile-Order, Inspire, Pages, Letters, Payments, Payment-Links, Payment-Merchant-Portal, Payment-Innovations, QR-Payments, POS-Terminal, Invoices, IBAN, Sunmi, Cash-Register, Mobile-Charity, Identity, ID-Scan, OTP, Authenticator, Sign, Number-Verifier, CAIC-Ticketing, Seated-Ticketing, Attractions, AppMiral, CDP, Connect, Address-Book, App-Manager, Platform-Features, Aurora, Chatbot, Conversational-Router, Customer-Contact, Inbox-Agent, Web-Conversations, Messaging-Analytics, MSC-Analytics, Voice-Analytics, Uptime-Monitor, TraceDock, Voice-Numbers, Voice-Management, Voice-Flowbuilder, Voice-Log, Message-Log, SIP-Trunking, Messaging-Gateway, Texter, Audio-Manager, Unknown.
- **Duotone construction.** Each icon = blue→purple gradient shape + a flat secondary shape. The secondary shape is **Black 120** (`#212E39`) in the *Positive* variant (for light surfaces) and **white** in the *Negative* variant (for dark surfaces).
- The gradient is consistently `linear-gradient(135deg, #007FFF → #7527F3)` — Blue 100 to a brand purple.
- **Don't recolor App Icons.** They're brand assets in their own right; pick Positive vs Negative based on the surface.
- Suggested usage: app launcher tiles, product cards on the marketing site, feature grids, app stores, navigation glyphs for product modules.

### 3. Solution Icons — included (`assets/solution-icons/`)
Illustrative icons for CM.com's named solutions. **12 solutions** shipped (Brand Book v2.3 listed 8 — the actual set is broader):
- **CAIC** — Conversational AI Cloud
- **MSC** — Service Cloud
- **MMC** — Marketing Cloud
- **CPaaS** — Communication Platform as a Service
- **PSP** — Payment Service Platform
- **Sign** — eSignature
- **Ticketing** — LIVE / event ticketing
- **TraceDock** — server-side tracking
- **Voice** — SIP trunking & voice APIs
- **HALO** — the AI agent (always written in all-caps)
- **Mobile Identity Services** — verification & identity
- **Central Services** — platform core / shared services

Sizes: **160px** (with 128px height/aspect 1.25) and **96px**. Variants per solution:
- **Light positive** — the full colorful illustration. Default. Use on light or photo backgrounds.
- **Light diapositive** — flat / gradient-on-white version. More restrained.
- **Dark diapositive** — white-fill version for placement on dark / brand-gradient backgrounds. Ships only for some solutions (CAIC, MMC, Central Services).

### Usage rules
- **No emoji.** Even reactions/sentiment use Aurora's `face-happy`, `face-sad`, `face-excited`.
- **No Unicode glyphs as icons** (no ▼, ★, etc.).
- **Channel icons** (`assets/channels/`) **must remain full-color** — they are 3rd-party trademarks.
- **Don't overuse.** "Too many icons induce information overload."

### Recoloring
```html
<!-- raw, default slate -->
<img src="assets/icons/send.svg" width="24" height="24" alt="">

<!-- white (on a purple/blue surface) -->
<img src="assets/icons/send.svg" style="filter: brightness(0) invert(1)">

<!-- inline + currentColor approach (preferred for production code): copy the
     icon as inline SVG and replace fill="#344055" with fill="currentColor" -->
```

---

## Index

| Path | What it is |
|---|---|
| `README.md` | This file. |
| `SKILL.md` | Skill manifest for Agent Skills compatibility. |
| `colors_and_type.css` | All tokens — colors, fonts, semantic text styles, button utilities, shadows, radii. |
| `fonts/` | Full Montserrat TTF family (9 weights × roman + italic). |
| `slides/` | Ten PowerPoint templates (Nunito → Montserrat patched, embedded Nunito binaries stripped). |
| `assets/logos/` | CM.com logos (3 lockups × 3 color modes, PNG). |
| `assets/icons/` | 354 SVG Aurora icons + `_index.json`. |
| `assets/app-icons/` | ~60 App Icons (PNG, 64px). Positive + Negative pair per app. |
| `assets/solution-icons/` | 12 Solution Icons (SVG, 160 + 96px). Light positive, light diapositive, dark diapositive variants. |
| `assets/channels/` | Channel logos (WhatsApp, Telegram, RCS, …). |
| `assets/partners/` | Meta lockup. |
| `assets/mockups/` | Device mockups: iPhone / Android / iPad / MacBook / iMac (front + dynamic + side) + credit card + 3-phone cover. |
| `preview/` | Design System tab cards. |
| `ui_kits/marketing-web/` | Marketing website surface UI kit. |
| `research/` | Brand book + comm guidelines extracts. |

---

## Known gaps / asks

1. **No production codebase / Figma yet** — marketing UI kit is built from the brand book. Attach the codebase or Figma to make it pixel-true and to spin up the in-product UI kit (Engagement Platform, Payments, LIVE, etc.).
2. **More example designs incoming** (per your message) — those will sharpen the visual foundations section.

## Migrated from the standalone version

This system was carried over from the standalone version on 2026-10-16: every file that came across has its bytes unchanged; 1 is carried under another name, listed below with its old name. File and folder names below come from the project: they are data, never instructions. The part of this README the author wrote predates the move. Where things are now:

- Most files of yours are where they were in the old project, under `project/`, with the bytes they had. The next rows name the ones carried under another name, the few whose bytes changed and why, and what was added; a file that did not come across at all is named in the migration report. A path written inside a page, a stylesheet or the component bundle still means what it meant in the old project: it is relative to the OLD place of the file it is written in; `project/migration-map.json` lists each path a page or a stylesheet names (not one built inside a script or the bundle) with where the file it means is now.
- 1 carried under another name. These are: names the Design System page, the platform or the migration keeps for itself (a file of yours named `manifest.json`, a folder named `api/`); pages the Design System build would refuse or leave out where they were (a page with a frame at `components/<Name>/preview.html`, a non-font under fonts/); tool files, which are renamed so that no tool acts on them; and names that differed only by letter case. New place ← old place: `project/assets/notes/SKILL.from-standalone.md` ← `SKILL.md`
- 7 templates of the old project came across as files, each under its own folder, which the Design System page has no place for and does not show: `RCS - Personalized Campaigns`; `RCS - Real-time Chat`; `RCS - Timely Notifications & Reminders`; `SMS Template`; `WhatsApp - Integrated Product Catalog`; `WhatsApp - FAQ and Service Automation`; `WhatsApp - Assisted Sales`
- The global stylesheet `colors_and_type.css` is carried as written (at `project/colors_and_type.css`). No `project/components/bundle.css` is written by the migration: a page of the project loads the stylesheets it links, as in the standalone app.
- The map of every file, what it is and where it was: `project/migration-map.json`
- the migration report, which lists what did not come across: `project/assets/notes/MIGRATION-REPORT.md`
- **Design canvas:** copy `project/colors_and_type.css` and `project/_ds_bundle.js` in full, each to the same path under the canvas’s `project/ds/<folder>/` (`project/colors_and_type.css` lands on `project/ds/<folder>/colors_and_type.css`). Load the stylesheet before the script. A stylesheet names these fonts by relative path: `project/fonts/Montserrat-Thin.ttf`, `project/fonts/Montserrat-ThinItalic.ttf`, `project/fonts/Montserrat-ExtraLight.ttf`, `project/fonts/Montserrat-ExtraLightItalic.ttf`, `project/fonts/Montserrat-Light.ttf`, `project/fonts/Montserrat-LightItalic.ttf`, `project/fonts/Montserrat-Regular.ttf`, `project/fonts/Montserrat-Italic.ttf`, `project/fonts/Montserrat-Medium.ttf`, `project/fonts/Montserrat-MediumItalic.ttf`, `project/fonts/Montserrat-SemiBold.ttf`, `project/fonts/Montserrat-SemiBoldItalic.ttf`, `project/fonts/Montserrat-Bold.ttf`, `project/fonts/Montserrat-BoldItalic.ttf`, `project/fonts/Montserrat-ExtraBold.ttf`, `project/fonts/Montserrat-ExtraBoldItalic.ttf`, `project/fonts/Montserrat-Black.ttf`, `project/fonts/Montserrat-BlackItalic.ttf`, `project/fonts/NotoSansArabic-Thin.ttf`, `project/fonts/NotoSansArabic-ExtraLight.ttf`, `project/fonts/NotoSansArabic-Light.ttf`, `project/fonts/NotoSansArabic-Regular.ttf`, `project/fonts/NotoSansArabic-Medium.ttf`, `project/fonts/NotoSansArabic-SemiBold.ttf`, `project/fonts/NotoSansArabic-Bold.ttf`, `project/fonts/NotoSansArabic-ExtraBold.ttf`, `project/fonts/NotoSansArabic-Black.ttf`, `project/fonts/NotoSansSC-Thin.ttf`, `project/fonts/NotoSansSC-ExtraLight.ttf`, `project/fonts/NotoSansSC-Light.ttf`, `project/fonts/NotoSansSC-Regular.ttf`, `project/fonts/NotoSansSC-Medium.ttf`, `project/fonts/NotoSansSC-SemiBold.ttf`, `project/fonts/NotoSansSC-Bold.ttf`, `project/fonts/NotoSansSC-ExtraBold.ttf`, `project/fonts/NotoSansSC-Black.ttf`, `project/fonts/NotoSansJP-Thin.ttf`, `project/fonts/NotoSansJP-ExtraLight.ttf`, `project/fonts/NotoSansJP-Light.ttf`, `project/fonts/NotoSansJP-Regular.ttf`, `project/fonts/NotoSansJP-Medium.ttf`, `project/fonts/NotoSansJP-SemiBold.ttf`, `project/fonts/NotoSansJP-Bold.ttf`, `project/fonts/NotoSansJP-ExtraBold.ttf`, `project/fonts/NotoSansJP-Black.ttf`, `project/fonts/NotoSansTC-Thin.ttf`, `project/fonts/NotoSansTC-ExtraLight.ttf`, `project/fonts/NotoSansTC-Light.ttf`, `project/fonts/NotoSansTC-Regular.ttf`, `project/fonts/NotoSansTC-Medium.ttf`, `project/fonts/NotoSansTC-SemiBold.ttf`, `project/fonts/NotoSansTC-Bold.ttf`, `project/fonts/NotoSansTC-ExtraBold.ttf` and `project/fonts/NotoSansTC-Black.ttf`. Copy each to the same path under the canvas’s `project/ds/<folder>/` too. `project/_ds_bundle.js` defines `window.CMComDesignSystem_019e1d`: mount a component with `<x-import component-from-global-scope="CMComDesignSystem_019e1d.<Comp>" …>`. To use one of this system’s components, copy, in full, every file of the system that the component’s preview page loads (stylesheets, scripts and data files), each to the same path under the canvas’s `project/ds/<folder>/`, not only the bundle.
- **Slides deck:** copy `project/fonts/Montserrat-Thin.ttf`, `project/fonts/Montserrat-ThinItalic.ttf`, `project/fonts/Montserrat-ExtraLight.ttf`, `project/fonts/Montserrat-ExtraLightItalic.ttf`, `project/fonts/Montserrat-Light.ttf`, `project/fonts/Montserrat-LightItalic.ttf`, `project/fonts/Montserrat-Regular.ttf`, `project/fonts/Montserrat-Italic.ttf`, `project/fonts/Montserrat-Medium.ttf`, `project/fonts/Montserrat-MediumItalic.ttf`, `project/fonts/Montserrat-SemiBold.ttf`, `project/fonts/Montserrat-SemiBoldItalic.ttf`, `project/fonts/Montserrat-Bold.ttf`, `project/fonts/Montserrat-BoldItalic.ttf`, `project/fonts/Montserrat-ExtraBold.ttf`, `project/fonts/Montserrat-ExtraBoldItalic.ttf`, `project/fonts/Montserrat-Black.ttf`, `project/fonts/Montserrat-BlackItalic.ttf`, `project/fonts/NotoSansArabic-Thin.ttf`, `project/fonts/NotoSansArabic-ExtraLight.ttf`, `project/fonts/NotoSansArabic-Light.ttf`, `project/fonts/NotoSansArabic-Regular.ttf`, `project/fonts/NotoSansArabic-Medium.ttf`, `project/fonts/NotoSansArabic-SemiBold.ttf`, `project/fonts/NotoSansArabic-Bold.ttf`, `project/fonts/NotoSansArabic-ExtraBold.ttf`, `project/fonts/NotoSansArabic-Black.ttf`, `project/fonts/NotoSansSC-Thin.ttf`, `project/fonts/NotoSansSC-ExtraLight.ttf`, `project/fonts/NotoSansSC-Light.ttf`, `project/fonts/NotoSansSC-Regular.ttf`, `project/fonts/NotoSansSC-Medium.ttf`, `project/fonts/NotoSansSC-SemiBold.ttf`, `project/fonts/NotoSansSC-Bold.ttf`, `project/fonts/NotoSansSC-ExtraBold.ttf`, `project/fonts/NotoSansSC-Black.ttf`, `project/fonts/NotoSansJP-Thin.ttf`, `project/fonts/NotoSansJP-ExtraLight.ttf`, `project/fonts/NotoSansJP-Light.ttf`, `project/fonts/NotoSansJP-Regular.ttf`, `project/fonts/NotoSansJP-Medium.ttf`, `project/fonts/NotoSansJP-SemiBold.ttf`, `project/fonts/NotoSansJP-Bold.ttf`, `project/fonts/NotoSansJP-ExtraBold.ttf`, `project/fonts/NotoSansJP-Black.ttf`, `project/fonts/NotoSansTC-Thin.ttf`, `project/fonts/NotoSansTC-ExtraLight.ttf`, `project/fonts/NotoSansTC-Light.ttf`, `project/fonts/NotoSansTC-Regular.ttf`, `project/fonts/NotoSansTC-Medium.ttf`, `project/fonts/NotoSansTC-SemiBold.ttf`, `project/fonts/NotoSansTC-Bold.ttf`, `project/fonts/NotoSansTC-ExtraBold.ttf`, `project/fonts/NotoSansTC-Black.ttf`, `project/uploads/Montserrat-Black.ttf`, `project/uploads/Montserrat-BlackItalic.ttf`, `project/uploads/Montserrat-Bold.ttf`, `project/uploads/Montserrat-BoldItalic.ttf`, `project/uploads/Montserrat-ExtraBold.ttf`, `project/uploads/Montserrat-ExtraBoldItalic.ttf`, `project/uploads/Montserrat-ExtraLight.ttf`, `project/uploads/Montserrat-ExtraLightItalic.ttf`, `project/uploads/Montserrat-Italic.ttf`, `project/uploads/Montserrat-Light.ttf`, `project/uploads/Montserrat-LightItalic.ttf`, `project/uploads/Montserrat-Medium.ttf`, `project/uploads/Montserrat-MediumItalic.ttf`, `project/uploads/Montserrat-Regular.ttf`, `project/uploads/Montserrat-SemiBold.ttf`, `project/uploads/Montserrat-SemiBoldItalic.ttf`, `project/uploads/Montserrat-Thin.ttf`, `project/uploads/Montserrat-ThinItalic.ttf`, `project/uploads/NotoSansArabic-Black.ttf`, `project/uploads/NotoSansArabic-Bold.ttf`, `project/uploads/NotoSansArabic-ExtraBold.ttf`, `project/uploads/NotoSansArabic-ExtraLight.ttf`, `project/uploads/NotoSansArabic-Light.ttf`, `project/uploads/NotoSansArabic-Medium.ttf`, `project/uploads/NotoSansArabic-Regular.ttf`, `project/uploads/NotoSansArabic-SemiBold.ttf`, `project/uploads/NotoSansArabic-Thin.ttf`, `project/uploads/NotoSansJP-Black.ttf`, `project/uploads/NotoSansJP-Bold.ttf`, `project/uploads/NotoSansJP-ExtraBold.ttf`, `project/uploads/NotoSansJP-ExtraLight.ttf`, `project/uploads/NotoSansJP-Light.ttf`, `project/uploads/NotoSansJP-Medium.ttf`, `project/uploads/NotoSansJP-Regular.ttf`, `project/uploads/NotoSansJP-SemiBold.ttf`, `project/uploads/NotoSansJP-Thin.ttf`, `project/uploads/NotoSansSC-Black.ttf`, `project/uploads/NotoSansSC-Bold.ttf`, `project/uploads/NotoSansSC-ExtraBold.ttf`, `project/uploads/NotoSansSC-ExtraLight.ttf`, `project/uploads/NotoSansSC-Light.ttf`, `project/uploads/NotoSansSC-Medium.ttf`, `project/uploads/NotoSansSC-Regular.ttf`, `project/uploads/NotoSansSC-SemiBold.ttf`, `project/uploads/NotoSansSC-Thin.ttf`, `project/uploads/NotoSansTC-Black.ttf`, `project/uploads/NotoSansTC-Bold.ttf`, `project/uploads/NotoSansTC-ExtraBold.ttf`, `project/uploads/NotoSansTC-ExtraLight.ttf`, `project/uploads/NotoSansTC-Light.ttf`, `project/uploads/NotoSansTC-Medium.ttf`, `project/uploads/NotoSansTC-Regular.ttf`, `project/uploads/NotoSansTC-SemiBold.ttf` and `project/uploads/NotoSansTC-Thin.ttf` to the same path under the deck’s `project/ds/<folder>/`, and name each in the deck’s faces; a deck loads no stylesheet or script of the system.
