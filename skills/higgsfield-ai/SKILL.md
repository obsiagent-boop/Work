---
name: higgsfield-ai
description: Generate images and video with the Higgsfield AI API.
---

## 1. Trigger
Use this skill when asked to interact with the Higgsfield AI API for tasks like image or video generation.

## 2. Workflow

### Step 1: Install the Correct Client
The correct Python library is `higgsfield-client`. The similarly named `higgsfield` package on PyPI is for an unrelated machine learning framework and should not be used.

Install the correct client directly from the official GitHub repository to avoid dependency issues and get the latest version.

```bash
pip uninstall -y higgsfield || true
pip install git+https://github.com/higgsfield-ai/higgsfield-client.git
```

### Step 2: Set Authentication
The client uses environment variables for authentication. Set them before running your script.

*   `HF_API_KEY`: Your API Key ID.
*   `HF_API_SECRET`: Your API Key Secret.

```python
import os

os.environ["HF_API_KEY"] = "YOUR_API_KEY_ID"
os.environ["HF_API_SECRET"] = "YOUR_API_KEY_SECRET"
```

### Step 3: Find the Correct Model Path
**CRITICAL:** Models are not identified by simple names (e.g., `flux_2`). They are identified by their full API path (e.g., `/higgsfield-ai/popcorn/auto`). Documentation or markdown files can be outdated. The only reliable way to get a current list of valid model paths is by fetching and parsing the official OpenAPI specification.

A copy of this specification is saved in `references/openapi.json`. Use it to find the correct path for the desired model under the `paths` key.

**Example script to find a model path:**
```python
import json

# In a real session, this would be `skill_view('higgsfield-ai', file_path='references/openapi.json')`
with open('skills/higgsfield-ai/references/openapi.json', 'r') as f:
    spec = json.load(f)

for path in spec['paths']:
    if path.startswith('/higgsfield-ai/popcorn/auto'):
        print(f"Found model path: {path}")
        # Use this path in the API call
        break
```

### Step 4: Make the API Call
Use the `higgsfield_client.subscribe` function with the full model path. Be prepared to handle parameter errors, as arguments like `resolution` are specific to each model.

```python
import os
import higgsfield_client

# Set credentials
os.environ["HF_API_KEY"] = "e41d9020-2d1f-478e-a22d-d092853eca18"
os.environ["HF_API_SECRET"] = "e48b770d7016c81a9aafa3fb2ea61011d27e42ad134769b4ce4e50c2b5eba4ff"

try:
    # Use the full, correct path from the OpenAPI spec
    model_path = '/higgsfield-ai/popcorn/auto'
    
    # Use parameters valid for this specific model
    result = higgsfield_client.subscribe(
        model_path,
        arguments={
            'prompt': 'A serene lake at sunset with mountains',
            'resolution': '720p',  # Valid values are '720p' or '1600p' for this model
            'aspect_ratio': '16:9'
        }
    )
    print("Successfully received result:")
    print(result)

except Exception as e:
    print(f"An error occurred: {e}")

```

## 3. Pitfalls
- **Wrong Package:** Do not `pip install higgsfield`. The correct package is `higgsfield-client`.
- **Incorrect Model Name:** Simple model names like `flux_2` or `seedream_v4_5` will result in a `model_not_found` error. You MUST use the full API path from the OpenAPI spec.
- **Model-Specific Parameters:** Arguments are not universal. An argument like `resolution: '2K'` might work for one model but fail on another. Check the API error messages for details on valid parameters.
- **`not_enough_credits` Error:** This error means authentication was successful, but the user's account lacks the funds to perform the operation. This is a user-side issue to be resolved in their Higgsfield Cloud dashboard.
