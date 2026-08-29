# Real-Time 3D Camera Angles, Open-Higgsfield & Native Telugu Audio Protocols

## 1. Real-Time 3D Perspective Transformations (DOT3 Verified Motion)
To eliminate flat 2D pans and deliver true cinematic depth:
- **Perspective Homography Warp (`cv2.warpPerspective`)**:
  - **Horizontal Panoramic Orbit**: Tilt source corner vertices dynamically (`±14°` angle swing) simulating a rotating 35mm camera track.
  - **Low-Angle Heroic Crane-Up**: Elevate perspective coordinates upward (`+20-25px`) with widening bottom field-of-view.
  - **High-Angle Dutch Tilt**: Rotate corner coordinates with angle torque (`15-20°`) for dramatic confrontations.
  - **360° Spherical Orbit**: Modulate x/y coordinates cyclically with sine/cosine trigonometric sweeps.

## 2. Dynamic Volumetric & Particle Dynamics (24fps Continuous Living Motion)
- **Mesh Grid Remapping (`cv2.remap`)**: Apply non-linear sinusoidal coordinate displacement for cloth rippling, hair motion, and wind physics.
- **Volumetric Aura Pulses**: Radial Gaussian-blurred light maps simulating glowing celestial energy.
- **24fps Particle Dynamics**:
  - Drifting marigold flower petals calculated with gravity, angle rotation, and horizontal wind sway.
  - Rising sacred incense and mountain mist circles with continuous vertical drift.

## 3. Traditional Telugu Devotional Audio Rules (Zero Fade-In / Zero Fade-Out)
- **Voice Profile**: Traditional, calm, spiritual female Indian Telugu cadence (Edge-TTS `te-IN-ShrutiNeural` at `-4%` speed, `+0Hz` natural pitch).
- **Zero Fade Traps**: Never apply `afade=t=in` or `afade=t=out`. The volume must remain solid, natural, and continuous from the first syllable to the closing blessing.
- **Acoustic Mastering**: Clean gain (`volume=1.2`) with highpass (`60Hz`) and lowpass (`14000Hz`) filters to avoid sudden audio drops.

## 4. Higgsfield Cloud API (`platform.higgsfield.ai/v1`)
- **Headers**: `hf-api-key: <KEY>`, `hf-secret: <SECRET>`
- **Supported Resolutions (Soul Text-to-Image)**:
  - 16:9 Landscape: `2048x1152`, `1696x960`
  - 9:16 Vertical: `1152x2048`, `960x1696`
  - Square: `1536x1536`, `2048x2048`
- **Video Motion Generation (DoP Image-to-Video)**: `POST /v1/image2video/dop` with `input_images` array and `motion_id`.
- **Character Consistency (Soul Custom Reference)**: `POST /v1/custom-references` to lock character geometry across shots.

## 5. CogVideoX-2B Colab Standalone Execution & Zero-OOM Pipeline
- **The OOM Root Cause**: Calling `.to("cuda")` immediately after `from_pretrained()` attempts to load the full ~14GB model into VRAM at once, crashing with `OutOfMemoryError: CUDA out of memory` on Google Colab T4 GPUs.
- **The Zero-OOM Fix**: Load in `torch_dtype=torch.float16` WITHOUT `.to("cuda")`. Configure `pipe.enable_model_cpu_offload()` + `pipe.enable_vae_tiling()` + `pipe.enable_vae_slicing()` to keep active VRAM consumption under **6 GB**.
- **PyTorch Memory Allocator**: Set `os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"` before importing torch to prevent memory fragmentation.
- **Auto-Zipping & Direct Download**: Batch-render all narrative shots into an output folder and export via `zip -j /content/generated_movie_clips.zip /content/movie_shots/*.mp4` followed by `files.download()`.
- **Style Lock Prepending**: Always prepend an explicit **Style Lock** string to every multi-shot prompt to maintain character facial structure, attire, lighting, and palette without drift across shots.
