---
name: social-video-intelligence
description: "Transcribe and summarize IG Reels, YouTube, and MP4 videos."
platforms: [linux, macos, windows]
---

# Social Video Intelligence & Multi-Layer Transcription

## When to use

Use when the user shares any social media video URL (Instagram Reels, YouTube Shorts/Videos, TikTok, X video) or local video file (.mp4, .mov) and asks for transcripts, summaries, key takeaways, action points, or blog posts.

## Core Mandates & Multi-Layer Inspection Standard

1. **Cross-Examine Spoken Audio AND Captions**: Never rely solely on video caption/description text or auto-generated OCR. Creators frequently present bonus tools, 6th recommendations, surprise takeaways, or exclusive promo codes in the spoken audio that are truncated or omitted in post captions. Always cross-verify:
   - Spoken audio track / transcript
   - On-screen visual overlays & slides
   - Description / caption text & pinned comments
2. **Standard Output Structure**:
   - Complete Transcribed Content (with all items & bonuses)
   - Timestamped Topic / Segment Breakdown
   - Key Takeaways & Action Points (with comparison matrices where applicable)
   - Ready-to-Publish Long-Form Blog Post / Social Thread
3. **Automated Knowledge Vault Sync**: Persist extracted transcripts and analysis to the project knowledge vault (e.g. `knowledge_vault/`), ensure git authorship is set explicitly to `obsiagent-boop` (`obsi.agent@gmail.com`), and commit/push to the active integrated Git repositories (`personal-agent-os`, `project-anya`). Also support document generation & archiving via AnyDoc and ReportLab.

## Video Processing Workflow

### 1. YouTube Extraction
- Primary: Extract via `youtube-transcript-api` or video metadata tools.
- Fallback: Use web extraction on transcript tools or download audio with `yt-dlp` for local transcription.

### 2. Instagram & Social Media Reels
- Extract post metadata, descriptions, and comments via web tools or direct HTTP requests.
- Extract audio stream / video frames to verify full spoken audio against text description.

### 3. Audio / Video File Transcription
- Use `ffmpeg` to extract audio (`ffmpeg -i video.mp4 -vn -ar 16000 -ac 1 audio.wav`).
- Transcribe via local Whisper, Whisper Web, or integrated speech models.

## Pitfalls & Best Practices

- **Missing Bonus Items**: Social media creators routinely use hooks like "5 repos..." but speak about a 6th bonus tool at the end. Always listen through the end of the media track.
- **Dark PDF Generation & Visual Verification**: When generating dark-mode monographs or branded deliverables, use **WeasyPrint with CSS Paged Media** (`@page { background-color: #000; }`) to avoid ReportLab canvas two-pass overdraw bugs. Always render sample pages to PNG (`pymupdf`) and visually confirm before delivery.
- **AnyDoc 14-Format Parsing**: Use `@firecrawl/anydoc` CLI or `firecrawl-anydoc` Python library to seamlessly convert Word (`.docx`), PowerPoint (`.pptx`), Excel (`.xlsx`), and PDF into clean GitHub-Flavored Markdown.
- **Datacenter IP Blocks**: Major video platforms throttle or block direct cloud/datacenter IPs. Always have secondary extraction fallbacks (web transcript scrapers, metadata inspection, user file uploads).
- **Format Integrity**: Keep code blocks, links, and financial/technical terms strictly verbatim.
- **Multi-Slide Carousel Zero-Loss Extraction**: For multi-image/carousel posts (`/p/...` with `img_index`), download and inspect ALL carousel slide images (slides 1 through 10) individually using `vision_analyze` / OCR. Never rely on the cover slide or snippet preview alone, as critical code, tools, and workflows span across subsequent slides. Cross-examine:
  1. Primary caption text & metadata (via embed or API).
  2. scontent CDN image URLs from unescaped embed HTML or oEmbed responses.
  3. Cover graphics and embedded carousel text across every slide.
  4. Cross-platform sync threads (Threads, X/Twitter, Bluesky) for exact text replicas when direct CDN extraction is rate-limited.
- **Downloadable Deliverable Standard**: Whenever the user requests downloadable files or outputs (PDF, XLSX, Markdown), always include `MEDIA:/absolute/path/to/file` in the final response so the platform delivers native attachments directly, and upload binary files (including `.md` files) directly to the target Notion pages via the 3-step `/v1/file_uploads` flow.
- **Instagram Extraction Fallback**: If `web_extract` on a direct Instagram URL times out or is blocked, immediately fetch `https://www.instagram.com/<path>/embed/captioned/` or parse `scontent` CDN image URLs in Python to extract all carousel slides and captions without missing data.
- **Autonomous Project Management & Direct Notion Uploads**: Route transcripts, code, and monographs to their designated project directories (`/data/project_qnt/` for quant research, `/data/project_reach/` for B2B outreach & ad monetization) and dispatch updates to the integrated Notion workspace. Use the 3-step Notion `/v1/file_uploads` API flow to attach binary PDFs, Excel workbooks, and Markdown files directly onto live Notion pages. (See `references/ad-monetization-and-notion-uploads.md` and `references/baidu-unlimited-ocr-and-notion-uploads.md` for full implementation details).
