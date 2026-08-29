# CogVideoX-2B Standalone Diffusion on Free Google Colab (T4 GPU)

## 1. Prerequisites & Environment Setup
- Free Google Colab Notebook with **T4 GPU** enabled (`Runtime -> Change runtime type -> T4 GPU`).
- Run `Runtime -> Restart session` to purge residual VRAM from previous runs.
- Environment variable to prevent PyTorch VRAM fragmentation:
  ```python
  import os
  os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
  ```

## 2. Dependencies
```bash
!pip install diffusers transformers accelerate torch -q
```

## 3. High-Efficiency Pipeline Setup (Zero-OOM Recipe)
**Crucial Fix:** Never call `.to("cuda")` on the pipeline object. Let `enable_model_cpu_offload()` dynamically move layers to GPU on demand, keeping VRAM consumption under 5.8 GB on the 15 GB T4 GPU.
```python
import torch, gc
from diffusers import CogVideoXPipeline
from diffusers.utils import export_to_video
from google.colab import files

model_id = "THUDM/CogVideoX-2b"
pipe = CogVideoXPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16
)

pipe.enable_model_cpu_offload()
pipe.enable_vae_tiling()
pipe.enable_vae_slicing()
```

## 4. Master Style Lock Pattern
Prepend a global visual anchor to all scene prompts:
```python
STYLE_LOCK = (
    "Traditional Indian miniature-meets-cinematic style, Maratha and Deccan mural influence, "
    "warm terracotta and gold palette, hand-painted texture with visible brushwork, deep indigo night skies, "
    "temple oil-lamp lighting, realistic asymmetry in faces and drapery, natural fabric physics on silk and cotton, "
    "weathered stone and brass textures, 24fps filmic motion, static or slow deliberate camera moves only, "
)
```

## 5. Standalone Batch Execution Loop (Zero Ephemeral Tunnel Drops)
```python
os.makedirs("/content/ganesha_master_film", exist_ok=True)

for idx, (filename, prompt_text) in enumerate(scenes):
    out_file = os.path.join("/content/ganesha_master_film", filename)
    torch.cuda.empty_cache()
    gc.collect()
    
    video_frames = pipe(
        prompt=prompt_text, 
        num_inference_steps=28, 
        num_frames=49, 
        guidance_scale=6.0
    ).frames[0]
    
    export_to_video(video_frames, out_file, fps=8)

!zip -j /content/ganesha_full_festival_movie.zip /content/ganesha_master_film/*.mp4
files.download('/content/ganesha_full_festival_movie.zip')
```
