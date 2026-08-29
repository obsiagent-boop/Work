# Precise Career Title Customization & Micro-Edits in ATS Resumes

## Core Principles
1. **Zero-Data-Loss Invariance:**
   - When modifying specific titles or role designations (e.g. updating candidate name to full legal name, altering target title to "Assistant Manager", or removing specific sub-designations like "POD Lead"), all underlying bullet points, metrics, and achievements must remain 100% intact.
   - Do not summarize, rephrase, or drop supporting bullets unless explicitly instructed.

2. **1-Page Visual Budget Preservation:**
   - Any addition or subtraction of text in headings or job headers must maintain the exact 1-page budget in PDF rendering.
   - Ensure line-height (1.18–1.22) and margins (0.4–0.5 in) dynamically balance so no secondary trailing page is produced.

3. **Multi-Format Parity (.docx & .pdf):**
   - Every single resume modification must update both the Microsoft Word `.docx` file (via `python-docx` XML table/border styling) and the `.pdf` render (via `WeasyPrint` and verified with `pymupdf` / `vision_analyze`).
   - Automatically commit and push both synchronized files to Git under `obsiagent-boop`.
