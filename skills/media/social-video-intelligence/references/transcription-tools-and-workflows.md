# Video Transcription Tools & Fallbacks Reference

## 1. Web Extraction & Transcriber Services
- **Tactiq.io Transcriber**: Fast transcript extraction from YouTube URLs.
- **Riverside.fm Free Transcriber**: Web-based audio/video transcription supporting drag-and-drop MP4 files.
- **TurboScribe.ai**: Whisper-based transcription with speaker separation.
- **Whisper Web (HuggingFace Xenova)**: Client-side in-browser transcription via WebGPU/WASM for 100% private processing.

## 2. Multi-Layer Video Audit Checklist
When processing short-form content (Instagram Reels, Shorts, TikTok):
1. **Metadata & Caption Pass**: Extract post caption, hashtags, and pinned comments.
2. **Audio / Speech Pass**: Transcribe spoken words across the full duration to catch trailing bonus items.
3. **Cross-Check Pass**: Reconcile numbered lists (e.g. caption says "5 tools" but audio covers 6).
4. **Git Knowledge Vault Commit**: Commit structured markdown under `knowledge_vault/` and push to remote repo.
