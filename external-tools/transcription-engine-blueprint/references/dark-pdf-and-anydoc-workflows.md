# Dark PDF Generation & AnyDoc Document Workflows

## 1. High-Performance Dark PDF Generation (CSS Paged Media via WeasyPrint)

### Why WeasyPrint over ReportLab for Dark Mode
ReportLab's two-pass `NumberedCanvas` often paints over rendered text if full-page background rectangles are executed during `showPage` or `save()`. WeasyPrint uses W3C standard CSS Paged Media where background colors belong to `@page`, guaranteeing text renders cleanly on top.

```python
import weasyprint

html_content = """<!DOCTYPE html>
<html>
<head>
<style>
  @page {
    size: letter;
    margin: 18mm 15mm 18mm 15mm;
    background-color: #000000;
    @top-center {
      content: "BRAND | DOCUMENT TITLE";
      font-size: 8pt;
      color: #64748B;
      border-bottom: 0.5pt solid #1E293B;
      padding-bottom: 4px;
    }
    @bottom-right {
      content: "Page " counter(page) " of " counter(pages);
      font-size: 8pt;
      color: #94A3B8;
    }
  }
  body {
    background-color: #000000;
    color: #F8FAFC;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }
</style>
</head>
<body>
  <h1>Document Title</h1>
  <p>Content goes here...</p>
</body>
</html>"""

weasyprint.HTML(string=html_content).write_pdf("output.pdf")
```

### Visual Verification Rule
Always render at least pages 0 and 1 to PNG via PyMuPDF before delivering to the user:
```python
import pymupdf

doc = pymupdf.open("output.pdf")
doc.load_page(0).get_pixmap(dpi=150).save("/tmp/verify_page_0.png")
```

---

## 2. AnyDoc 14-Format Conversion Pipeline (Firecrawl AnyDoc)

Use `anydoc` to ingest and normalize any office or media document into GitHub-Flavored Markdown:

```python
import anydoc

# Filepath input -> Markdown string output
markdown_text = anydoc.to_markdown("document.docx")  # Works with .pptx, .xlsx, .pdf, .epub, .csv
```
CLI usage:
```bash
anydoc presentation.pptx -o presentation.md
```
