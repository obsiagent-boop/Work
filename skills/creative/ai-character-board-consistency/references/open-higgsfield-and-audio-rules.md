# Open-Higgsfield AI Architecture, Native Aspect Ratios & Devotional Audio Rules

## 1. Open-Higgsfield AI Architecture & Limitations
- **Repository Reference:** `/data/project_video/open-higgsfield-ai/` (`https://github.com/Autom8AI/Open-Higgsfield-AI`)
- **Structure:** Open-Higgsfield AI is a frontend studio interface built on Vite, Tailwind CSS, and vanilla JavaScript.
- **Backend Mechanics:** It does not run local GPU video generation out-of-the-box on CPU hosts. It defines camera/lens presets (70mm Grand Format, 35mm Natural Prime, Anamorphic, Halation Diffusion) but routes requests to cloud inference APIs (Muapi, Fal.ai, Kling, Wan 2.1).

## 2. Aspect Ratio Invariants (Eliminating 1:1 Square Traps)
- **Problem:** Generating standard 1:1 square assets (`1024x1024`) and cropping into 16:9 widescreen (`1280x720`) or 9:16 vertical cuts crops off crucial anatomy (Mukuta crowns, deity feet, temple backdrops).
- **Rule:**
  - Enforce native 16:9 widescreen (`1280x720` or `1920x1080`) at prompt generation time.
  - Prompt full-body compositions with dedicated breathing room above crowns and below pedestals.

## 3. Devotional Audio Dynamics (Zero Fade-In / Zero Fade-Out)
- **Problem:** Adding `afade=t=in` and `afade=t=out` causes jarring volume fluctuations where the first words are inaudible and the ending feels cut off.
- **Rule:**
  - For traditional, calm, spiritual Telugu voiceovers, use steady, continuous natural gain (`volume=1.2`).
  - Keep pacing measured and serene (-4% to 0% rate) with zero robotic jumps and zero pitch distortion.
