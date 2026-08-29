# Suno AI Ingestion & Subtitle Mastering Pipeline

## Overview
This reference specifies the deterministic method to ingest Suno AI public shared audio links, transcribe/align lyrical timestamps, and composite small, high-contrast, professional subtitles onto animated video loops for mobile and Discord/Telegram playback.

---

## 1. Extracting Raw Audio from Public Suno Shared Links

When a user shares a Suno public link (`https://suno.com/s/<shortcode>` or `https://suno.com/song/<uuid>`):

1. **HTML Inspection & UUID Extraction:**
   Fetch the page HTML and search for UUID patterns:
   ```python
   import urllib.request, re
   url = "https://suno.com/s/<shortcode>"
   req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
   with urllib.request.urlopen(req) as resp:
       html = resp.read().decode('utf-8')
       uuids = re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', html)
   ```

2. **Direct CDN Audio Fetch:**
   Query Suno's CDN endpoints using the discovered UUIDs:
   - `https://cdn1.suno.ai/<uuid>.mp3`
   - `https://audiopipe.suno.ai/?item_id=<uuid>`

---

## 2. Professional Subtitle Typography & Legibility Standard

### Pitfall to Avoid:
- **Never render oversized subtitle bars** (e.g. `FontSize=24+` in vertical videos) that block characters, scenery, or visual focal points.

### Standard Subtitle Styling (Compact, Readable, High-Contrast):
In ASS/SRT formatting or FFmpeg `force_style`:
```ini
FontName=DejaVu Sans
FontSize=10 to 12
PrimaryColour=&H00FFFFFF       ; Pure White text
OutlineColour=&H90000000       ; Semi-translucent crisp black outline
Outline=1.2
BorderStyle=3                  ; Rounded opaque / semi-opaque background box
BackColour=&H50000000          ; 30-40% dark backdrop box for high contrast
Alignment=2                    ; Bottom Center
MarginV=30 to 35               ; Sits cleanly above bottom mobile safe zone
```

---

## 3. Video Looping & Discord Optimization

### Video Looping with `-stream_loop`:
When the audio track is longer than the source animated video clip (e.g. 38s video vs 180s song):
```bash
ffmpeg -y -stream_loop 2 -i source_clip.mp4 -ss 0 -t 75 -i suno_track.mp3 \
  -filter_complex "[0:v]scale=576:1024,subtitles=subtitles.srt:force_style='FontName=DejaVu Sans,FontSize=10,PrimaryColour=&H00FFFFFF,OutlineColour=&H90000000,BorderStyle=3,BackColour=&H50000000,Alignment=2,MarginV=30'[v]" \
  -map "[v]" -map 1:a \
  -c:v libx264 -preset fast -crf 24 -c:a aac -b:a 192k -shortest output_master.mp4
```

### Discord File Size Limits:
- Discord non-Nitro limit is 10MB (or 25MB).
- Using `-crf 24` or `-crf 25` and 192k AAC ensures high visual/audio quality while keeping 1-2 minute clips around 6–8 MB for instant Discord upload.
