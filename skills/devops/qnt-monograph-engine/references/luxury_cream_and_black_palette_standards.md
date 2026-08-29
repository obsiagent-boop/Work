# Luxury Cream & Black Palette Standard for qnt. Publications

## Core Visual Palette & CSS Tokens
* **Page Canvas Background:** `#FAF8F5` (Warm Luxury Cream / Ivory)
* **Card & Panel Background:** `#FFFFFF` (Crisp Pure White)
* **Borders & Rules:** `1.5px solid #000000` (Solid Pitch-Black Obsidian Rules)
* **Primary Typography:** `#000000` / `#0A0A0A` (Deep Pitch-Black, 100% Contrast)
* **Secondary / Header Accent Background:** `#F4EFEA` (Soft Sand)
* **Table Headers:** `background-color: #000000; color: #FFFFFF; font-weight: 800;`
* **Table Alternating Rows:** Even rows `#FAF8F5`, Odd rows `#FFFFFF`, borders `1px solid #000000`

## Continuous Flow & Zero Spacing Voids
1. **Never use artificial height containers or forced `page-break-after: always;` on multi-page continuous monographs.** Hard breaks with underfilled content create massive empty gaps at the bottom of pages.
2. Allow content to flow naturally and continuously using `break-inside: avoid;` exclusively on individual cards and tables under 100px.
3. Keep line-height tightly bounded to `1.28–1.30` with Inter Variable typography (`file:///data/fonts/InterVariable.ttf`) to maintain dense, institutional readability.
