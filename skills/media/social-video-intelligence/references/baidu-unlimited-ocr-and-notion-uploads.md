# Baidu Unlimited-OCR & Notion Binary File Uploads

## Baidu Unlimited-OCR Integration
- **Repo:** `https://github.com/baidu/Unlimited-OCR.git`
- **Location:** `/data/external_repos/Unlimited-OCR`
- **Utility:** One-shot long-horizon document parsing, PDF-to-Markdown validation, table extraction, and multimodal layout analysis.
- **Workflow:** Parse documents with `infer.py` or `@firecrawl/anydoc` to verify that generated PDFs and complex tables retain 100% of structured data without truncation.

## Notion Binary File Uploads Flow (3-Step API)
1. **Initialize Upload:** `POST https://api.notion.com/v1/file_uploads` with `{"filename": "...", "content_type": "application/pdf" | "text/markdown" | "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"}`.
2. **Post File Bytes:** `POST <upload_url>` with `multipart/form-data` containing the raw file bytes.
3. **Attach File Block to Page:** `PATCH https://api.notion.com/v1/blocks/<page_id>/children` with:
```json
{
  "children": [
    {
      "object": "block",
      "type": "file",
      "file": {
        "type": "file_upload",
        "file_upload": {"id": "<upload_id>"},
        "name": "<filename>"
      }
    }
  ]
}
```
