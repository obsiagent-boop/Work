---
name: ai-character-board-consistency
description: "Use when building multi-view character grids for AI video."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [character-consistency, turnaround-grid, model-sheet, multi-shot-video, video-generation, creative]
---

# AI Character Board Consistency & Multi-Shot Video Architecture

Framework for generating immutable character identities across long-form video, storyboards, and multi-scene films without facial, wardrobe, or physiological drift.

## Core Architectural Invariants

### 1. The Multi-View Turnaround Grid Principle
- **Single reference images fail**: A single perspective leaves 80% of volumetric geometry ambiguous, guaranteeing that character identity will drift as soon as camera angles or lighting change.
- **9-Angle Turnaround Model Sheets**: Before prompting scenes, generate a dedicated 16:9 character turnaround sheet containing:
  1. Frontal Neutral (eye-level)
  2. 3/4 Left and 3/4 Right perspectives
  3. 90-degree Profiles (Left/Right)
  4. Emotional Expression Grid (Joy, Serenity, Wrath, Reverence)
  5. Isolated Costume, Weapon, and Jewelry close-ups.

### 2. Multi-Shot Story Sequencing Pipeline
1. **Model Sheet Generation**: Build turnaround sheets from scratch for each hero subject (e.g., Lord Ganesha, Lord Shiva, Goddess Parvati).
2. **Subject Conditioning**: Pass the model sheet as the canonical structural anchor into the image/video diffusion model.
3. **Sequential Narrative Framing**: Prompt consecutive narrative moments inheriting the exact costume, color palette, and anatomical anchors from the character board.
4. **Widescreen Framing & Zoom Invariant**:
   - **Zero Over-Zooming**: Strictly enforce native 16:9 uncropped canvas (`1280x720` / `1920x1080`) during generation.
   - **Full-Body & Environment Preservation**: Prompt wide shots that keep full character anatomy, background temples, and mountain peaks in frame without aggressive edge-cropping.
   - **Dynamic Motion vs Static Slides**: Apply subtle sub-3% camera push-ins or animated atmospheric light particles (divine motes, subtle light glows) so visuals feel alive rather than like static picture slideshows.
### 3. Real Neural Video Diffusion vs 2D Image Slideshows
- **The 2D Pan/Zoom / Wave Warp Trap**: Panning, zooming, crossfading, or synthetic ripple/wave distortions on static 2D images is **NOT** video generation. Users immediately identify it as a slideshow with superficial effects ("AI slop") and will reject it. True video requires skeletal and physical character motion interacting with the scene.
- **Standalone GPU Compute (Google Colab T4) vs Ephemeral Tunnels**:
  - Do not rely on ephemeral `gradio.live` tunnels when streaming batches from mobile or background sessions; browser tab suspensions drop the tunnel mid-generation.
  - **Standalone Batch Recipe**: Run self-contained batch diffusion scripts directly on the GPU instance (e.g. `CogVideoX-2b` with `expandable_segments:True`, `enable_model_cpu_offload()`, `enable_vae_tiling()`, `enable_vae_slicing()`), exporting to an auto-downloading `.zip` bundle.
  - **PyTorch OOM Guardrail on T4 GPU**: Never call `.to("cuda")` on the pipeline directly when loading CogVideoX-2b on 15GB T4 GPUs. Instead, load in `torch_dtype=torch.float16` and allow `pipe.enable_model_cpu_offload()` to manage sub-layer VRAM offloading dynamically (keeping VRAM < 6GB). If previous runs leave VRAM fragments, instruct a runtime restart before launch.
- **Audio Delivery & Mastering Invariants**:
  - **Zero Audio Fade In/Out**: Devotional and traditional broadcast speech requires continuous, steady volume normalization (`volume=1.2`) without artificial fade-in or fade-out effects that clip opening/closing syllables.
  - **Authentic Traditional Voice Tone**: Use serene, unaccelerated or slightly calm rates (`-4%` on regional neural engines) for sacred/traditional storytelling.
- **Prompt Architecture & Style Locking**:
  - Prepend an explicit **Style Lock** (e.g., *Traditional Indian miniature/mural aesthetic, terracotta & gold palette, visible brushwork, realistic facial asymmetry, natural fabric physics, 24fps filmic motion*) to every multi-shot prompt to lock character identities across scenes.
- **Standalone Markdown Specs for User Execution**: When providing code/specs for external execution on Google Colab or remote GPUs, always write and deliver the complete, zero-loss runnable script as a standalone `.md` file with clear step-by-step instructions.
- **Higgsfield AI & Open-Higgsfield API Protocol**:
  1. *Higgsfield Cloud API Integration*: Higgsfield operates through `https://platform.higgsfield.ai/v1` with headers `hf-api-key` and `hf-secret`.
     - Image Generation (Soul): `POST /v1/text2image/soul` with exact supported aspect resolutions (`2048x1152` for 16:9, `1152x2048` for 9:16).
     - Video Motion Generation (DoP): `POST /v1/image2video/dop` with `input_images` array and `motion_id`.
     - Character References: `POST /v1/custom-references` for reusable character IDs across scenes.
  2. *Open-Higgsfield AI Local Engine*: Open-Higgsfield AI (`https://github.com/Autom8AI/Open-Higgsfield-AI`) contains camera/lens UI presets (Grand Format 70mm, 35mm natural perspective, halation diffusion, swirl bokeh).
- **True Neural Video & Motion Physics Requirements**:
  1. *Dynamic Camera Movements (Open-Higgsfield Pattern)*: Use real cinematography physics — 35mm natural push-ins, 24mm wide angle zoom-outs revealing environments, 50mm anamorphic pushes, and continuous S-curve orbits.
  2. *Living Volumetric & Lighting FX*: Apply halation volumetric rays, swirl bokeh, dynamic rising mountain mist, and 24fps wind-driven particle physics (falling flower petals) across every frame so scenes feel alive.
  3. *Audio Quality & Natural Continuity*: Devotional/spiritual voiceovers must remain steady, calm, and traditional with **zero audio fade-ins or fade-outs** (which cause jarring cutoffs or volume drops).
  4. *Colab / Zero-GPU Execution*: When running remote diffusion servers on free Google Colab (T4 GPUs), mobile browser tab suspensions kill temporary Gradio tunnels. Use standalone batch rendering that generates all shots directly to a zip archive on the local GPU instance without live tunnel drops.
   - **Fast-Paced Regional Broadcast vs Spiritual Devotional Cadence**: For Indian regional news/announcements, accelerate speech rate by +18% to +22%. When traditional, spiritual, calm devotional tone is requested, use normal to slightly slowed rate (-4% to 0%) with steady, respectful, continuous volume.
   - **Zero Audio Fade-In/Out Traps**: Never apply artificial audio fade-in or fade-out filters (`afade=t=in`, `afade=t=out`) to devotional/spiritual voiceovers. Maintain clean, consistent, continuous natural gain from the first word to the final blessing.
   - **Aspect Ratio Invariants (Native 16:9 vs 1:1 Traps)**: Always generate images and master video frames in native target ratios (`1280x720` / `1920x1080` for 16:9, or `720x1280` / `1080x1920` for 9:16 vertical). Never generate square 1:1 (`1024x1024`) images and crop them down, which truncates head crowns, jewelry, and background environments.
   - **Open-Higgsfield AI Architecture**: Understand that open-source repositories like Open-Higgsfield AI provide frontend studio architecture and camera/lens presets (e.g. 70mm Grand Format, 35mm natural perspective, halation diffusion, swirl bokeh), but require underlying GPU video inference pipelines (CogVideoX / Wan2.1 / Kling) for 24fps temporal motion.
   - **Acoustic Mastering**: Apply multiband compression (`threshold=-16dB:ratio=3.5:attack=5:release=50`) and highpass filtering (`80Hz-12kHz`) for TV studio clarity.
   - **Zero Subtitle Clutter**: Avoid obstructive burned-in subtitle boxes unless explicitly requested; allow 4K cinematics to remain pristine.
   - **Multi-Ratio Delivery**: Produce parallel 16:9 Landscape Masters and 9:16 Vertical Reels simultaneously.
   - **Strict Document-Source Grounding**: When a user provides project architecture as a Markdown (`.md`) specification alongside binary document files (e.g. PDF/DOCX resumes), strictly prioritize and read the native Markdown document using plain text file tools; do not attempt binary PDF image extraction on unrelated document attachments when the user directs to use the `.md` source file exclusively.

## Reference Files
- [Turnaround and Audio Recipes](references/turnaround-and-audio-recipes.md) — 9-angle model sheet prompts, TTS rates, and mastering settings.
- [Free Colab GPU Bridge & Zero-GPU Video Recipes](references/free-colab-gpu-bridge.md) — Free Google Colab T4 GPU tunnel setup, Gradio client integration, and zero-GPU troubleshooting.
- [Real-Time 3D Camera Angles, Open-Higgsfield & Native Telugu Audio Protocols](references/realtime-camera-and-audio-protocols.md) — Homography perspective transforms, volumetric fluid remapping, zero fade-in/out audio rules, and Higgsfield platform API schemas.
