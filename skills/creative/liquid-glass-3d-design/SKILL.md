---
name: liquid-glass-3d-design
description: Build liquid glass WebGL & tactile 3D UI animations.
category: creative/ui-components
triggers:
  - liquid glass
  - 3d animations
  - dribbble 3d
  - glassmorphism webgl
  - tactile 3d web design
---

# Liquid Glass & 3D Interactive WebGL Design Architecture

## Overview
Standard CSS glassmorphism (flat opacity over static backgrounds) fails the luxury standard because real liquid glass requires optical light refraction, sub-surface chromatic dispersion, and dynamic moving gradients beneath the frosted surface.

## Core Rules for Liquid Glassmorphism

### 1. The Dynamic Refraction Requirement
Never place static frosted cards over a solid or static background. Liquid glass requires moving color bodies (e.g. animated radial aurora blobs) behind the glass panel to visibly demonstrate caustic refraction, saturation boost, and chromatic dispersion.

### 2. Apple VisionOS / Awwwards Liquid Glass CSS Spec
```css
.liquid-glass-card {
  background: rgba(255, 255, 255, 0.35) !important;
  backdrop-filter: blur(28px) saturate(200%) brightness(108%);
  -webkit-backdrop-filter: blur(28px) saturate(200%) brightness(108%);
  border: 1.5px solid rgba(255, 255, 255, 0.7);
  border-radius: 36px;
  box-shadow: 
    0 30px 70px -15px rgba(0, 0, 0, 0.12),
    inset 0 1.5px 1.5px 0 rgba(255, 255, 255, 0.9),  /* Top Bevel Highlight */
    inset 0 -1.5px 2px 0 rgba(0, 0, 0, 0.05);        /* Bottom Shadow */
}
```

### 3. Three.js Physical Glass Transmission Material
```javascript
const glassMaterial = new THREE.MeshPhysicalMaterial({
  color: 0xFFFFFF,
  metalness: 0.05,
  roughness: 0.02,
  transmission: 0.98,          // 98% Light transmission
  thickness: 3.5,              // Refraction depth
  ior: 1.52,                   // Crown Glass Refraction Index
  reflectivity: 0.9,
  clearcoat: 1.0,              // High-gloss lacquer layer
  clearcoatRoughness: 0.05,
  transparent: true,
  opacity: 0.95
});
```

## Dribbble-Grade 3D Fintech Animation Archetypes

1. **3D Real Dollar Coin ($):** Heavy 24k gold bullion disc with 48 radial edge reeding teeth, double-struck high-relief serif dollar monogram (`$`) front and back, and gyroscopic orbital halos with 12 crystal factor nodes.
2. **3D Kinetic Typography (`$ Q N T`):** Extruded glass letters orbiting and tumbling on Euler axes with spring inertia.
3. **Magnetic Bouncing Spheres:** Multi-asset spheres reacting to cursor motion with spring repulsion.
4. **Multi-Layered Glass Cards:** Thick frosted credit card with embedded metallic gold chip and rotating halo ribbons.
5. **Perlin-Noise Metasurface Blobs:** Oscillating vertex ripples simulating liquid mercury or organic water droplets.
6. **Elevating 3D Bar Graph Pillars:** Translucent glass pillars scaling with sinusoidal time pulses.
7. **Gyroscopic Portal Halos:** Interlocking concentric rings spinning with counter-rotations.

## Light Liquid Design & Contrast Standards
- **Background Canvas:** Prefer light Luxury Cream (`#FAF8F5`) or soft slate-blue pastel backgrounds over dark voids unless explicitly instructed.
- **High-Contrast Legibility:** Ensure headline typography is pitch black (`#0A0E1A` / `#000000`) using bold modern typefaces (Syne, Plus Jakarta Sans, Clash Display) so all copy is razor-sharp against frosted cards.
- **Spacious Macro-Layout:** Employ generous spacing and macro padding (`pt-12`, `mb-24`, `gap-12`) to prevent UI clutter.
- **Modular Editability:** Organize the codebase into clearly labeled token maps and component blocks so future modifications via natural language commands can be applied with precision.

## Direct Gesture & Inertial Physics
Never leave 3D models purely floating in the background without direct interaction. Embed models into tactile glass canvas containers with mouse and touch listeners (`mousedown`, `mousemove`, `touchstart`, `touchmove`) enabling direct 3D drag rotation with momentum.
