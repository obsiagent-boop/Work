# Document Extraction & Archiving Reference (Firecrawl AnyDoc)

## AnyDoc Overview
AnyDoc is Firecrawl's Rust-powered document-to-markdown conversion engine with Node.js and Python bindings.

## Supported Formats
- Office & Presentations: `.docx`, `.doc`, `.pptx`, `.ppt`, `.odt`, `.odp`
- Spreadsheets: `.xlsx`, `.ods`, `.csv`
- Books & Documents: `.pdf`, `.epub`, `.rtf`

## CLI Commands
```bash
# Convert to stdout
anydoc input.docx

# Convert to file
anydoc input.pptx -o output.md
```

## Python Integration
```python
import anydoc

# File conversion
md_text = anydoc.to_markdown("path/to/file.docx")

# In-memory conversion
md_text = anydoc.to_markdown_bytes(raw_bytes, format="docx")
```

## Agency Engine Path
- Unified script: `/data/integrations/agency_doc_engine.py`
- Usage: `python3 /data/integrations/agency_doc_engine.py parse <file> <out.md>`
- PDF generation: `python3 /data/integrations/agency_doc_engine.py pdf <title> <in.md> <out.pdf>`
