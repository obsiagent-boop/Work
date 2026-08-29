# Zero-Triangle & Executive Multi-Tier Grid Architecture

## The Problem with Triangle / Pyramid SVGs
In PDF and vector rendering, triangular polygons naturally narrow to a point at the top apex. Attempting to fit complex institutional asset titles (e.g. *"Tier 4: Global Tech & Small-Cap Alpha (10–15%)"*), underlying instrument tickers, and explanatory sub-clauses inside a narrow apex polygon inevitably causes:
1. Text clipping across polygon boundaries.
2. Crowded vertical line spacing and illegible font sizes.
3. Unavoidable user complaints regarding layout crampedness.

## The Solution: Executive Multi-Tier Institutional Allocation Grid
When displaying the 4-tier wealth architecture, eliminate triangle polygons entirely and replace them with a responsive, high-contrast horizontal tier grid:

```html
<div style="background-color: #FFFFFF; border: 1.5px solid #000000; border-radius: 2px; padding: 6px 8px; margin: 4px 0;">
  <div style="font-size: 8pt; font-weight: 900; color: #000000; text-transform: uppercase; text-align: center; margin-bottom: 4px;">
    THE qnt. 4-TIER FINANCIAL FREEDOM ASSET ALLOCATION ARCHITECTURE
  </div>
  
  <!-- Tier 4: Alpha & Global (Top Tier) -->
  <div style="background-color: #0F172A; border-left: 4px solid #000000; padding: 4.5px 7px; margin-bottom: 3px; color: #FFFFFF; border-radius: 2px;">
    <strong style="color: #FFFFFF; font-size: 7.5pt;">TIER 4: GLOBAL TECH &amp; SMALL-CAP ALPHA (10–15% Allocation)</strong><br/>
    <span style="font-size: 6.8pt; color: #CBD5E1;">• Core Engines: US S&amp;P 500 (VOO) | Nasdaq 100 (QQQ) | Nippon Small Cap | Semiconductor SMH</span><br/>
    <span style="font-size: 6.5pt; color: #94A3B8;">• Objective: Captures exponential innovation compounding, USD currency appreciation, and multi-bagger small-cap alpha.</span>
  </div>

  <!-- Tier 3: Core Growth Equities -->
  <div style="background-color: #1E293B; border-left: 4px solid #000000; padding: 4.5px 7px; margin-bottom: 3px; color: #FFFFFF; border-radius: 2px;">
    <strong style="color: #FFFFFF; font-size: 7.5pt;">TIER 3: CORE COMPOUNDING EQUITIES &amp; FACTOR ENGINES (55–60% Allocation)</strong><br/>
    <span style="font-size: 6.8pt; color: #CBD5E1;">• Core Engines: UTI Nifty 50 Index | ICICI Nifty Next 50 | Parag Parikh Flexi Cap | Nifty 200 Momentum 30</span><br/>
    <span style="font-size: 6.5pt; color: #94A3B8;">• Objective: The primary wealth multiplier compounding at 14%–18% CAGR across domestic market leaders.</span>
  </div>

  <!-- Tier 2: Real Estate & Commodities -->
  <div style="background-color: #334155; border-left: 4px solid #000000; padding: 4.5px 7px; margin-bottom: 3px; color: #FFFFFF; border-radius: 2px;">
    <strong style="color: #FFFFFF; font-size: 7.5pt;">TIER 2: REAL ESTATE CASHFLOW &amp; COMMODITY SHIELD (15–20% Allocation)</strong><br/>
    <span style="font-size: 6.8pt; color: #CBD5E1;">• Core Engines: Embassy Office Parks REIT | PowerGrid InvIT | Sovereign Gold Bonds (SGB) | Silver ETFs</span><br/>
    <span style="font-size: 6.5pt; color: #E2E8F0;">• Objective: Delivers 7.5%–11% quarterly distribution cashflow + 5,000-year geopolitical crisis protection.</span>
  </div>

  <!-- Tier 1: Sovereign Foundation (Base Tier) -->
  <div style="background-color: #475569; border-left: 4px solid #000000; padding: 4.5px 7px; color: #FFFFFF; border-radius: 2px;">
    <strong style="color: #FFFFFF; font-size: 7.5pt;">TIER 1: SOVEREIGN BEDROCK &amp; EMERGENCY MOAT (10–15% Allocation)</strong><br/>
    <span style="font-size: 6.8pt; color: #FFFFFF;">• Core Engines: Public Provident Fund (PPF) | Sukanya Samriddhi (SSY) | SCSS | RBI 10Y Gilts | 6-Month Liquid Moat</span><br/>
    <span style="font-size: 6.5pt; color: #F1F5F9;">• Objective: Impenetrable zero-default foundation with 100% Triple-E tax exemption and court attachment immunity.</span>
  </div>
</div>
```

## Universal Institutional Telemetry Integration
Every instrument module must additionally integrate the 6-dimension risk telemetry table:
- **Sharpe Ratio:** Risk-adjusted return efficiency against risk-free rate.
- **Sortino Ratio:** Downside volatility protection metric.
- **Max Historical Drawdown:** Peak-to-trough historical loss bounds during crises (2008, 2020).
- **Beta to Nifty 50:** Systemic market risk co-variance.
- **Total Expense Ratio (TER):** Cost drag benchmark.
- **Settlement Liquidity:** Redemption timeline (T+1 vs Lock-in).
