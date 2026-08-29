---
name: higgsfield-ai-api
category: software-development
description: Use for Higgsfield AI. Covers auth, and model discovery.
---

## 1. Summary

This skill provides a reliable workflow for using the Higgsfield AI API, which has several non-obvious steps. It covers finding the correct client, authenticating, discovering the correct model identifiers (which is a major pitfall), and handling common errors.

## 2. Trigger

Use this skill whenever the user asks to generate images or video using the Higgsfield AI platform, or provides Higgsfield API credentials.

## 3. Workflow

### Step 1: Installation

The correct Python client is `higgsfield-client`. The version on PyPI may be outdated or incorrect. Install directly from the official GitHub repository for the latest version.

```bash
pip install git+https://github.com/higgsfield-ai/higgsfield-client.git
```

**Pitfall:** Do not `pip install higgsfield`. This is a different, unrelated library for training ML models and will cause `AttributeError` exceptions.

### Step 2: Authentication

The client authenticates using environment variables. The script must set `HF_API_KEY` (for the key ID) and `HF_API_SECRET` before making any API calls. The library does not use a client object; you call functions directly from the `higgsfield_client` module.

```python
import os
import higgsfield_client

os.environ["HF_API_KEY"] = "your-api-key-id"
os.environ["HF_API_SECRET"] = "your-api-key-secret"

# Now you can call functions like higgsfield_client.subscribe(...)
```

### Step 3: Discovering Model Identifiers (Critical)

This is the most common point of failure. Model identifiers are **not** simple names (e.g., `flux_2`). They are full API paths.

**The only reliable way to get the current list of model identifiers is to fetch and parse the official OpenAPI specification.** Do not trust lists from markdown files or other documentation, as they may be outdated.

1.  **Fetch the OpenAPI spec:**
    ```bash
    curl -o openapi.json https://docs.higgsfield.ai/docs/openapi.json
    ```

2.  **Extract the paths:** The valid model identifiers are the keys in the `paths` object that start with `/higgsfield-ai/`. A Python script can be used to list them. See `scripts/list_models.py` for a reusable implementation.

### Step 4: Making a Request

Use the `higgsfield_client.subscribe` function with the full model path as the first argument.

```python
# Correct usage with a full path identifier
result = higgsfield_client.subscribe(
    '/higgsfield-ai/popcorn/auto',
    arguments={'prompt': 'A test prompt'}
)
```

### Step 5: Handling Errors

-   **`model_not_found`**: The model identifier path is incorrect. Re-run the discovery step to get a fresh list of valid paths from the OpenAPI spec.
-   **Parameter Validation Error** (e.g., `Input should be '720p' or '1600p'`): The model was found, but the arguments are invalid. The error message is usually informative. Consult the OpenAPI spec for the correct schema for that model path to see the valid parameters and their accepted values.
-   **`not_enough_credits`**: This is a user account issue, not a technical one. It means authentication was successful but the account lacks funds. Clearly inform the user that they need to add credits to their Higgsfield account.

## 4. Linked Files

-   **`scripts/list_models.py`**: A Python script to parse the `openapi.json` and print a list of all valid model endpoint paths.
-   **`references/openapi.json`**: A cached copy of the API specification for reference.
