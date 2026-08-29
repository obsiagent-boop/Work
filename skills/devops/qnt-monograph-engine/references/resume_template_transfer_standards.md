# Zero-Data-Loss Resume Template Mapping & Formatting Standards

## Purpose
Use when transferring a candidate's complete career history from an existing resume into a new template format (e.g. standard 1-page ATS template in `.docx` and `.pdf`) with 100% fidelity, exact section ordering, and zero information loss.

## Core Rules & Execution Architecture

### 1. Zero-Data-Loss Standard
- **Preserve Every Metric & Detail:** Never truncate, summarize away, or omit past companies, titles, dates, metrics, percentages, tools, or awards.
- **Section Order Mapping:** Match the exact section sequence of the target template:
  1. Header: Full Name, Target Professional Title, Contact & Location.
  2. Professional Summary: Dense 3–4 line executive synthesis highlighting total experience, top clients, and core leadership/technical methodologies.
  3. Education: University, Degree, Specialization/Coursework, Location, Dates.
  4. Technical Skills & Core Competencies: Segmented by domain (Leadership/Methodologies, Platforms/CRM, Analysis/Languages).
  5. Professional Experience: Reverse chronological order with two-column headers (Company/Role left, Dates/Location right) and quantifiable bullet points.
  6. Key Achievements & Awards: Highlighted recognitions and milestone deliveries.

### 2. Microsoft Word (`.docx`) Construction Standards
- **Two-Column Headers via Borderless Tables:** In `python-docx`, construct clean two-column sub-headers using borderless tables (`<w:tcBorders w:val="none"/>`) rather than tab stops, ensuring cross-platform ATS parser compatibility.
- **Section Dividers:** Add standard solid black bottom borders (`<w:bottom w:val="single" w:sz="12" w:color="000000"/>`) directly to the section heading paragraph properties.
- **Margins & Spacing:** Set tight, professional margins (0.5 in / 12.7 mm) with compact paragraph spacing (`space_before: 1-2pt`, `space_after: 1-2pt`, `line_spacing: 1.05-1.1`).

### 3. Exact 1-Page ATS PDF Generation via WeasyPrint
- **Font & Size Budget:** Use `Calibri` / `Inter Variable` with base body size `7.8pt – 8.2pt` and line-height `1.20 – 1.25`.
- **Page Budget Clamping:** Ensure total content height fits strictly onto a single `letter` or `A4` page canvas without triggering an accidental 2nd page spillover.
- **Visual Verification:** Render rendered page PNGs via `pymupdf` and inspect with `vision_analyze` to verify 1-page completion before delivery.
