# Josh Prompt Analyzer

An AI-powered prompt analyzer that helps users understand, improve, and refine their prompts.

## What It Does

The user enters a prompt and the AI analyzes:

* **Goal** : Is the objective clear?
* **Context** : Is enough information provided?
* **Specificity** : How specific is the request?
* **Missing Information** : What details could improve it?
* **Feedback** : What can be improved?
* **Score** : How strong is the prompt?
* **Improved Prompt** : A clearer and more complete version.
* **Suggestions** : Additional ideas the user could consider.

### Flow

`Prompt → Analysis → Feedback → Improved Prompt → Suggestions`

## Tech Stack

* Python
* Streamlit
* Hugging Face
* Transformers
* LLM inference APIs

## Development Journey

### V1 — Prompt Engineering

The first version was built mainly through experimentation with **system instructions and prompt engineering**.

I created my own rules for how the AI should analyze prompts, identify missing information, provide feedback, and generate improved versions.

### V2 — Local LLM

For V2, I experimented with running an LLM directly on my computer using Hugging Face Transformers.

**Model:** `Qwen/Qwen3-0.6B`

This version helped me understand local model inference, tokenization, chat templates, model generation, and the difference between running models locally and using an API.

The model worked locally, but CPU inference made responses significantly slower.

### V3 — API Inference

For V3, I moved the inference to an API to make the application faster and more practical.

**Model:** `zai-org/GLM-5.3-Flash:novita`
**Inference:** Novita API

I also added structured system instructions and custom rules to make the model follow a consistent analysis format.

## What This Project Taught Me

Building this project gave me practical experience with:

* Prompt engineering
* LLM inference
* Hugging Face Transformers
* Local model deployment
* API-based inference
* System and user messages
* Tokenizers and chat templates
* Environment variables
* Debugging and testing AI behavior

A major lesson was that getting an LLM to consistently follow instructions requires **testing, tweaking, and iteration**.

## Project Progression

**V1 → Prompt Engineering**
**V2 → Local LLM**
**V3 → API Inference**

This project is part of my journey into AI engineering.

Prompt Analyzer - Analyze, improve, and score user prompts with AI
