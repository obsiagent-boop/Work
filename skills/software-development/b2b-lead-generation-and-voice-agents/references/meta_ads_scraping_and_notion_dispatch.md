# Meta Ad Library Scraping, Notion Binary Uploads & Clickable Outreach Standards

## 1. Zero-Fabrication Meta Ad Library Prospecting SOP
- **Direct Advertiser Link Rule:** Never provide generic keyword search query links (`q=greens%20powder`). Always extract and link to the brand's verified direct Meta Ad Library page link using `view_all_page_id=<PAGE_ID>` (e.g. `https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=183869772601&search_type=page&media_type=all`).
- **Multi-Portal Enrichment:** For every client audit, provide:
  1. Direct Meta Ad Library Live Ads Link (`view_all_page_id`)
  2. Official Brand Website Store Domain
  3. Direct Instagram Profile for DM Outreach
  4. Empirical Flaw Diagnosis (blurry text, flat static photos, no 0-3s hook)
  5. Mastermind 3-Second Viral Redesign (Hook + AI Visual Prompt + VO Script + On-Screen Text)

## 2. Clickable Links Standards in Notion & Excel
- **Notion Rich Text Links:** In Notion block payloads, format clickable links as:
  ```json
  {"type": "text", "text": {"content": "👉 Open Live Meta Ads", "link": {"url": "https://..."}}, "annotations": {"bold": true, "color": "blue"}}
  ```
- **Excel Native Hyperlinks:** When generating `.xlsx` workbooks with `openpyxl`, write native Excel formula strings:
  ```python
  ws.cell(row=r, column=c, value=f'=HYPERLINK("{url}", "👉 Open Live Meta Ads")')
  ```

## 3. Notion 3-Step Binary File Upload Pipeline
To upload binary PDFs, Excel workbooks, or media files directly into Notion:
1. **Initiate Upload:**
   ```bash
   POST https://api.notion.com/v1/file_uploads
   Body: {"filename": "report.pdf", "content_type": "application/pdf"}
   Returns: {"id": "file_upload_id", "upload_url": "https://..."}
   ```
2. **Post Binary Bytes:**
   ```bash
   POST {upload_url}
   Multipart/form-data with binary file payload.
   ```
3. **Attach File Block to Page:**
   ```bash
   PATCH https://api.notion.com/v1/blocks/{page_id}/children
   Body: {
     "children": [
       {
         "object": "block",
         "type": "file",
         "file": {
           "type": "file_upload",
           "file_upload": {"id": "file_upload_id"},
           "name": "report.pdf"
         }
       }
     ]
   }
   ```

## 4. PDF Generation Standard (WeasyPrint vs ReportLab)
- **ReportLab Canvas Pitfall:** In ReportLab, drawing a full-page rectangle in `NumberedCanvas.draw_page_decorations` after flowable rendering paints OVER the text layer, rendering the PDF visually blank.
- **WeasyPrint Best Practice:** Use HTML/CSS Paged Media with explicit `@page` background rules (`background-color: #000000;`), `@top-center` running headers, and `@bottom-right` dynamic page numbering counters for institutional-grade dark presentation documents.
