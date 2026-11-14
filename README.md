# Personal AI Image Generation API

A personal image generation API built with Python and [Modal](https://modal.com/), using cloud GPUs to run open-source image generation models.

## Overview

This project explores deploying and running AI image generation models on Modal. It provides an OpenAI-compatible API for generating images through cloud GPU inference.

The project is intended for personal use, experimentation, and learning about serverless GPU deployment.

## Features

- GPU-accelerated image generation
- OpenAI-compatible Images API
- Support for Z-Image-Turbo and KOOK Guanlan
- API key authentication
- Shared model weight caching with Modal Volumes
- Automatic GPU worker scaling

## Deployment

Requirements:
- A Modal account with GPU access
- Python 3.12 or later
- Modal CLI

Install dependencies:

```bash
pip install -r requirements.txt
modal token new
```

Create an API authentication secret:

```bash
modal secret create image-api-auth API_KEY=your-secret-key
```

Deploy the application:

```bash
modal deploy images_app.py
```

After deployment, use the URL provided by Modal with `/v1` as the API base URL.

## API Usage

List available models:

```bash
curl "$BASE_URL/models" \
  -H "Authorization: Bearer $API_KEY"
```

Generate an image:

```bash
curl "$BASE_URL/images/generations" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "z-image-turbo",
    "prompt": "A peaceful mountain landscape at sunrise",
    "size": "1024x1024",
    "response_format": "b64_json"
  }'
```

## Project Goals

- Experiment with open-source image generation models
- Learn how to deploy AI inference services on Modal
- Explore GPU performance and resource configurations
- Use a personal API with compatible AI clients

## Credits

This project is based on the open-source implementation by [NormanMises](https://github.com/NormanMises/z-image-turbo-modal-openai-api).

The original MIT license and copyright notices are retained. Please refer to the original project and individual model licenses for their respective terms.
