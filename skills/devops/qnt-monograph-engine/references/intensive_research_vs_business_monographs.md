# Strict Rule: Intensive Research vs. Business Wealth Framing

## 1. Context & User Directives
When Dxrk sky requests deep/intensive research dossiers (e.g. AI subscriptions, developer APIs, infrastructure tools, SaaS reviews):
- **NEVER** inject unwanted quantitative wealth business boilerplate (e.g. ₹1k/₹10k/₹1L compounding tables, SWP tax drag, Fama-French factor desks, or investment asset allocations) unless explicitly asked for wealth/financial content.
- Present pure technical, commercial, and operational intelligence.
- Attribute research to **`qnt. Research Intelligence`** without forcing the wealth platform business model onto the content.

## 2. Zero-Void Page Density vs. Hard Page Breaks
- **Root Cause of Empty Space:** Hardcoded `page-break-after: always;` paired with fixed/underfilled containers creates large empty cream/black gaps at the bottom of pages.
- **Enforce Continuous Flow:**
  - Structure all multi-page research documents with **Continuous Flow Layout**.
  - Apply `break-inside: avoid;` ONLY to small cards/tables (<120px) to prevent awkward mid-element page slicing.
  - Never place hard breaks between individual modules or platforms.
  - Allow text, tables, and specifications to fill 100% of the canvas from top margin to bottom margin.

## 3. Luxury Cream & Pitch-Black Standard Tokens
- **Background Canvas:** `#FAF8F5` (Warm Cream / Ivory).
- **Cards/Panels:** `#FFFFFF` (Crisp Warm White) with `1.5px solid #000000` (Solid Black Border).
- **Typography:** `#000000` (100% Pure Pitch Black) on Inter Variable font (`file:///data/fonts/InterVariable.ttf`) with compact line-height (`1.26–1.30`).
- **Accent Badges:** `#000000` background with `#FFFFFF` text.
