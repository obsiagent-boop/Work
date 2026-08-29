# Project Skills: Enterprise Career Transformation Monograph Standards

## Purpose & Scope
This standard governs the creation of 50+ page, 100% zero-void career transformation and technical upskilling monographs for enterprise operations professionals transitioning into high-leverage roles (Operations Architects, Business Systems Leads, Continuous Improvement Directors).

## Core Architecture & Execution Directives

### 1. 100% Zero-Void Continuous Flow Engineering
- **Elimination of Early Page Breaks:** Hardcoded `page-break-after: always;` and isolated fixed-height card wrappers (>180px) cause WeasyPrint to abort pages prematurely, leaving empty white/cream gaps at the bottom.
- **Continuous Stream Protocol:**
  - Remove all artificial container-level page breaks.
  - Allow rich technical prose, dynamic code snippets, and structured tables to flow naturally from header to footer across all 50+ pages.
  - Apply `break-inside: avoid;` ONLY to small sub-elements (summary tables under 100px, callout boxes) to prevent awkward mid-table splits.
  - Use `break-after: avoid;` on headings and section labels to bind them to the succeeding paragraph.

### 2. Pure Intensive Technical Research Standard
- **No Fabrication & Deep Real-World Tooling:** Every module must contain actual production architectures, exact JavaScript/DAX/VBA code blocks, genuine Erlang C queueing equations, SAP transaction codes (`VA01`, `MM01`, `IW51`), and real-world enterprise operational workflows.
- **Dedicated Master Bibliography at the End:**
  - In addition to inline citations, compile an exhaustive, multi-page Master Reference Directory at the very end of the PDF (Domain 11).
  - Index every official documentation URL, free developer sandbox (`developer.servicenow.com`, `learning.sap.com`, `learn.microsoft.com`, `academy.hubspot.com`), certification syllabus, and premier YouTube video masterclass.

### 3. Luxury Cream & Black Palette Compliance
- **Canvas:** Warm Luxury Cream / Ivory (`#FAF8F5`).
- **Typography:** Pure Pitch-Black (`#000000`) with Inter Variable Font (`file:///data/fonts/InterVariable.ttf`) at compact `1.30–1.34` line-height for clean readability.
- **Dividers & Tables:** 1.5px solid black borders (`#000000`) with high-contrast slate/white callouts (`#F4EFEA`).
