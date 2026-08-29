# Multi-Angle Turnaround Reference Prompts & Fast Audio Pacing Recipes

## 1. Multi-Angle Character Grid Generation Prompt Template
```text
Character model sheet grid, multiple views turnaround of [CHARACTER_NAME]: 
front view, profile view, three-quarter view, emotional expressions, and seated/action posture. 
[DETAILED_ATTIRE_DESCRIPTION], [INTENTIONAL_JEWELRY_AND_PROPS], [LIGHTING_STYLE], 
neutral clean studio background, 8k concept art, 16:9 widescreen format.
```

## 2. Devotional & Regional Audio Pacing Recipes (Edge-TTS / Neural Pipeline)

### A. Calm Traditional Devotional Delivery
- **Voice**: `te-IN-ShrutiNeural` (Telugu Female)
- **Rate**: `-4%` to `-2%` (reverent, spiritual cadence)
- **Pitch**: `+0Hz` (pure natural timbre)
- **Zero Fade In/Out Invariant**: Never apply audio fade-in or fade-out (`afade=t=in/out`) on spiritual narrations — it creates artificial volume drops and cutoffs. Use clean continuous normalization:
```bash
ffmpeg -i raw.mp3 -af "volume=1.2" -c:a libmp3lame -b:a 320k clean.mp3
```

### B. Fast Indian Regional Broadcast Delivery (Bhakthi TV News Style)
- **Voice**: `te-IN-ShrutiNeural` (Telugu Female) or `te-IN-MohanNeural` (Telugu Male)
- **Rate**: `+18%` to `+22%` (rapid broadcast pacing)
- **Pitch**: `-1Hz` (warm acoustic depth)
- **FFmpeg Broadcast Chain**:
```bash
ffmpeg -i raw.mp3 -af "highpass=f=80,lowpass=f=12000,acompressor=threshold=-16dB:ratio=3.5:attack=5:release=50,volume=1.35" -c:a mp3 -b:a 320k mastered.mp3
```

## 3. Open-Higgsfield Dynamic Camera & Lighting FX
To prevent flat 2D picture feel and make scenes volumetric:
1. **Dynamic Camera Choreography**:
   - Shot 1 (Opening/Character Introduction): 35mm Natural Perspective with smooth Zoom-In (`1.00x → 1.08x`).
   - Shot 2 (Environment/Arrival): 24mm Wide Angle with cinematic Zoom-Out (`1.10x → 1.00x`) + lateral Pan.
   - Shot 3 (Transformation/Climax): 50mm Anamorphic with dynamic Light-Push-In.
   - Shot 4 (Coronation/Blessing): Modular 8K Digital with continuous S-curve tracking & camera orbit.
2. **Volumetric Lighting & Particle FX**:
   - Halation Volumetric Rays: Golden hour and divine aura pulses.
   - 24fps Particle Dynamics: Organic falling flower petals with wind drift.
   - Sacred Mountain & Incense Mist: Rising translucent particles.
