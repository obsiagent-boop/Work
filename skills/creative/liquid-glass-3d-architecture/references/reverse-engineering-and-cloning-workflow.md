# High-Fidelity Website Cloning & Reverse-Engineering Architecture
# Sourced from: ai-website-cloner-template (JCodesMore) & Dribbble Top 1% Design Patterns

## Core Reverse-Engineering Workflow

### 1. Foreperson Pattern: Inspection & Briefing
When tasked with cloning or reverse-engineering a high-prestige website (e.g. Dribbble, Stripe, Linear):
- Extract **both appearance AND behavior**:
  - Appearance: Exact computed styles (`getComputedStyle()`), glass backdrop blur tokens, border radii, high-contrast typography pairings.
  - Behavior: Trigger events (drag deltas, wheel scroll thresholds, intersection observer entry delays, inertia dampening formulas).
- Do not build monolithic multi-part components in one shot: break down sections into sub-150-line focused units.

### 2. Physical Glassmorphism Integration
When cloning liquid glass interfaces:
- Always ensure dynamic moving color sources (e.g., SVG/CSS Aurora Blobs) are positioned directly beneath the glass panels.
- Configure Three.js `MeshPhysicalMaterial` with:
  - `transmission: 0.96` to `0.98`
  - `ior: 1.52` (Crown Glass) to `2.42` (Diamond)
  - `roughness: 0.02` (Mirror Polish)
  - `clearcoat: 1.0` and `clearcoatRoughness: 0.05`
  - `thickness: 2.5` to `3.5` (Subsurface Refraction)

### 3. Dedicated Floating 3D Portal Stages
- Never constrain 3D hero assets inside boxed, rigid widget frames.
- Use seamless, borderless floating glass portal stages (`backdrop-filter: blur(36px) saturate(220%)`, `border-radius: 40px`, and tactile pointer inertia tracking).
