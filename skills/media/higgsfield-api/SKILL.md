---
name: higgsfield-api
description: Generate images/video via the Higgsfield AI platform API.
---
# Using the Higgsfield AI API

This skill provides the correct workflow for the Higgsfield AI API, avoiding common pitfalls.

## Trigger
Use when asked to generate media via the Higgsfield platform.

## Workflow

1.  **Installation & Auth**: Ensure `higgsfield-client` is installed. The client uses `HF_API_KEY` and `HF_API_SECRET` environment variables.

2.  **Find Model Identifier**: **Do not guess model names.** The definitive source for model paths is the official OpenAPI specification. A reference copy is saved in this skill at `references/openapi.json`. The correct identifiers are full API paths (e.g., `/higgsfield-ai/popcorn/auto`).

3.  **Verify Parameters**: Check the `openapi.json` spec for the chosen model to find required arguments and their exact allowed values (e.g., `resolution` must be `'720p'`, not `'2K'`).

4.  **Submit & Handle Errors**: Use the full model path as the application name in `higgsfield_client.subscribe()`. Clearly explain common errors to the user:
    -   `model_not_found`: The path is wrong. Re-check the spec.
    -   `validation_error`: A parameter is wrong. Re-check the spec.
    -   `not_enough_credits`: Inform the user their account needs credits.
