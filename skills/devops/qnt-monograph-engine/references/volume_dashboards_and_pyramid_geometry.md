# Volume-Specific Dashboards & Triangle Visual Layout Standards

## 1. The Pyramid Visual Truncation Pitfall & Geometric Geometry Fix

### Pitfall
When drawing multi-tier asset pyramids in SVG (e.g. 4 tiers: Tier 1 Base to Tier 4 Peak), using a standard tight triangle aspect ratio (e.g. `viewBox="0 0 700 230"`) causes the top apex tier (Tier 4) to narrow drastically into a tiny sharp triangle. Consequently, two lines of text (e.g. `TIER 4: GLOBAL TECH & SMALL-CAP ALPHA` + fund tickers) will visually collide with the top border and side slopes, creating ugly text clipping and unreadable overlap.

### The Geometric Fix
1. **Expand Height Budget:** Set `viewBox="0 0 700 310"`.
2. **Widen Apex Polygon Base:** Start Tier 4 at `polygon points="350,42 260,105 440,105"` instead of `(350,30 280,75 420,75)`. This gives the top apex a horizontal width of **180px** instead of 140px.
3. **Generous Vertical Spacing:**
   - Tier 4 Heading at `y=70` (font-size: 8pt, font-weight: 900, fill: #FFFFFF).
   - Tier 4 Subtitle at `y=88` (font-size: 6.8pt, font-weight: 600, fill: #CBD5E1).
   - Clean gap of 17px before Tier 3 begins at `y=105`.
4. **Contrast Palette:**
   - Tier 4 (Apex): `#0F172A` (Deep Slate)
   - Tier 3: `#1E293B`
   - Tier 2: `#334155`
   - Tier 1 (Base): `#475569`
   All tiers use crisp white (`#FFFFFF` / `#F1F5F9`) typography with sharp `1.5px solid #000000` boundaries.

---

## 2. Dedicated Volume-Opening Dashboards Architecture

Every major volume must feature a dedicated, bespoke vector SVG dashboard (height: ~130px, width: 100%) immediately beneath its volume header:

1. **Volume I (Postal & Small Savings):** Yield & Tax-Exemption Waterfall mapping SSY (8.2% EEE) vs SCSS (8.2% Quarterly) vs NSC (7.7%) vs KVP (7.5%) vs PPF (7.1% EEE).
2. **Volume II (Sovereign Debt & T-Bills):** RBI Yield Curve & Duration Profile (91D T-Bill at 6.75% ──► 10Y Benchmark at 7.18% ──► State SDLs at 7.55%).
3. **Volume III (Domestic Equities):** Indian Equity Market-Cap Alpha & Beta Volatility Bands (Nifty 50 vs Next 50 vs Midcap 150 vs Smallcap 250).
4. **Volume IV (Global Equities):** S&P 500 / Nasdaq 100 USD Compounding + 3.0% Annual INR Currency Depreciation Tailwind.
5. **Volume V (Real Estate & REITs):** Commercial REIT NDCF Yield (13.5% Total) vs Residential Buy-to-Let (1.2% Net Yield).
6. **Volumes VI–X:** Senior Secured Credit Recovery Waterfalls, Gold Crisis Correlation Heatmaps, MPT Efficient Frontier Curves, and HUF Tax Multiplying Structures.
