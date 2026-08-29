---
name: qnt-pdf-generator
description: "Use when asked 'pdf for qnt.'. Generates qnt quant PDFs."
platforms: [linux, macos, windows]
---

# qnt. Master PDF & Content Generation Skill

## Trigger
Use this skill whenever the user mentions `"pdf for qnt."` or requests a branded `qnt.` research PDF, viral concept dossier, or academic quantitative monograph.

## Core Directives
1. **Visual Styling:**
   - Pure pitch-black monochrome canvas (`#000000`)
   - Official `qnt.` logo engraved on the cover and running headers (`/data/cache/images/img_3e4fbac95420.jpg`)
   - High-contrast pure white typography (`#FFFFFF`), ice slate (`#94A3B8`), and electric cyan/emerald accents (`#38BDF8`, `#34D399`)
2. **Content Architecture:**
   - University citations (Bachelier, Turing, Mandelbrot, Shannon, Lorenz, Simons, Vaswani)
   - 200+ unique, mathematically grounded concepts across Quant, AI, Forex, Crypto, and Chaos Physics
   - 5-year-old intuitive models for every complex formula
   - Viral Instagram hook and video prompts for each concept
   - 4-Tier Monetization Ladder and VIP Instagram Networking Map
3. **Execution Pipeline:**
   - Compile via WeasyPrint (`weasyprint /tmp/qnt.html /data/reports/qnt_...pdf`)
   - Verify visually via PyMuPDF image rendering
   - Validate with Firecrawl AnyDoc (`/data/bin/anydoc ... -o ...md`)
   - Push all assets to GitHub under `obsiagent-boop` (repos: `personal-agent-os` and `project-anya`)
   - Deliver via `MEDIA:/data/reports/...`
