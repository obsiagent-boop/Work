# Master ATS Parsing & Resume Formatting Guidelines (100% Pass Rate Standard)

## Core ATS Parsing Vulnerabilities & Structural Directives
Modern Applicant Tracking Systems (Workday, Greenhouse, Taleo, iCIMS, Lever, Ashby, BambooHR) parse documents linearly. Any complex desktop-publishing layouts (multi-column tables, floating text boxes, graphic canvases) result in garbled text streams, skipped sections, or dropped contact data.

### 1. Typography & Strict Size Thresholds
- **Allowed Standard Fonts Only:** Calibri, Arial, Helvetica, Georgia, Times New Roman.
- **Strictly Prohibited:** Script fonts, condensed/narrow variants, custom web fonts, or decorative glyphs.
- **Font Size Hierarchy:**
  - **Candidate Name / Header:** `14 pt – 16 pt` Bold.
  - **Standard Section Headings:** `12 pt – 14 pt` Bold, uncolored (#000000), uppercase or title case.
  - **Body & Bullet Points:** `10 pt – 12 pt` Regular.
  - **Subtitles & Dates:** `9 pt – 10 pt` Regular or Italic.

### 2. Layout & Container Rules (Zero-Artifact Standard)
- **Zero Tables:** Never use Word or HTML tables for multi-column alignment (e.g. putting company on left and dates on right inside a table cell). Many legacy ATS parsers concatenate table cells horizontally rather than vertically.
- **Zero Text Boxes & Canvas Shapes:** Never place text inside floating shapes, callout boxes, or header/footer containers. All text must reside in the standard document body stream.
- **Zero Graphics / Icons:** Never use social icon images (phone glyphs, email envelope icons, LinkedIn logos) for contact info. Use plain text: `City, Country | LinkedIn: url | Email: text`.
- **Standard Bullet Symbols:** Use standard round filled bullets (`•` / `List Bullet`), not custom chevrons, arrows, or checkboxes.

### 3. Canonical Section Naming Standards
ATS keyword classifiers map experience using exact standard dictionaries. Never use creative or colloquial section headings.
- **Approved Headings:**
  - `Professional Summary` (or `Summary`)
  - `Work Experience` (or `Professional Experience`, `Experience`)
  - `Education`
  - `Skills` (or `Technical Skills`)
  - `Key Achievements` (or `Achievements`, `Certifications`)

### 4. File Format Deliverable Priority
- **Primary Deliverable:** `.docx` (Microsoft Word XML document). `.docx` is universally parsed across 100% of legacy and modern ATS engines with zero font embedding or rendering layer issues.
- **Secondary Deliverable:** Clean, single-column 1-page `.pdf` compiled strictly from linear document flows.
