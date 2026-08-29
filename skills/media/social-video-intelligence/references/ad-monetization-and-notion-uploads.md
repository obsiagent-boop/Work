# Ad Creation, AI Creative Direction & Notion Binary File Uploads

## 1. Zero-Infrastructure Ad Creative Monetization Plays
- **Meta Ad Library Scraper:** Search `facebook.com/ads/library` by niche (e.g. D2C Supplements, Skincare, Fashion). Find active advertisers running low-CTR ads with weak 0-3s hooks. Rebuild 2 motion video concepts in CapCut/Runway and send a 45s Loom pitch.
- **Freelance Fast-Bids:** Filter Upwork, Contra, Billo.app by "Payment Verified" + "<5 proposals" for urgent ad redesign gigs ($150-$500/gig).
- **AI Stylist & E-Commerce Reskinning:** Place flat Amazon/Shopify product photos onto AI runway models or luxury studio backgrounds using FLUX.1/Midjourney/Runway ($500-$2,500/collection).

## 2. Meta Ad Library Live Link Protocol
- Never use generic search keywords (e.g. `q=keyword`) in client deliverables, as they show random search results rather than the specific client's active ads.
- Always locate the advertiser's official Meta Page ID and use the direct `view_all_page_id` parameter:
  `https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=<PAGE_ID>&search_type=page&media_type=all`

## 3. Excel Spreadsheet Hyperlink Protocol
- When building client lead lists or outreach databases in `.xlsx` format, use native openpyxl formulas:
  `ws.cell(row=r, column=c, value=f'=HYPERLINK("{url}", "👉 Open Live Meta Ads")')`
- Set font formatting with underline and color `#0284C7` to ensure immediate visual recognition as a clickable element.

## 4. Multi-Slide Carousel OCR & Visual Verification
- When transcribing Instagram carousel posts (which may contain 5-10 images), never rely on the first slide or description alone.
- Download all slide image CDN URLs and run multi-image visual inspection across every slide to ensure zero data loss.

## 5. Notion 3-Step Binary File Upload API Workflow
To upload and embed PDFs, `.xlsx` workbooks, or `.md` Markdown files directly into a live Notion page:

1. **Create Upload Slot:**
   ```http
   POST https://api.notion.com/v1/file_uploads
   Headers: Authorization: Bearer <TOKEN>, Notion-Version: 2022-06-28, Content-Type: application/json
   Body: {"filename": "report.md", "content_type": "text/markdown"}
   ```
   Response returns `upload_id` and `upload_url`.

2. **Upload File Bytes:**
   ```http
   POST <upload_url>
   Headers: Authorization: Bearer <TOKEN>, Content-Type: multipart/form-data; boundary=...
   Body: <multipart binary file payload>
   ```

3. **Attach File Block to Notion Page:**
   ```http
   PATCH https://api.notion.com/v1/blocks/<PAGE_ID>/children
   Headers: Authorization: Bearer <TOKEN>, Notion-Version: 2022-06-28, Content-Type: application/json
   Body: {
     "children": [
       {
         "object": "block",
         "type": "file",
         "file": {
           "type": "file_upload",
           "file_upload": {"id": "<upload_id>"},
           "name": "report.md"
         }
       }
     ]
   }
   ```

## 6. Downloadable Deliverable Rule
- When the user asks for a file that is "downloadable" or "in a markdown file", always pair the response with `MEDIA:/absolute/path/to/file` so the platform automatically delivers it as an attachment, and simultaneously upload the file via Notion `/v1/file_uploads`.

## 6. Project Routing & Notion Destinations
- **Project qnt.:** `/data/project_qnt/` -> Pushes to Notion page `qnt.agent` -> `Project qnt. Hub`
- **Project Reach:** `/data/project_reach/` -> Pushes to Notion page `qnt.agent` -> `Project Reach CRM`
