# Snorlax Labs Music & Media Production Standard

This reference documents the exact, tested production pipeline for scraping Pinterest media, synthesizing multi-genre musical backing tracks (Lo-Fi Chillhop, Cute Trap, Pop), rendering cinematic animated music videos, and delivering them across Discord and Telegram.

---

## 1. Scraping Pinterest & Multi-Platform Media (`gallery-dl`)

To avoid bot protection and Cloudflare friction on Pinterest, Twitter/X, Instagram, and Reddit, use `gallery-dl`:

```bash
# Scrape Pinterest pin or board to directory:
gallery-dl --dest /data/scraped_media/pinterest_snorlax "https://www.pinterest.com/pin/477803841730159668/"

# Scrape Instagram, Twitter/X, Reddit media:
gallery-dl --dest /data/scraped_media/ "https://x.com/username/status/..."
```

---

## 2. Multi-Genre Audio Backing Track Synthesis (Python Stdlib `wave` + `struct`)

### A. 80-82 BPM Lo-Fi Chillhop (Rhodes + Swung Boom-Bap Drums)
- **Harmonic Progression (Neo-Soul Jazz):** `Dm9` - `G13` - `Cmaj9` - `Am9` or `Bbmaj7` - `Am7` - `Dm9` - `Fmaj7`.
- **Rhodes Timbre:** Sine harmonic overtone layering (`f`, `2f`, `3f`) with slow exponential decay and detuned tape wow/flutter (`1.0 + 0.003 * sin(t * 3.5)`).
- **Drums & Ambience:** 808 low-thump kick, swung rimshot on 2 & 4 (delay +15ms), swung hi-hats, and random vinyl crackle / rain ambience.

### B. 140 BPM Cute Trap / Kawaii Future Bass
- **808 Sub-Bass:** Saturated sub-sine with exponential pitch drop (`f_now = root * 0.5 + 35 * exp(-t * 25)`) and `tanh(raw * 2.2)` saturation.
- **Chimes:** 16th-note plucks with bell harmonics (`f`, `2f`, `3.5f`).
- **Drums:** Half-time snare on beat 3, punchy four-pole kicks on 1 and 2.5, and 16th/triplet hi-hat rolls.

### C. 120 BPM Taylor Swift Style Synth-Pop (1989 / Cruel Summer)
- **Progression:** `Em` - `C` - `G` - `D`.
- **Instrumentation:** Pulsing 8th-note sawtooth synth bass, 16th-note shimmer arpeggios, driving 4-on-the-floor kick on every beat, big reverb snare on 2 & 4.

---

## 3. Emotive Vocals & Studio FFmpeg Mastering

Generate vocals with specific emotional pacing matching the genre BPM, then mix:

```bash
ffmpeg -y \
  -i vocals.ogg \
  -i backing.wav \
  -filter_complex "[0:a]volume=1.4,equalizer=f=2800:t=q:w=1.2:g=2.8,aecho=0.8:0.6:90:0.45[voc];[1:a]volume=0.72,lowpass=f=7200[bg];[voc][bg]amix=inputs=2:duration=longest:dropout_transition=3,alimiter=limit=0.95[out]" \
  -map "[out]" \
  -b:a 320k \
  output_master.mp3
```

---

## 4. Cinematic Video Animation with Synced Subtitles (PIL + FFmpeg)

1. **Camera Movement:** Subtle continuous zoom (`zoom = 1.0 + (t/dur)*0.05`) and slow trigonometric pan.
2. **Atmospheric Layers:** Overlay animated raindrops, floating dust motes/sparkles, and rising coffee steam.
3. **Synchronized Subtitles:** Draw semi-transparent pill container at bottom screen with active lyric slice corresponding to exact audio timestamps.
4. **Encoding:**
```bash
ffmpeg -y -framerate 24 -i /tmp/frames/frame_%04d.png -i output_master.mp3 -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p -c:a aac -b:a 320k -shortest output_video.mp4
```

---

## 5. Discord Multi-Attachment Delivery Payload

Upload both the `.mp4` video and `.mp3` master audio in a single `multipart/form-data` REST payload to Discord channels:

```python
body.append(f'--{boundary}\r\nContent-Disposition: form-data; name="payload_json"\r\nContent-Type: application/json\r\n\r\n{json_text}\r\n'.encode('utf-8'))
body.append(f'--{boundary}\r\nContent-Disposition: form-data; name="files[0]"; filename="video.mp4"\r\nContent-Type: video/mp4\r\n\r\n'.encode('utf-8') + video_bytes + b'\r\n')
body.append(f'--{boundary}\r\nContent-Disposition: form-data; name="files[1]"; filename="audio.mp3"\r\nContent-Type: audio/mpeg\r\n\r\n'.encode('utf-8') + audio_bytes + b'\r\n')
body.append(f'--{boundary}--\r\n'.encode('utf-8'))
```
