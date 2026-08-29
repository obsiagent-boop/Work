---
name: liquid-glass-3d-architecture
description: Use when building 3D liquid glass WebGL designs and Dribbble-grade fintech art sculptures.
---

# Liquid Glass 3D WebGL & Dribbble Architecture Skill

## 1. True Liquid Glass Principles (Apple VisionOS & Awwwards Standard)
To make liquid glass realistic in the browser, the surface CANNOT sit over a static/flat background. It requires **moving, dynamic color and light sources directly behind it** to demonstrate optical refraction and caustic dispersion.

### Core CSS Tokens for Liquid Frosted Glass Panels
```css
.liquid-glass-panel {
  background: rgba(255, 255, 255, 0.35) !important;
  backdrop-filter: blur(28px) saturate(200%) brightness(105%);
  -webkit-backdrop-filter: blur(28px) saturate(200%) brightness(105%);
  border: 1.5px solid rgba(255, 255, 255, 0.7);
  border-radius: 36px;
  box-shadow: 
    0 30px 60px -12px rgba(0, 0, 0, 0.08),
    0 18px 36px -18px rgba(0, 0, 0, 0.05),
    inset 0 1px 1px 0 rgba(255, 255, 255, 0.9),
    inset 0 -1px 2px 0 rgba(0, 0, 0, 0.05);
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Seamless Floating 3D Portal Stage (No Boxy Widgets)
Never place 3D objects in rigid, boxed widget containers. Always use a seamless, borderless floating glass portal stage:
```css
.portal-3d-stage {
  background: rgba(255, 255, 255, 0.35) !important;
  backdrop-filter: blur(36px) saturate(220%) brightness(110%);
  -webkit-backdrop-filter: blur(36px) saturate(220%) brightness(110%);
  border: 1.5px solid rgba(255, 255, 255, 0.8);
  border-radius: 40px;
  box-shadow: 
    0 35px 80px -15px rgba(0, 0, 0, 0.18),
    inset 0 2px 2px 0 rgba(255, 255, 255, 0.9),
    inset 0 -2px 3px 0 rgba(0, 0, 0, 0.08);
  position: relative;
  cursor: grab;
  overflow: hidden;
}
```

### Background Aurora Gradient Blobs (The Refraction Engine)
```css
.liquid-blob {
  position: fixed;
  width: 550px;
  height: 550px;
  background: radial-gradient(circle, #06B6D4 0%, transparent 70%);
  filter: blur(80px);
  opacity: 0.45;
  z-index: 0;
  animation: floatBlob 18s ease-in-out infinite alternate;
  pointer-events: none;
}
```

---

## 2. Three.js Physical Glass Transmission Shaders (`MeshPhysicalMaterial`)
Never use basic wireframes or dull materials for glass. Use physical transmission with high index-of-refraction (IOR) and specular clearcoats:

```javascript
const physicalGlassMaterial = new THREE.MeshPhysicalMaterial({
  color: 0xFFFFFF,              // Base glass tint (can be pastel tinted)
  metalness: 0.05,              // Low metallic
  roughness: 0.02,              // Mirror polish
  transmission: 0.98,           // Optical transmission (98% light passthrough)
  thickness: 3.5,               // Subsurface refraction depth
  ior: 1.54,                    // Standard Crown Glass Refraction Index
  reflectivity: 0.9,
  clearcoat: 1.0,               // Top liquid lacquer sheen
  clearcoatRoughness: 0.05,
  transparent: true,
  opacity: 0.95
});
```

---

## 3. Dribbble-Grade 3D Architectural Weaponry & Interactive Art Sculptures
See `references/3d-art-icons-and-fintech-blueprints.md` for full geometry blueprints, lighting rigs, and physical shaders.
See `references/dribbble-full-page-and-3d-dollar-architecture.md` for full-page Dribbble layout reverse-engineering and 3D Real Dollar Sovereign Bullion code.
See `references/reverse-engineering-and-cloning-workflow.md` for high-fidelity reverse-engineering and cloning workflows sourced from ai-website-cloner-template.
Implement high-concept Dribbble fintech archetypes:
1. **The Sovereign Bullion Ingot in Quartz Obelisk:** Heavy 3D Gold Bar with 999.9 purity stamps encased in an optical frosted glass obelisk with rotating laser crests.
2. **The Quantum Sovereign Aegis:** Multi-layered faceted crystal shield with an internal glowing neon core & orbital laser halos.
3. **The Neo-Black Obsidian Titanium Card:** Revolut/Apple Card standard with embedded 3D metallic chip & debossed typography.
4. **The Alpha Quantum Prism Bolt:** Sharp faceted crystal lightning sculpture with internal refractive lattice.
5. **The Hyper-Fluid Liquid Glass Nautilus:** Bio-computational mathematical spiral with iridescent chromatic oil-slick sheen.
6. **The Institutional Multi-Currency Gyroscope:** Interlocking brushed gold & glass gimbals holding floating $, ₹, €, £ tokens.
7. **The Monolithic Compounding Crystal Pillars:** 5 Tiered crystal columns with gold-leaf caps and real-time laser grid indicators.
8. **The Wealth Velocity DNA Double Helix:** Intertwined glass and polished gold molecular strands connected by glowing milestone nodes.
9. **The Neomorphic Viscous Asset Capsule:** High-precision glass pill containing floating magnetic factor spheres.
10. **The Sovereign Grand Opus Dodecahedron:** Breathing faceted quartz dodecahedron with an embedded 24k gold core.
11. **3D Kinetic Typographic Meshes ($ Q N T):** 3D extruded Frosted Glass letterforms tumbling in multi-axis spring inertia.
12. **Funky Magnetic Gravity Physics Playgrounds:** Floating multi-asset magnetic spheres & gold coins bouncing organically with dynamic spring repulsion.
13. **Tactile Gesture Drag & Inertia:** Dedicated container with pointer events allowing the user to grab and spin objects in 3D space with angular velocity.
14. **High-Relief Sovereign Bullion Dollar ($) Coin:** Double-sided high-relief embossed 3D currency bullion ($) in polished 24k gold alloy (`metalness: 0.96`, `roughness: 0.12`) with 48 radial edge reeding teeth, double-struck serif dollar bars, beveled rim, gyroscopic orbital halos (`wireframe: true`), and 12 orbiting crystal factor shards.
15. **Dribbble Design-to-Code Reverse-Engineering Standard:** When emulating Dribbble/Awwwards showcase screenshots, emulate the ENTIRE full-page architecture (bracketed split heroes, circular telemetry ray diagrams, parabolic dashed milestone curves `M1–M4`, and monumental typography) instead of a minimal partial component mockup, while maintaining pure, unadulterated project branding without leftover template names.
16. **Modular Single-File Custom Command Architecture & Legibility Standard:**
    - Always build on luxury Light Liquid Canvas (`#FAF8F5` Cream or pastel frosted glass) with high-contrast pitch-black typography (`#0A0E1A`) using premium fonts (Syne, Plus Jakarta Sans, Clash Display) so all text is 100% legible and readable.
    - Structure single-file apps into cleanly segmented, tokenized module blocks (Theme Config Tokens, 3D Canvas Rig, Compounding Engine, SQL Database, 6-Desk Allocator, Modals) for effortless zero-regression editing.
    - Expose a clear, declarative Command Matrix so users know the exact high-level commands to modify any theme token, 3D geometry, typography, spacing, or financial formula.
17. **Liquid Obsidian Black & Pure White Cinematic Video Standard:**
    - See `references/liquid_black_3d_and_diffusion_standards.md` for the complete Liquid Obsidian Black (`#02040A` -> `#000000`), crisp white Inter Variable typography, and CogVideoX-2B zero-OOM CPU offloading workflows.
18. **Multi-Project Brand & Git Remote Isolation:**
    - When directed to create a new standalone project (e.g. `7Theory` / `detail.7`), isolate code into a dedicated repository and workspace with zero cross-brand contamination.
    - Always verify active Git remote origin URLs and credentials to ensure commits go strictly to the user's intended Git account (`obsiagent-boop`).
    - For standalone web apps, embed high-resolution visual assets as Base64 Data URIs (`data:image/jpeg;base64,...`) to guarantee zero-broken-link portability across local previews, Cloudflare Pages, and CDN hosting.
19. **Full-Bleed Parallax Background & Liquid Overlay Architecture:**
    - When user requests image backgrounds across a sequential scroll (e.g. 7 stages / protocols), do NOT nest images inside small card widgets.
    - Set the high-resolution images as full-bleed, parallax-fixed section backgrounds (`background: linear-gradient(...), url(...) center/cover no-repeat fixed`).
    - Place ultra-translucent frosted glass shells (`background: rgba(13, 10, 24, 0.48); backdrop-filter: blur(32px) saturate(210%);`) over the background images with glowing transparent typography (`-webkit-background-clip: text; -webkit-text-fill-color: transparent;`).
    - Watermark stage numbers with giant semi-transparent gradient numbers (`01`–`07`) sitting directly in the liquid layer.

