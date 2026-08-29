# Snorlax Labs Music & Animated Video Production Guide

This reference documents the procedural synthesis and rendering workflows for generating exclusive music (Lo-Fi Chill, Cute Trap, Pop Anthems) and animated music videos for Snorlax Labs.

---

## 1. Aesthetic Music Genre Presets

### A. 82 BPM Lo-Fi Chill / Chillhop
- **BPM:** 82 (Relaxed, swung lo-fi hip-hop groove)
- **Chord Progression:** `Dm9` ➔ `G13` ➔ `Cmaj9` ➔ `Am9` (Neo-Soul Jazz)
- **Instrumentation:** Warm Rhodes electric piano with tape wow/flutter (`1.0 + 0.003 * math.sin(t * 4.0)`), vinyl rain crackle ambience, swung boom-bap drums (thumpy 808 kick, rimshot on 2 & 4 with swing delay, 16th swung hi-hats).
- **Vocal Style:** Soft, soothing, rhythmic, poetic bedroom pop.

### B. 140 BPM Cute Trap / Kawaii Future Bass
- **BPM:** 140 (Half-time trap feel)
- **Key:** F# Minor (`F#m` - `D` - `A` - `E`)
- **Sub-Bass:** Saturated 808 sub-bass with exponential pitch drop (`math.tanh(raw * 2.2)` saturation).
- **Chimes & Bells:** 16th-note syncopated Kawaii chime bells and glitchy square/sine plucks with fast exponential decays (`math.exp(-t * 12.0)`).
- **Drums:** Punchy transient kick on beat 1 & 2.5, crisp snappy trap rimshot/snare on beat 3, and rapid 16th/triplet hi-hat rolls on beat 4.

### C. 120 BPM Synth-Pop Anthem (Taylor Swift 1989 Style)
- **BPM:** 120 (Driving synth-pop rhythm)
- **Chord Progression:** `Em` ➔ `C` ➔ `G` ➔ `D`
- **Instrumentation:** Pulsing 8th-note synth bass, 16th-note shimmer arpeggios, driving four-on-the-floor kick, big stadium snare.
- **Vocal Style:** Emotive, breathy, anthemic pop storytelling.

---

## 2. Cinematic Animated Video & Synced Lyrics Pipeline (PIL + FFmpeg)

### Visual Staging & Animation
1. **Aesthetic Sourcing:** Scrape/curate high-res visual frames (e.g. Pinterest/curated graphics).
2. **Camera Motion:** Apply subtle slow cinematic zoom (`zoom = 1.0 + (t / duration) * 0.05`) and pan across frames.
3. **Atmospheric Effects:** Render animated raindrops running down the window, rising coffee steam, and floating dream sparkles.
4. **Time-Synchronized Subtitles:** Map timestamp tuples `(start_sec, end_sec, text)` and render into high-contrast pill badges on every frame so lyrics sync 100% with audio playback.

### FFmpeg Video + Audio Assembly
```bash
ffmpeg -y \
  -framerate 24 \
  -i /tmp/snorlax_lofi_frames/frame_%04d.png \
  -i /data/Snorlax_Labs_Lofi_Chill_Master.mp3 \
  -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p \
  -c:a aac -b:a 320k \
  -shortest \
  /data/Snorlax_Labs_Lofi_Chill_Cinematic_Video.mp4
```

---

## 3. Discord Multi-Attachment Delivery Standard
When delivering music and video packages to Discord, bundle both files in a single multi-part payload:
- `files[0]`: Video (`.mp4`)
- `files[1]`: Master Audio (`.mp3`)
