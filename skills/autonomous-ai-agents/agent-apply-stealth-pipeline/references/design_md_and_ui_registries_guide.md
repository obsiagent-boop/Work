# DESIGN.md Token Spec & UI Component Registry Integration

## 1. Overview
This reference specifies the standards for extracting, parsing, and applying `DESIGN.md` token specifications alongside the 7 UI component registries (`reactbits.dev`, `refero.design`, `ui.aceternity.com`, `21st.dev`, `componentry.dev`, `toggle.supply`, `motion.dev`).

## 2. Mandatory Workflow Habit (User Correction)
**Always communicate the architectural plan, visual tokens, and design references to the user BEFORE building.**
- State the color palette (Cyber Void `#060811`, Electric Cyan `#06B6D4`, Luxury Cream `#FAF8F5`).
- State the target components (Aceternity Bento Grid, ReactBits animated counters, Componentry tabs).
- State the functional interactive features (live JavaScript calculator, modal drawers, dynamic filters).
- Wait for user confirmation before executing full production writes.

## 3. The 9 DESIGN.md Extraction Engines
1. `getdesign.md` — 300+ Google DESIGN.md spec catalog.
2. `designmd.cc` — Live DOM/CSSOM computed styles & DTCG token extractor.
3. `designmd.ai` — AI-native design systems repository (Genesis, Dark Immersive).
4. `styles.refero.design` — 2,000+ real-world UI design system specs.
5. `context.dev/free-tools/design-md-generator` — Brand Styleguide & Screenshot API generator.
6. `design-extractor.com` — Live Tailwind v4 and DTCG tokens from any URL.
7. `designmd.supply` — Open-source styleguide collection.
8. `designmd.me` — AI-generated DESIGN.md files with HTML specimens and Figma variables.
9. `aura.build/design-systems` — AI website builder design system benchmarks.

## 4. UI Component Library Integrations
- **Aceternity UI (`ui.aceternity.com`):** Copy-paste Tailwind + Framer Motion components (BentoGrid, BackgroundBeams, GlowingBorder, 3DCardPin).
- **ReactBits (`reactbits.dev`):** Animated React/Tailwind elements (CounterStreamer, ParticleBackground, InteractiveStatSelector).
- **Refero Design (`refero.design`):** Benchmark screenshots and real-world flow references for Linear, Stripe, Vercel styles.
- **Componentry (`componentry.dev`):** Accessible animated tabs, toggles, popovers, and interactive modals.
- **Toggle Supply (`toggle.supply`):** Micro-interactions, tactile switches, zero-dependency state toggles.
- **Motion Dev (`motion.dev`):** Physics-based transitions, elevation shifts (`transform -translate-y-1`), and scroll listeners.
- **21st.dev (`21st.dev`):** 12,000+ Tailwind CSS component registry.

## 5. Standard Interactive SaaS Template Pattern
When creating any SaaS landing page, ensure 100% functionality across every interactive zone:
- Dynamic calculation engine ($A = P(1+r)^t$) with live DOM recalculation.
- Interactive principal/strategy toggle pills.
- Mobile-responsive navigation and sticky glassmorphic headers (`backdrop-blur-12px`).
- Valid download endpoints for generated PDF compendiums and dossiers.
