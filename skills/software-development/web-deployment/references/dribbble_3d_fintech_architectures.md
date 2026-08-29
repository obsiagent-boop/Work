# Dribbble 3D WebGL Fintech Reverse-Engineering Specification

## Overview
A master reference specification for reverse-engineering and implementing viral Dribbble, Spline 3D, and Awwwards-grade 3D WebGL fintech design systems into complete, whole-page web applications.

---

## 🎨 1. The 3 Primary Dribbble Fintech Architectural Paradigms

### A. The Intelliphy Architecture (Anatoliy Demyanchuk Standard)
* **Visual Identity:** Soft slate/periwinkle canvas (`#9EAFCA` to `#A4B4CB`) contrasted with deep navy footer (`#010B1E`) and electric royal blue accent buttons (`#002BFF`).
* **Layout Structure:**
  1. **Bracketed Section Hierarchy:** Uses technical brackets (`[About]`, `[Asset Selection]`, `[Service Type]`, `[Menu]`, `[Documentation]`) for structural labels.
  2. **Split Hero Stage:** Left-aligned headline in clean sans-serif with a dedicated central 3D WebGL canvas container and right-aligned royal blue exploration cards.
  3. **High-Performance Telemetry Diagram:** Circular 24-ray geometric ray diagram with center concentric hubs.
  4. **Parabolic Milestone Arcs:** Staggered roadmap cards connected by dashed parabolic Bezier curve vectors (`M1–M4`).
* **3D WebGL Asset:** Extruded 3D hexagonal ring in frosted optical glass (`MeshPhysicalMaterial`, `thickness: 3.5`, `ior: 1.54`) encasing an internal liquid royal blue emissive torus core.

---

### B. The OpenSim Cosmic Void Architecture
* **Visual Identity:** Abyssal space black (`#030712`) with glowing cyan/neon blue typography and high-saturation volumetric lighting.
* **Layout Structure:**
  1. **Monumental Neon Typography:** Gigantic hero titles (`text-8xl` to `text-9xl`) with wide tracking and deep cyan text shadows (`text-shadow: 0 0 40px rgba(6,182,212,0.6)`).
  2. **Pill Action Triggers:** Solid white pill buttons (`ENTER WORLD`) with dark hover fills.
  3. **Cosmic Allocation Bento:** Deep frosted glass cards (`rgba(15,23,42,0.65)`) with subtle cyan border outlines.
* **3D WebGL Asset:** Dense glowing blue ion sphere with an inner solid emissive core, high-density geometric wireframe grid, and 500+ floating volumetric sparkling ion particles.

---

### C. The Priceless RWA Tokenized Architecture
* **Visual Identity:** Deep velvet black (`#06070B`) with neon magenta (`#F43F5E`) and cyan dual-light specular highlights.
* **Layout Structure:**
  1. **Floating Metric Badges:** Translucent neon glass pill badges (`$16 Trillion`, `$33 Millions`) anchored at asymmetrical coordinates across the 3D stage.
  2. **Tokenized RWA Vault Grid:** Multi-tier institutional asset cards with bold rate callouts.
* **3D WebGL Asset:** 4 Staggered floating isometric frosted glass bricks rendered from an angled isometric perspective (`camera.position.set(12, 14, 18)`), refracting multi-point magenta and cyan studio point lights.

---

## 🛠️ 2. Core Three.js Optical Physical Glass Shader Recipe

To replicate authentic Dribbble glass in pure JavaScript:

```javascript
const glassMaterial = new THREE.MeshPhysicalMaterial({
  color: 0xFFFFFF,
  metalness: 0.1,
  roughness: 0.05,
  transmission: 0.96,        // Optical light transmission
  thickness: 3.2,            // Refraction depth
  ior: 1.54,                 // Crown glass refraction index
  reflectivity: 0.9,
  clearcoat: 1.0,            // Top liquid lacquer sheen
  clearcoatRoughness: 0.05,
  transparent: true,
  opacity: 0.92
});
```

---

## ⚠️ 3. Key Operational Rules
1. **Never build partial widgets:** When tasked with emulating a Dribbble shot, implement the **entire whole-page experience** (Navbar, Split Hero, Interactive 3D Canvas, Telemetry Diagrams, Roadmap Arcs, Dark Contrast Statistics Banners, and Bracketed Footers).
2. **Preserve Production Environments:** Always stage experimental Dribbble architectures in dedicated subdirectories or subprojects (e.g. `qnt-dribbble-lab`), leaving the live production domain untouched.
