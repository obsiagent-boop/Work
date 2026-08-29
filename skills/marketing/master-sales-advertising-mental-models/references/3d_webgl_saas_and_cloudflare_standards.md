# qnt. 3D WebGL SaaS Architecture, High-Contrast UI & Live Database Standards

## 🏛️ 1. Core Brand Identity & Header Rules
- **Brand Logo:** Must be rendered as pure, undisturbed typography (`qnt.`) using luxury geometric brand weights (e.g. *Syne* or *Plus Jakarta Sans* font).
- **Prohibition of Redundant Badges:** Never add distracting decorative boxes (like a separate 'Q' box) or subtitles (like '3D Sovereign') beside the primary `qnt.` header logo.
- **Top-Left Slide-Out Header Drawer (3-Line Hamburger):**
  - Must use **3 solid black high-contrast horizontal lines** (`w-6 h-0.5 bg-black`) contained within a defined bordered button (`border-2 border-black`).
  - Opens a dedicated slide-out navigation drawer with quick links to all calculators, databases, research grants, and agency portals.

## 💵 2. 3D WebGL Real-Time Finance Visuals (Three.js Standards)
- **Real-Time Financial Asset:** The 3D scene must represent real-world finance/wealth symbols — specifically a **real-time rotating 3D Golden Metallic `$` (Dollar) sculpture** with specular lighting, metallic reflections, and an electric cyan orbital wireframe halo.
- **Canvas Base:** WebGL canvas runs asynchronously in the background (`position: fixed; top: 0; left: 0; z-index: 0; pointer-events: none;`) reacting smoothly to user mouse/touch inertia without blocking UI clicks.

## 🎨 3. Luxury White / Cream High-Contrast UI Rules
- **Background Foundation:** Pristine Luxury Cream / Light Canvas (`#FAF8F5` / `#FFFFFF`).
- **Typography Contrast:** All text, headings, and toggles must enforce **solid pitch-black (`#000000` / `#060811`) typography**.
- **Button Contrast:**
  - Active buttons/toggles must use solid black fill (`bg-black text-white`) with defined borders (`border-2 border-black`).
  - Inactive buttons must use solid white fill with bold black text (`bg-white text-black border-2 border-black`).
  - Never allow faint grey text on grey backgrounds or washed-out white text on light canvases.

## 🗄️ 4. 200-Module Live Quantitative Database Engine
- **Live Instant Search:** Incorporate an instant in-memory JavaScript/SQL search bar filtering by name, asset category, or statutory legal protection.
- **High-Contrast Table Layout:** Display ID, Asset Name, Tier Badge, 5-Year Rolling CAGR, and Statutory Tax Protections (e.g. *Section 14 Court Attachment Immunity, Section 47(viic) 0% Capital Gains*).
- **Interactive Action Links:** Direct execution portal buttons on every row.

## 🏛️ 5. Expandable Sub-Functionalities on All 6 Factor Desks
- Every Factor Desk card must be interactive and clickable.
- Clicking any desk card expands a dedicated **Sub-Drawer** revealing:
  1. *Exact Portfolio Allocation Holdings* (e.g. 40% Large Cap / 30% Mid Cap / 30% Small Cap).
  2. *Risk & Factor Telemetry* (Fama-French Alpha spread, 99% Value at Risk bounds).
  3. *Statutory Tax Exemption Laws & Cashflow Sweep Rules*.

## 🔬 6. Open Research Grants & Collaborator Network
- Dedicated collaboration section featuring:
  - **Factor Alpha Research Grants ($500–$2,000 bounties)** for mathematicians and quant developers.
  - **Creator Strategy Syndication (70% Revenue Share)** for finance educators and portfolio builders.
  - **B2B Wealth Structuring Commissions** for family offices and HNIs.
- All forms pre-wired with FormSubmit routing directly to the user's business email (`action="https://formsubmit.co/..."`).

## ☁️ 7. Zero-Cost Cloudflare Pages Deployment Engine
```bash
export CLOUDFLARE_API_TOKEN="<user_token>"
export CLOUDFLARE_ACCOUNT_ID="020d1df3cf57711a7c60d93a9d530c7d"

npx wrangler pages deploy /data/project_qnt/public_deploy --project-name qnt-terminal --branch master
```
