# qnt. 3D WebGL Web Platform Architecture & UI Standards

## 🏛️ Core Design Mandates & Pitfalls Discovered

### 1. Pure "qnt." Brand Identity Lockup
- **Zero Distracting Sub-Badges:** Never attach extra badges (e.g. "3D Sovereign", mini boxes with "Q") directly beside the `qnt.` logo in headers. The brand name must stand 100% pure, bold, and undisturbed with the signature period accent (`qnt.`).
- **3-Line Hamburger Slide-Out Navigation:** The header must feature an independent, bold 3-lines menu button positioned to the left of `qnt.` that triggers a slide-out navigation drawer with smooth backdrop blur.

### 2. High-Contrast Luxury White / Cream (#FAF8F5 / #FFFFFF) UI Standard
- **Black Typography on Light Canvas:** To prevent text washing out on mobile Safari/Chrome or OS light-mode triggers:
  - Background must be fixed to `#FAF8F5` / `#FFFFFF`.
  - All headings and body text must use solid pitch-black ink (`#000000` / `#060811`) with high contrast.
  - All interactive buttons, toggle pills, and filter tabs must use solid high-contrast black/white styling with bold text (`#000000` text on inactive pills, white text on active black pills).

### 3. Real-Time 3D Financial WebGL Scene (Three.js Powered)
- **Finance-Specific 3D Assets:** Avoid generic wireframe geometries. Hero sections must feature a real-time rotating **3D Golden Metallic Dollar Asset (`$`)** with specular lighting, depth reflections, and an electric cyan orbital halo.
- **Mouse & Touch Inertia:** WebGL camera must respond dynamically to user cursor movement and touch scrolling.

### 4. Interactive Live Database Table Engine
- **In-Page Quantitative Search & Filtering:** The platform must embed a live client-side searchable and filterable 200-asset database table showing Asset ID, Tier, 5Y Rolling CAGR, and exact Statutory Tax Law Protections.

### 5. Expandable Sub-Functionalities on All Factor Desks
- Every card in the 6-Desk Institutional Matrix must be clickable to expand a dedicated sub-drawer revealing exact portfolio holdings, 99% VaR drawdown limits, Fama-French alpha spreads, and monthly cashflow payout rules.

### 6. Dual-Rail Backend Architecture (Supabase PostgreSQL + FormSubmit / Zoho Email)
- All modal forms must feature **Dual-Rail submissions**:
  1. Client-side database insert to **Supabase** (`@supabase/supabase-js`) for instant live table tracking.
  2. Automatic form delivery via **FormSubmit** (or custom Zoho workmail) for zero-cost immediate email notifications.

### 7. Developer Code-Spaces & Zero Data Loss Customization Map
- All core sections are mapped to specific lines in `index.html`: Three.js scene (lines 440–520), SQL Database (lines 535–590), Slide Menu (lines 112–148), Compounding Math (lines 595–635), 6-Desk expanders (lines 250–350), and Dual Backend hooks (lines 380–435).

## 💻 Developer Customization Protocol

### A. Modifying the 3D WebGL Shader / Mesh
```javascript
// Located in init3D() inside index.html
const customMaterial = new THREE.MeshStandardMaterial({
  color: 0x06B6D4,   // Electric Cyan
  metalness: 0.90,
  roughness: 0.15
});

// Custom 3D Polyhedral Diamond mesh:
const diamondGeo = new THREE.IcosahedronGeometry(4, 0);
const diamondMesh = new THREE.Mesh(diamondGeo, customMaterial);
dollarGroup.add(diamondMesh);
```

### B. Appending New Assets to SQL Database (Zero Data Loss)
```javascript
// Append directly to assetDatabase[] in index.html:
{ 
  id: 11, 
  name: "Global Quantum Semiconductor ETF (SMH)", 
  tier: "tier4", 
  tierName: "Tier 4: Global AI Hardware", 
  rate: "31.40% INR CAGR", 
  tax: "Global Monopolies + 3.2% USD/INR Tailwind", 
  link: "https://www.indmoney.com" 
}
```

### C. Zero-Downtime Deployment & Version Control
- Deploy via Wrangler: `npx wrangler pages deploy /data/project_qnt/public_deploy --project-name qnt-terminal`
- Sync to Git: `git push -u origin master` under `obsiagent-boop` (`https://github.com/obsiagent-boop/qnt-wealth-platform.git`).
