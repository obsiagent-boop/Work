---
name: qnt-monograph-engine
description: "Use when creating qnt. PDFs. Generates zero-void monographs."
platforms: [linux, macos, windows]
---

# qnt. Monograph & Quantitative PDF Engine

## Trigger
Use this skill whenever asked to generate a `qnt.` branded PDF monograph, quant dossier, multi-page investment encyclopedia, or when the user requires large-scale (e.g. 15–20+ pages) research PDFs with zero page voids.

## Core Rules & Execution Architecture

### 1. Brand Identity & Source Intelligence Shield
- **Strictly scrub social media provenance:** Never include Instagram `@` handles, reel links, or scraper mechanics in the output PDF.
- **Brand Attribution:** Attribute all research exclusively to **`qnt. Quantitative Wealth Systems`** supported by statutory and institutional citations (Ministry of Finance, RBI, SEBI, US SEC, AMFI, SPIVA).
- **Official Brand Logo:** Embed `/data/project_qnt/assets/qnt_logo.jpg` at the top of the cover and headers.

### 2. Zero-Void & Continuous Stream Layout Principles
- **Root Cause of Empty Lower Voids:** Hardcoded `page-break-after: always;` paired with underfilled content blocks or oversized `break-inside: avoid;` cards (>200px) causes WeasyPrint to abort the page early, leaving huge black empty spaces at the bottom.
- **The Continuous Flow Rule (Default for Large Monographs):**
  1. For large encyclopedic publications (80–200+ modules), **DO NOT use hard page breaks (`page-break-after: always`) between individual modules**.
  2. Allow content to flow naturally and continuously from top to bottom across pages.
  3. Apply `break-inside: avoid;` ONLY to small individual cards and tables (under 100px) so they never slice awkwardly across pages.
  4. Use `break-after: avoid;` on section headers and volume titles to bind them to the succeeding card.
  5. The result is 100% full utilization of every single page canvas from the top header line to the bottom footer with zero voids.
- **The Exact Fixed-Page Budget Rule (When Explicit Page Counts are Requested):**
  1. When an exact discrete page count is requested (e.g. exactly 20 pages), every single page container must be given an exact height budget and sufficient dense content (~3,000 chars + tables + citations) to completely fill the canvas before triggering the break.
  2. Use the **Inter Variable font** (`file:///data/fonts/InterVariable.ttf`) loaded via `@font-face` with compact line-height (`1.28–1.32`).
  3. Keep vector SVG canvas heights to ≤90px–95px with viewBox responsive scaling.
  4. Adhere strictly to `/data/project_qnt/DESIGN.md` tokens (`#000000` canvas, `#060913` cards, `#06B6D4` cyan, `#10B981` emerald).

### 3. Visual Themes & Cognitive Standards
- **Luxury Cream & Black Edition (Mandatory Default when Cream Requested):**
  - Follow [`references/luxury_cream_and_black_palette_standards.md`](references/luxury_cream_and_black_palette_standards.md).
  - Background Canvas: Warm Luxury Cream / Ivory (`#FAF8F5`).
  - Cards: Crisp White (`#FFFFFF`) with solid black borders (`1.5px solid #000000`).
  - Typography: 100% Pure Pitch-Black (`#000000`) with Inter Variable font (`line-height: 1.28–1.30`).
  - Accent / Sub-boxes: Soft Sand (`#F4EFEA`).
  - Tables: Pitch-black header (`#000000` background, `#FFFFFF` bold text), alternating `#FAF8F5` and `#FFFFFF` row fills.
  - Zero Page Voids: Continuous flow layout without hard breaks (`break-inside: avoid` on cards only).
- **Alternative Theme (Cyber Void):** Solid pitch-black `#000000` canvas, `#060913` cards, Electric Cyan (`#06B6D4`, `#38BDF8`) & Emerald (`#34D399`) accents.
- **5-Year-Old Analogies:** Plain-language intuition paired with rigorous mathematical proofs.
- **Embedded SVG Diagrams:** Vector flowcharts, asset allocation wheels, and growth curves.
- **Actionable Direct-Access Encodings:** Every single financial vehicle, fund, or sovereign asset MUST contain:
  1. An explicit **`🌐 OFFICIAL ACCESS PORTAL`** with direct clickable web URL (e.g. `https://ebanking.indiapost.gov.in`, `https://rbiretaildirect.org.in`, `https://enps.nps-proteantech.in`, `https://app.mfcentral.com`, `https://amc.ppfas.com`).
  2. A concrete **`🚀 EXACT ONBOARDING PROCEDURE`** detailing KYC prerequisites, minimum ticket size, Demat ticker symbol, and deposit instructions so any reader can execute immediately without ambiguity.
  3. A dedicated **`REAL-TIME MONEY COMPOUNDING TRAJECTORY (5Y, 10Y, 15Y)`** table showing exact projected corpus values for ₹1,000, ₹10,000, and ₹1,00,000 (see `references/bespoke_fund_growth_standards.md`).
  4. An explicit **`⚠️ CRITICAL RISKS, LOCK-IN & FAILURE MODES`** warning box for every instrument.
  5. A dedicated **`🏛️ LIVE STATUTORY VERIFICATION & PUBLIC TRUST CITATION`** box containing exact parent Acts, Government Gazette Notifications (e.g. G.S.R. numbers), RBI Master Directions, SEBI Regulation clauses, or US SEC filings to ensure unassailable public trust and verifiable authenticity.
  6. **Mandatory Front-Matter Legal & Statutory Disclaimer (Standalone Page 1):** Every publication must lead with an explicit Front-Matter page containing the Impersonal Educational Publishing Exemption (Lowe v. SEC / SEBI Investment Advisers Regulations 2013), statutory market risk disclaimers, and deterministic mathematical compounding notices. The disclaimer page MUST enforce a strict page break (`break-after: page;`) so the main title and vector dashboards begin cleanly on Page 2 without awkward mid-page overlap.
  7. **High-Density Vector Visual Dashboards:** Publications must embed scalable SVG visual analytics (Wealth Pyramids, 20-Year Compounding Curves, Asset Correlation & Diversification Matrices, and 70:15:15 Allocation Wheels) before fund breakdown sections.
  8. **Three Analytical Possibility Dimensions for Every Instrument:** Every single fund or asset module must feature three distinct analytical sections:
     - `🚀 ANALYTICAL POSSIBILITIES: WEALTH CREATION & MULTIPLIER UPSIDE` (compounding mechanics, beating inflation, alpha acceleration).
     - `📉 ANALYTICAL POSSIBILITIES: CAPITAL DEPRECIATION & INFLATION DRAG` (real purchasing power loss, cash drag, interest rate cycles, illiquidity risks).
     - `💡 HIGH-CONVICTION DIRECT ASSET / STOCK RECOMMENDATIONS` (direct-growth plans, sovereign tranches, low-cost exchange tickers e.g. VOO, QQQ, MOMENTUM, GOLDBEES, EMBASSY, PGINVIT with TER < 0.30%).
  9. **Master Executive Indexing & Advanced Institutional Cashflow Methodologies:**
     - Publications must include an upfront Master Executive Index (Page 2) outlining all sections and volumes with their strategic objectives.
     - Must embed 10 advanced institutional wealth methodologies tailored for Indian investors:
       1. SWP vs Dividend Tax Drag Mechanics (4x higher post-tax cashflow via ₹1.25L Section 112A LTCG exemptions).
       2. Loan Against Securities (LAS) / Bank Overdraft 'Buy-Borrow-Die' Systems (9.0%–9.75% revolving credit lines bypassing capital gains events).
       3. The 3-Bucket Retirement Cashflow Waterfall (0–3Y Liquid, 4–7Y Refill Engine, 8+Y Equities).
       4. Sovereign Postal + Equity SWP Monthly Paycheck Synthesis.
       5. Systematic Transfer Plan (STP) Value Averaging During Market Euphoria.
       6. Hindu Undivided Family (HUF) Entity Tax Multiplication (doubling annual 80C & basic exemption slabs).
       7. Covered Call Option Overlay on Demat Large-Cap Portfolios (harvesting 8%–12% annual option premium yield).
       8. Arbitrage Fund Cash Moat vs Bank Fixed Deposits (7.2%–7.8% yield with equity tax status).
       9. Sovereign Gold Bond (SGB) Secondary Market Discount Capture (3%–5% immediate spot gold discount).
       10. GIFT City IFSC Direct Global Dollar Wealth Accumulation (bypassing domestic banking remittance delays).
     (See `references/global_standards_and_institutional_telemetry.md` and `references/advanced_cashflow_methodologies_and_indexing.md`).
  10. **Universal Institutional Risk Telemetry & Metrics Table:**
     - Every single module across all volumes must feature an institutional metrics matrix: Sharpe Ratio (Risk-Adjusted Alpha), Sortino Ratio (Downside Protection), Max Historical Drawdown Bounds, Beta to Nifty 50 Index, Total Expense Ratio (TER Benchmark), and Settlement Liquidity Horizon.
  11. **Volume-Level Visual Dashboards & Prohibition of Triangle Overlaps:**
     - Every Volume opening must feature a dedicated vector visual dashboard tailored to its asset class (Postal Yield Spectrums, G-Sec Yield Curves, Equity Alpha Bands, USD FX Math, REIT vs Residential Rent Comps).
     - **Pyramid / Triangle Prohibition Rule:** Never attempt to force multi-line text descriptions into narrow triangular apex polygons. When the user requests removing triangles or when presenting multi-tier wealth structures, REPLACE the triangle SVG completely with an **Executive Multi-Tier Institutional Allocation Grid** built of responsive rectangular cards with high-contrast slate/white typography. (See `references/comprehensive_volume_dashboards_and_methodologies.md` and `references/zero_triangle_and_tier_grid_architecture.md`).
  12. Absolute prohibition of repetitive generic boilerplate sentences or identical 4-point checklists across modules. All research must be structured as enterprise-grade investigations by `qnt. Quantitative Wealth Systems`. (See `references/analytical_possibilities_and_stock_recommendations.md`).
  13. **Artistic UI Application Pipelines & Real-Time Profit Realization Schedulers:**
     - Every single module across all 200 instruments must incorporate an artistic 5-step visual UI application pipeline card (Step 1 Access, Step 2 KYC, Step 3 Money Allocation [₹1k/₹10k/₹1L], Step 4 Standing Mandate Execution, Step 5 Payout Harvesting).
     - Every module must feature a dedicated green **`💰 REAL-TIME PROFIT REALIZATION & PAYOUT SCHEDULE`** box detailing exact payout frequency (Monthly, Quarterly, Annual EEE, SWP), bank/Demat routing, and tax-exempt extraction thresholds. (See `references/artistic_ui_pipelines_and_profit_realization.md`).
  14. **Intuitive Financial Glossary & Growing Wealth Possibility Boxes:**
     - Every publication must feature a dedicated Plain-English Financial Glossary (Page 3) demystifying CAGR, Sharpe, Sortino, Beta, Max Drawdown, SWP, and LAS into accessible 5-year-old intuitive analogies.
     - Every single module across all 200 instruments must incorporate an explicit blue **`🌟 IF YOU INVEST ₹1,00,000 / ₹10,000 / ₹1,00,000 GROWING WEALTH POSSIBILITY`** box that clearly explains the tangible multi-year wealth transformation for small, medium, and large capital allocations. (See `references/intuitive_glossary_and_growing_possibilities.md`).
  15. **100% Bespoke Domain Analytics & Elimination of Repetitive Section Boilerplate:**
     - Absolutely prohibit using copy-paste boilerplate sentences across modules in Upside, Downside, and Recommendation boxes. Every single fund must receive customized, asset-specific mathematical explanations, realistic downside risks (e.g. lock-in traps, tax drags, drawdown percentages), and actionable fund/ticker names with exact timing rules (e.g. PPF April 1–5 deposit window, SSY monthly 1st standing order). (See `references/bespoke_domain_analytics_and_zero_boilerplate.md`).
  16. **In-Situ Contextual Financial Jargon Decoders (Immediate On-Page Definitions):**
     - In addition to the master glossary, every single module and volume MUST feature a dedicated purple in-situ jargon decoder (`💡 CONTEXTUAL FINANCIAL JARGON DECODER`) that defines all technical financial terms (CAGR, EEE, Court Attachment Immunity, Section 10(11A), TER, LTCG, NDCF, Beta, Sharpe, Sortino, Drawdown, LRS, SWP, LAS) used on that exact page, ensuring any reader without financial background can understand the material immediately. (See `references/insitu_jargon_decoders_and_educational_architecture.md`).
  17. **Fincept Terminal 6-Desk Institutional Global Matrix Integration:**
     - Structure multi-asset research following Fincept Terminal's institutional architecture: Desk I Equities & Factor Engines (13.2%–24% CAGR), Desk II F&O Derivative Harvesting & Covered Calls (8%–14% Premium), Desk III Sovereign Fixed Income (7.1%–8.2% EEE), Desk IV Commercial REITs & Infrastructure (7.5%–11.5% NDCF), Desk V Commodities & Crisis Moats (SGB 10.5% + 2.5%), and Desk VI Global USD Cross-Border (15.2%–18.5% INR CAGR). (See `references/fincept_terminal_institutional_architecture.md`).
  18. **Legal Insulation, Trademark & Impersonal Publishing Exemption:**
     - Maintain strict compliance under *Lowe v. SEC (1985)* and *SEBI (Investment Advisers) Regulations, 2013*. Protect the `qnt.` brand via Class 16, 41, and 9 trademarks and Wyoming LLC privacy structures. (See `references/legal_infrastructure_and_brand_protection.md`).
  19. **Dynamic Page-Annotated Executive Index Table:**
     - Master Index (Page 2) must include a 4-column directory table utilizing WeasyPrint's GCPM `target-counter(attr(href), page)` to automatically resolve and display the exact compiled page numbers for every section and volume with clickable internal links. (See `references/dynamic_page_annotations_and_index_architecture.md`).
  20. **Fincept Terminal 5-Lab Deep Quantitative Analytical Architecture:**
     - Publications must embed the 5 Fincept Quantitative Labs: Lab 1 Multi-Factor Alpha & Fama-French 5-Factor Modeling, Lab 2 Options Greeks & Theta Harvesting Physics, Lab 3 DCF, Reverse DCF & ROIC Moats, Lab 4 Macroeconomic Regimes & Sovereign Yield Curves, and Lab 5 Modern Portfolio Theory & Efficient Frontier Optimization. (See `references/fincept_deep_quant_labs_and_analytical_models.md`).
  21. **The 12-Book Cognitive Architecture & Mental Models:**
     - Ingests and enforces the 12 master texts across all research deliverables: 1) Taleb Antifragile Barbell, 2) Marks Second-Level Cycles, 3) Munger Inversion Checklists, 4) Damodaran DCF & ROIC, 5) López de Prado Dynamic Barriers, 6) Ernie Chan Cointegration Spreads, 7) John Hull Theta Greeks, 8) Ed Thorp Kelly Criterion, 9) Donella Meadows Stocks & Flows, 10) Ray Dalio All-Weather Machine, 11) Alex Hormozi Value Equation, and 12) Eliyahu Goldratt Theory of Constraints. (See `references/twelve_book_cognitive_architecture.md`).
  22. **In-Situ Deep Explanations of Cognitive Models & Guaranteed Index Resolution:**
     - Every single module MUST embed a dedicated `🧠 12-BOOK COGNITIVE MENTAL MODEL MATRIX` box that explains *who the authors are* (e.g. Eliyahu Goldratt author of The Goal, Nassim Taleb author of Antifragile, Charlie Munger, Donella Meadows) and *what the concept means in plain English* as applied to that specific instrument.
     - The Master Executive Index MUST ensure all 10 volumes have explicit HTML anchor IDs (`vol-1` to `vol-10`) so WeasyPrint's GCPM `target-counter(attr(href), page)` never renders blank page numbers. (See `references/insitu_cognitive_definitions_and_full_volume_index.md`).
 23. **Institutional 4-Tier Ratings & Quick-Nav Asset Selector Architecture:**
 - Every single module across all 200 instruments must lead with a dedicated Institutional Tier Rating Badge:
   • TIER 1: Sovereign Bedrock & Court-Immune Vault (Rating: AAA ★★★★★ | Conviction: 99/100 | Target: Risk-averse savers & guaranteed income).
   • TIER 2: Defensive Cashflow & Real Asset Moat (Rating: AA+ ★★★★☆ | Conviction: 93/100 | Target: Salaried professionals & stock landlords).
   • TIER 3: Core Wealth Multiplier & Factor Compounding (Rating: A+ ★★★★★ | Conviction: 96/100 | Target: FIRE number & 15Y wealth builders).
   • TIER 4: Convex Alpha & Global Innovation Multiplier (Rating: A ★★★★☆ | Conviction: 90/100 | Target: Aggressive accumulators & USD fortunes).
 - Upfront Quick-Nav Executive Asset Selector (Page 3): A structured decision matrix matching investor life-stages to exact fund tiers for instant navigation without cognitive fatigue. (See `references/institutional_ratings_and_quick_nav_selector.md`).
 24. **Dedicated Artistic Tier Class & Capabilities Architecture:**
    - Every module must feature an isolated, styled **`🏛️ TIER CLASSIFICATION & STRATEGIC CAPABILITIES`** block containing:
      • Dedicated Pill Badges & Theme Colors (Tier 1 Emerald, Tier 2 Blue, Tier 3 Orange, Tier 4 Amber).
      • Explicit 3-metric header (Institutional Credit Rating, Conviction Score /100, Default/Distribution/CAGR Yield).
      • Explicit **`🛡️ CORE STRATEGIC CAPABILITIES`** section detailing Legal Immunity, Tax Status, Volatility Armor, and Target Portfolio Weighting (e.g. 10%–15% Bedrock, 55%–60% Core Alpha). (See `references/artistic_tier_class_and_capabilities_cards.md`).
 25. **Deep Quantitative Research, 5Y Track Records, Mathematical Upside Projections & Ruin Probing:**
    - **Quantitative Overview & Core Profile:** Must include verified 5-Year Historical Track Records (e.g. FY20–FY26 annual/rolling CAGR) and an explicit "Must-Know Investor Terms" checklist.
    - **Real-Time Profit Realization Payout Schedule:** Must detail historical 5-year distribution track records, exact bank credit mechanisms (ECS/NEFT/T+1), and tax-harvesting strategies.
    - **Wealth Creation & Multiplier Upside:** Must provide rigorous step-by-step mathematical compounding proofs ($A = P(1+r)^t$), exact terminal corpus projections for ₹1k, ₹10k, ₹1L, and structural economic catalysts (monopoly pricing power, GDP formalization, USD FX depreciation boost).
    - **Capital Depreciation & Inflation Drag Probing:** Must probe the exact worst-case failure modes, purchasing power erosion under 6.5% CPI inflation, liquidity lock-in traps, interest rate hike cycles, and tax slab drag.
    - **Expanded Risk Telemetry & Practical Protocols:** Telemetry tables must incorporate **Value at Risk (VaR 99% 1-Day)** alongside Sharpe, Sortino, Max Drawdown, Beta, TER, and a concrete **Practical Risk Management Protocol** for every instrument. (See `references/deep_quantitative_overview_and_risk_telemetry.md`).
 26. **100% 1:1 Synchronized In-Situ Jargon Decoders & 4-Pillar Actionable Risk Protocols:**
    - **100% 1:1 Jargon Synchronization Rule:** Every single financial term listed in the "Essential Investor Terminologies" under the Quantitative Overview MUST be explicitly and exhaustively defined inside that module's purple `💡 CONTEXTUAL FINANCIAL JARGON DECODER` box. Zero terms may appear in the overview without a corresponding in-situ plain-English definition on that exact page.
    - **4-Pillar Actionable Institutional Risk Management Protocol:** The Risk Telemetry section must conclude with a structured, 4-step risk execution guide tailored to that asset class: (1) Portfolio Allocation Limit / Boundary, (2) Timing, Strike & Cashflow Execution Rest, (3) Inflation / Drawdown Buffer Integration, (4) Liquidity Defense & Compliance Shield (e.g. Schedule FA, Form 15H, ₹1.25L LTCG harvesting). (See `references/synchronized_jargon_and_risk_protocols.md`).
 27. **Authoritative Publication Tone & Total Elimination of Prompt Meta-Commentary:**
    - **Pure Institutional Publishing Voice:** Completely eliminate artificial meta-commentary, self-referential phrases (e.g. '100% bespoke', 'as per prompt', 'as requested'), and prompt artifacts from section titles and text bodies.
    - **Natural Executive Headers:** Re-engineer section headers into natural, dignified publication titles:
      • `ASSET ARCHITECTURE & STRATEGIC ALLOCATION CAPABILITIES`
      • `QUANTITATIVE SPECIFICATION, 5-YEAR TRACK RECORD & STRUCTURAL MECHANICS`
      • `FOUNDATIONAL CONCEPTS & TERMINOLOGY DECODER`
      • `COGNITIVE DECISION FRAMEWORKS & MENTAL MODELS`
      • `DETERMINISTIC COMPOUNDING TRAJECTORY: ₹1,00,000 | ₹10,000 | ₹1,00,000`
      • `OPERATIONAL EXECUTION & ONBOARDING WORKFLOW`
      • `CASHFLOW HARVESTING, HISTORICAL PAYOUTS & TAXATION ARCHITECTURE`
      • `QUANTITATIVE TELEMETRY, RISK PROFILES & INSTITUTIONAL PROTOCOLS`
      • `STRUCTURAL GROWTH CATALYSTS & ASYMMETRIC UPSIDE MECHANISMS`
      • `CAPITAL DEPRECIATION, MACRO REGIMES & STRESS-TEST PROBING`
      • `DIRECT INSTRUMENT SELECTION & STATUTORY REGULATORY VERIFICATION`
      (See `references/authoritative_publication_voice_and_section_architecture.md`).
 28. **3D WebGL Web Platform & Luxury Light UI Architecture:**
    - Pure `qnt.` branding (zero distracting badges or boxes in header).
    - 3-lines slide-out hamburger navigation drawer on upper left.
    - High-contrast luxury white/cream foundation (`#FAF8F5` / `#FFFFFF`) with pitch-black (`#000000`) text across all toggles and buttons.
    - Real-time 3D Golden Metallic Dollar (`$`) WebGL scene with Three.js.
    - Interactive 200-Module SQL Quantitative Database table with live instant search.
    - Expandable sub-drawers across all 6 Factor Desks.
    (See `references/qnt_3d_webgl_saas_platform_standards.md`).
 - **Strict Git & Deployment Identity:** All generated compendiums, SaaS platforms, and repositories must be committed, tagged, and deployed exclusively under **`obsiagent-boop`** (`obsi.agent@gmail.com`) with zero legacy account traces.
 - **AI Agent Monetization Codex Standards:** See [`references/ai_agent_monetization_codex_standards.md`](references/ai_agent_monetization_codex_standards.md) for the 5-Axis 2026 Sovereign AI Monetization Framework (Outcome-Based, Hybrid Retainers, Autonomous Arbitrage, Ghost Fulfillment, Enterprise Licensing) and zero-void 20-page compendium standards.
 - **Dedicated 2026 AI Agent Monetization & Cashflow Dimensions:** When generating AI agent codexes, encyclopedias, and directories, strictly abort legacy asset metrics and anchor every single agent entry to the **5 Sovereign AI Agent Monetization Axes** (Outcome-based, Hybrid Retainers, Autonomous Arbitrage, Ghost Fulfillment, Enterprise Licensing) with net cashflow velocity as the terminating metric. (See `references/ai_agent_monetization_framework_2026.md`).
 - **DOT3 Note Model Architecture & Self-Learning State Ledger:** See [`references/dot3_note_model_architecture.md`](references/dot3_note_model_architecture.md) for Tempo multi-step checkpointing, dynamic `memory.mmd` state tracking, and autonomous self-correction workflows.
 - **Generative Video & No-Slop Synthesis Standards:** See [`references/generative_video_no_slop_standards.md`](references/generative_video_no_slop_standards.md) for Google Gemini 4K image diffusion, regional multilingual TTS, high-performance FFmpeg concat, and burned-in subtitle standards.
 - **Subtitles Preference & Pure Visual Directives:** In video generation, subtitles must either be small, crisp, and high-contrast (`FontSize=10-12` in a compact bottom pill) or completely omitted when pure cinematic visuals and broadcast-quality voiceovers (e.g. regional TV news presenter profiles) are requested.
 - **100% In-Situ Jargon Terminology Mirroring:**
    - Every technical term presented in the Quantitative Overview checklist MUST be mapped with an explicit, plain-English entry in the module's Terminology Decoder box. Zero terms may appear in the profile without an immediate on-page explanation.
- **Pure Research Intelligence Dossiers vs Institutional Wealth Compendiums:**
    - See [`references/pure_research_vs_wealth_monographs.md`](references/pure_research_vs_wealth_monographs.md) and [`references/intensive_research_vs_business_monographs.md`](references/intensive_research_vs_business_monographs.md). When tasked with pure technology, software, model, or subscription research conducted by `qnt. Research Intelligence`, strictly exclude internal wealth-compounding frameworks (₹1k/₹10k/₹1L tables, Fincept labs, investment legal safe-harbors) and focus 100% on technical specifications, subscription tiers ($10–$100), per-unit API pricing, hardware quotas, and verified international payment options on the Luxury Cream canvas with continuous-flow zero page voids.
- **Zero-Void Spacing & Cream Theme Layout Architecture:** See [`references/zero_void_cream_layout_architecture.md`](references/zero_void_cream_layout_architecture.md) for strict elimination of page voids in large 50+ page compendiums using continuous stream layout, compact line-heights, and the Luxury Cream (`#FAF8F5`) / Pure Pitch-Black (`#000000`) theme standard.
- **Continuous Dense Research & Editorial Flow:** See [`references/continuous_dense_research_standards.md`](references/continuous_dense_research_standards.md) for structuring intensive technical and operations research into continuous prose with structural summary tables rather than rigid card grids.
- **Project Skills & Career Transformation Standards:** See [`references/project_skills_career_transformation_standards.md`](references/project_skills_career_transformation_standards.md) for 50+ page zero-void enterprise upskilling monographs, practical sandbox setups (ServiceNow PDI, SAP Learning Hub, Microsoft Learn, HubSpot Academy), continuous typographical density, and dedicated master end-bibliographies.
- **Global Business & Monetization Research Standards:** See [`references/global_business_and_monetization_standards.md`](references/global_business_and_monetization_standards.md) for 50+ page Canadian & global business opportunity blueprints, incorporation & tax tiers ($100 to $100k+ CAD), C11/ICT visa governance, and centralized master regulatory bibliographies.
- **Fresh Domain Isolation & 100+ Page Research Standards:** See [`references/fresh_domain_isolation_and_100page_standards.md`](references/fresh_domain_isolation_and_100page_standards.md) for complete context purging between distinct domain investigations, strict zero-cross-pollination, 100+ page continuous zero-void density scaling, and mandatory centralized end-bibliographies.
- **Visual Dashboards & Regulated Industry Standards:** See [`references/visual_dashboards_and_regulated_licensing_standards.md`](references/visual_dashboards_and_regulated_licensing_standards.md) for 4-metric visual KPI dashboard widgets, provincial dispensary licensing blueprints (e.g. Ontario AGCO CROL/RSA, CannSell, OCS wholesale), and U of T / PGWP OINP Masters graduate business incorporation pathways.
- **Visual Analytics Dashboards & Partition Table Telemetry:** See [`references/visual_analytics_dashboards_and_partition_telemetry.md`](references/visual_analytics_dashboards_and_partition_telemetry.md) for dual-chart SVG visual dashboard panels (12-month revenue curves + expense distribution stacked bars), embedded capital/visa telemetry sub-rows in economic tables, granular 5-step regulatory onboarding sequences, and zero-void continuous flow standards.
- **Executive Research Methodology & Capital-Sorted Hierarchy Standards:** See [`references/executive_methodology_and_capital_hierarchy_standards.md`](references/executive_methodology_and_capital_hierarchy_standards.md) for mandatory executive research methodology & source attribution pages (Pages 1–3), strict low-to-high capital sorting ($0–$100 CAD to $150,000+ CAD), dual-chart visual analytics panels, and 100+ page continuous-flow zero-void publications.
- **Regional University Hubs & Strict Capital Hierarchy Standards:** See [`references/regional_university_hubs_and_capital_hierarchy.md`](references/regional_university_hubs_and_capital_hierarchy.md) for dedicated University of Toronto & University of Windsor cross-border commercial hubs, OINP Non-GTA regional scoring advantages, and strictly sorted capital progression ($0–$100 to $150k+ CAD).
- **Apify Scraping, Resume Matching & Supabase Pipelines:** See [`references/apify_resume_scraping_and_supabase_pipeline.md`](references/apify_resume_scraping_and_supabase_pipeline.md) for Apify LinkedIn scraper actor runs, candidate resume relevance scoring, time-filtered job ingestion (past 24-48h), and Supabase cloud synchronization.
- **Zero-Data-Loss Resume Template Mapping & Formatting:** See [`references/resume_template_transfer_standards.md`](references/resume_template_transfer_standards.md) for complete candidate career history transfer into standard 1-page ATS templates (.docx and .pdf), borderless table alignments, and strict zero-information-loss protocols.
- **Precise Career Title Customization & Micro-Edits:** See [`references/precise_resume_customization_and_micro_edits.md`](references/precise_resume_customization_and_micro_edits.md) for targeted header and role title modifications, bullet preservation, 1-page budget invariance, and dual DOCX/PDF parity.



### 4. Verification & Delivery Pipeline
1. Compile HTML to PDF via WeasyPrint.
2. Verify exact page count with `pymupdf` (`len(doc)`).
3. Inspect rendered page PNGs with `vision_analyze` to confirm zero voids.
4. Convert to AST Markdown using `/data/bin/anydoc`.
5. Upload to Notion via `file_uploads` API.
6. Commit & push to GitHub under `obsiagent-boop` (`personal-agent-os` and `project-anya`).
7. Deliver via `MEDIA:/data/project_qnt/reports/...`.
