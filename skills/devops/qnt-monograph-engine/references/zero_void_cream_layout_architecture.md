# Zero-Void Spacing & Cream Theme Layout Architecture for PDF Compendiums

## 1. Root Cause of Spacing Voids & Pagination Drops
When compiling large multi-page monographs and 50+ page compendiums via WeasyPrint:
- Hardcoded `page-break-after: always;` / `break-after: page;` on underfilled module cards creates massive awkward white or dark voids at the bottom of pages.
- Large fixed `height: 98vh` or `height: 100vh` flex containers cause WeasyPrint to miscalculate pagination boundaries and dump half-empty pages.

## 2. The 100% Zero-Void Continuous Stream Rule
1. **Never use hard page breaks between individual modules** in encyclopedic compendiums (20–100+ modules).
2. Allow content to flow naturally and continuously using `break-inside: avoid;` strictly on small individual cards (`.module-card`) and tables.
3. Use `break-after: avoid;` on section headings (`.sec-heading`) so they bind directly to the succeeding card without leaving orphan titles.
4. Set `@page` margins to `10mm–12mm` and use compact font line-height (`1.28–1.30`) with Inter Variable font.

## 3. Luxury Cream & Pitch-Black Theme Standard (`#FAF8F5` / `#000000`)
When generating cream/white financial compendiums:
- **Canvas Background:** `#FAF8F5` (Warm Cream / Ivory Canvas).
- **Cards & Modules:** `#FFFFFF` with `1.5px solid #000000` borders.
- **Accents & Sub-boxes:** `#F4EFEA` (Soft Sand) with solid black rules.
- **Typography:** Pure pitch-black (`#000000`) with high-contrast font weights (800/900 for titles, 500/700 for text).
- **Brand Monogram:** Monumental bold black `qnt.` header.
