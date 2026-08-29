# Higgsfield API & Open-Higgsfield Engineering Reference

## 1. Official Higgsfield Cloud API (`platform.higgsfield.ai`)
- **Headers:**
  - `hf-api-key`: User API Key ID
  - `hf-secret`: User API Secret Key
  - `Content-Type`: `application/json`

### Supported Aspect Ratios & Resolutions:
- **16:9 Widescreen:** `2048x1152` or `1696x960`
- **9:16 Vertical:** `1152x2048` or `960x1696`
- **4:3 Standard:** `2048x1536` or `1536x1152`
- **Square 1:1:** `2048x2048` or `1536x1536`

### Key API Endpoints:
1. `GET /v1/text2image/soul-styles` — List 106+ image styles
2. `GET /v1/motions` — List 121+ video motion presets (`360 Orbit`, `3D Rotation`, `Action Run`)
3. `POST /v1/text2image/soul` — Generate image using Soul model
4. `POST /v1/image2video/dop` — Convert image to 5s cinematic video with motion preset
5. `POST /v1/custom-references` — Upload 1-5 face angles to lock character identity across scenes
6. `GET /v1/job-sets/{id}` — Poll generation job status (`queued`, `in_progress`, `completed`, `failed`)

## 2. Open-Higgsfield AI Architecture
- **Repo:** `https://github.com/Autom8AI/Open-Higgsfield-AI` (or cloned locally at `/data/project_video/open-higgsfield-ai/`)
- **Camera/Lens Presets:** Grand Format 70mm, 35mm natural perspective, Compact Anamorphic, Halation diffusion filter, Swirl bokeh portrait.

## 3. Audio & Voice Rules for Traditional Devotional Videos
- **Pacing:** Traditional spiritual pacing: `-4%` speed, neutral pitch (`+0Hz`).
- **Volume Invariant:** Strictly **ZERO** fade-in and **ZERO** fade-out filters (`afade=t=in`, `afade=t=out`). Maintain clean, steady, uninterrupted acoustic gain throughout.
