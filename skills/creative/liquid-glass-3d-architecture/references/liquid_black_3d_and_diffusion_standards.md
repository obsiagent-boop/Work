# Liquid Black 3D & Dribbble-Grade Cinematic Video Standards

## 1. Core Visual Architecture (Liquid Obsidian Black & Pure White)
When generating video content and animated UI representations for `qnt.`:
- **Canvas Base:** Pure Liquid Obsidian Black (`#02040A` -> `#000000`). Never use flat gray or muddy darks.
- **Optical Glass:** MeshPhysicalMaterial (`transmission: 0.98, ior: 1.54, thickness: 3.5, roughness: 0.02`) with high specular clearcoat (`1.0`).
- **Dynamic Chromatic Refraction:** Always place moving, animated aurora/caustic light sources (Electric Cyan `#06B6D4`, Emerald `#34D399`) *directly behind* the glass elements to demonstrate physical optical refraction.
- **Typography:** Pure crisp white (`#FFFFFF`) and titanium silver (`#E2E8F0`) using **Inter Variable** (`file:///data/fonts/InterVariable.ttf`). 100% high-contrast legibility.
- **Engraved Branding:** Official `qnt.` monogram and institutional badges engraved in-frame on frosted glass pills with specular top sheen lines.

## 2. CogVideoX-2B / Diffusion Zero-OOM Protocol
- **The Issue:** `.to("cuda")` immediately consumes 14.5GB VRAM and crashes free 15GB T4 GPUs.
- **The Solution:** Load in FP16 and enable `pipe.enable_model_cpu_offload()` + `pipe.enable_vae_tiling()` + `pipe.enable_vae_slicing()`. This keeps VRAM under 6GB on 15GB GPUs with zero CUDA Out-Of-Memory errors.

## 3. Persistent Loop & Refinement Standard
- Continuously construct, verify, and loop sequences at full computing power.
- Zero cheap placeholder graphics or synthetic 2D wave warps when 3D neural or 3D WebGL projective geometry is required.
