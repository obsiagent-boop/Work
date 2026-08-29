# Free Colab GPU Bridge & Zero-GPU Video Recipes

## 1. Free Dedicated Google Colab T4 GPU Bridge Setup
When external paid video APIs (Fal.ai, Higgsfield, Lumeflow) have zero balance and local CPU cannot run 14B diffusion models, launch a free dedicated inference tunnel via Google Colab.

### Mobile-Safe & Memory-Optimized Colab Script
```python
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

!pip install diffusers transformers accelerate torch gradio -q

import torch, gc, gradio as gr
from diffusers import CogVideoXPipeline
from diffusers.utils import export_to_video

model_id = "THUDM/CogVideoX-2b"
pipe = CogVideoXPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

pipe.enable_model_cpu_offload()
pipe.enable_vae_tiling()
pipe.enable_vae_slicing()

def gen(prompt):
    torch.cuda.empty_cache()
    gc.collect()
    frames = pipe(prompt=prompt, num_inference_steps=30, num_frames=49, guidance_scale=6.0).frames[0]
    out = "/content/video.mp4"
    export_to_video(frames, out, fps=8)
    return out

gr.Interface(fn=gen, inputs=gr.Textbox(), outputs=gr.Video()).launch(share=True)
```

### Critical Implementation Rules & Pitfalls:
1. **PyTorch VRAM Allocation (`PYTORCH_CUDA_ALLOC_CONF`)**:
   - Set `os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"` before importing torch to prevent memory fragmentation on Colab's 15GB T4 GPU.
   - Always invoke `pipe.enable_vae_tiling()` and `pipe.enable_vae_slicing()` to keep decode memory footprint under 6GB VRAM.
   - Call `torch.cuda.empty_cache()` and `gc.collect()` before every generation loop.
2. **Mobile Copy-Paste Formatting**:
   - When providing code to mobile users, avoid multi-line string prompts or long wrapped comments. Mobile clipboard tools frequently split strings across newlines, causing `SyntaxError: unterminated string literal`.
   - Provide ultra-compact, pre-formatted copy blocks without trailing multi-line strings.
3. **Gradio Public URL Ephemeral Lifecycles & Session Disconnections**:
   - Every time a Colab notebook cell is restarted or re-run, Gradio generates a **brand new unique random sub-domain** (e.g. `https://[NEW_HASH].gradio.live/`). Old links become immediately invalid with `ValueError: Could not fetch config for https://...`.
   - **Mobile Tab Sleep & Keep-Alive**: When running Colab from a mobile device or backgrounded browser tab, mobile operating systems aggressively suspend JavaScript execution after 15–30 seconds of inactivity, which severs the SSH tunnel and closes the Gradio share link. Users must keep the browser tab in the foreground while rendering, or launch with background keep-alives.
   - **Colab GPU Compute Budgeting**: Free-tier Google accounts receive ~4–6 continuous hours per compute session and a rolling ~12 hours per week allocation before hitting cooldown.

## 2. Autonomous Standalone Colab Video Batch Generator (Tunnel-Free Architecture)
When mobile users experience repeated tunnel dropouts due to browser app-switching, avoid remote streaming tunnels (`gradio.live`) altogether. Provide a standalone Colab batch generation script that runs all scene prompts consecutively on the Colab T4 GPU, saves them to disk, and packages them as a 1-click `.zip` download (`ganesha_movie_clips.zip`).

```python
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

!pip install diffusers transformers accelerate torch -q

import torch, gc
from diffusers import CogVideoXPipeline
from diffusers.utils import export_to_video

model_id = "THUDM/CogVideoX-2b"
pipe = CogVideoXPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")
pipe.enable_model_cpu_offload()
pipe.enable_vae_tiling()
pipe.enable_vae_slicing()

os.makedirs("/content/movie_shots", exist_ok=True)

# Define scenes list: (filename, prompt)
scenes = [
    ("shot01.mp4", "Cinematic prompt 1..."),
    ("shot02.mp4", "Cinematic prompt 2...")
]

for idx, (fname, p_text) in enumerate(scenes):
    out_file = os.path.join("/content/movie_shots", fname)
    if os.path.exists(out_file): continue
    torch.cuda.empty_cache(); gc.collect()
    frames = pipe(prompt=p_text, num_inference_steps=28, num_frames=49, guidance_scale=6.0).frames[0]
    export_to_video(frames, out_file, fps=8)

!zip -r /content/movie_clips.zip /content/movie_shots
from google.colab import files
files.download('/content/movie_clips.zip')
```

## 3. Client Side Integration in Python (via `gradio_client`)
```python
from gradio_client import Client
import shutil

colab_url = "https://xxxx.gradio.live"
client = Client(colab_url)

result = client.predict(
    prompt="Lord Ganesha raising hand in divine blessing, flowing golden silk, falling flowers, cinematic 24fps video",
    api_name="/predict"
)

out_video_path = result["video"]
shutil.copy(out_video_path, "/data/rendered_video.mp4")
```
