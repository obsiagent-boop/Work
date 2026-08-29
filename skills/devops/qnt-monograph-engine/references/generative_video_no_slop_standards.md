# 🎬 Generative Video Production & No-Slop Synthesis Engine

## 1. Multi-Tier Generative Video Execution
When producing professional cultural, commercial, or creative video deliverables:
- **Deity & Character Visuals:** Use Google Gemini 2.5/3.1 Image Generation endpoints (`gemini-2.5-flash-image:generateContent`) with structured JSON prompts to generate high-resolution, photorealistic 4K frames.
- **Audio & Vocal Narration:** Synthesize natural, regional multilingual voiceovers (e.g. `te-IN-ShrutiNeural` for Telugu, `en-IN-NeerjaNeural` for Indian English) with custom cadence and pitch modulation via Edge TTS / ElevenLabs.
- **Master Concat & Subtitle Burn:** Avoid sequential single-frame PNG encoding loops that cause timeouts; use high-performance FFmpeg clip generation + demuxer concatenation with burned-in ASS/SRT subtitles and high-contrast letterboxing.
- **Reels & Multi-Format Delivery:** Render parallel 16:9 landscape master cuts and 9:16 vertical Instagram Reels cuts (`crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=720:1280`).

## 2. "No AI Slop" Quality Standards
- **Zero Robotic Voice Artifacts:** Enforce natural neural regional voices with humanized pacing and tone modulation.
- **Visual Consistency:** Anchor characters across shots using consistent lighting, palettes, and reference elements rather than disconnected stock visuals.
- **Subtitles:** Elegant, small, readable text (`FontSize=10–15`) with semi-transparent background pills that never obstruct primary character framing.
