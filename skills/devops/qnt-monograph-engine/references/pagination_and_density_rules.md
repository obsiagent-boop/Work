# WeasyPrint Zero-Void Pagination & Density Rules

## 1. The Anatomy of Page Gaps in WeasyPrint
WeasyPrint calculates pagination top-down. 
1. **Hard Page Breaks (`page-break-after: always;`):** When placed on content sections that only fill a fraction of the page height, WeasyPrint immediately aborts the page, leaving the bottom as an empty black void.
2. **Oversized Containers (`break-inside: avoid;`):** If a container exceeds the remaining printable height on the page canvas, the engine pushes the entire element to the top of the next page, leaving the remainder of the current page blank.

## 2. The Continuous Stream Flow Pattern (Publication Standard)
For large-scale, gapless compendiums (such as the 200-module Master Codex):
- **Never use hard `page-break-after: always` on recurring modules.**
- Allow content to flow naturally and continuously like a published textbook or encyclopedic volume.
- Set `break-inside: avoid;` ONLY on small individual elements (sub-cards <100px, tables, citation blocks).
- Set `break-after: avoid;` on all section and volume headers to bind them to the next card.
- Result: Every page is 100% full from the top header line to the bottom footer line with zero dead space.

## 3. Quantitative Design & Typography Standards
- **Standard Letter Printable Dimensions:** 215.9mm × 279.4mm with `margin: 10mm 10mm;`.
- **Primary Typography:** Inter Variable (`file:///data/fonts/InterVariable.ttf`) via `@font-face`.
- **Sub-card Height Budget:** Keep cards ≤90px each (including padding and margin).
- **SVG Canvas Budget:** Set `viewBox="0 0 700 85"` with `height: auto; margin: 3px 0;`.
- **Background & Card Colors:** Canvas `#000000`, Cards `#060913`, Border `#1E293B`, Accents `#06B6D4` / `#10B981`.

## 4. Brand Protection Rules
- Never include social media handles (`@...`) or scraper references.
- Attribute all research to **`qnt. Quantitative Wealth Systems`**.
- Embed official logo: `file:///data/project_qnt/assets/qnt_logo.jpg`.
