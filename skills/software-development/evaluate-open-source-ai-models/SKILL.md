---
name: evaluate-open-source-ai-models
category: software-development
description: Use when asked to run an open-source AI model locally.
---

## 1. Summary

This skill provides a structured workflow for evaluating the feasibility of installing and running an open-source AI model locally. It prioritizes a quick, definitive "yes" or "no" for the user by focusing on the most common blockers: hardware requirements and installation complexity.

## 2. Trigger

Use this skill whenever the user asks if you can install and run a specific open-source AI model locally. This is a common request after discovering that a commercial API is not free.

## 3. Workflow

### Step 1: Find the Official Source

Locate the official open-source repository for the model. This is typically on GitHub or Hugging Face. Use search queries like "[Model Name] open source github" or "[Model Name] hugging face".

### Step 2: Assess the Installation Complexity

Quickly analyze the repository's `README.md` or other top-level documentation to answer one question: **Is this a standalone application or a plugin for a larger framework?**

-   If it's a plugin for a complex framework (e.g., ComfyUI, Automatic1111), the answer is almost always **no**, as setting up the entire framework is a significant task in itself.
-   If it's a standalone application with a `requirements.txt` and a clear entry point, proceed to the next step.

### Step 3: Identify Hardware Requirements (The Key Blocker)

This is the most critical step. Scan the `README.md` for keywords related to hardware:

-   `VRAM`
-   `GPU`
-   `memory`
-   `NVIDIA`
-   `CUDA`

The documentation will almost always specify a minimum amount of **VRAM** (video memory).

-   **If the VRAM requirement is greater than zero, the answer is NO.** State this clearly to the user. Explain that your environment is CPU-based and does not have a dedicated GPU, making it impossible to run the model.
-   Provide the specific VRAM requirement found in the docs (e.g., "The model requires a GPU with at least 32 GB of VRAM.").

### Step 4: Synthesize the Final Answer

Combine the findings into a clear, direct answer for the user.

1.  **Start with a direct "Yes" or "No".** In most cases for large media models, this will be "No".
2.  **State the primary reason.** This is almost always the VRAM requirement.
3.  **Explain the limitation in simple terms.** (e.g., "The model needs a powerful graphics card with X GB of memory, and my environment doesn't have one.")
4.  **If applicable, contrast the open-source version with the API version.** Explain that the API version runs on their powerful hardware, which is what the user is paying for.
5.  **Offer alternatives.** Suggest using cloud GPU providers (like Google Colab, RunPod, or Vast.ai) as the most practical and cost-effective way for the user to run the model without buying expensive hardware.

## 5. Pitfalls

-   **Do not attempt to `pip install` anything until after you have confirmed the hardware requirements.** A successful installation is irrelevant if the model can't be loaded.
-   **Do not get bogged down in software dependencies.** The hardware is the most common and definitive blocker.
-   **Zero Fabrication:** Be direct about your limitations. Do not imply that you *might* be able to run it. If the VRAM requirement isn't met, the answer is a hard no.
