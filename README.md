# A personal AI image generation API powered by Z-Image-Turbo and Modal GPU

A personal AI image generation API powered by [Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) and [Modal](https://modal.com/).

This project runs the Z-Image-Turbo image generation model on Modal GPU and provides an API for generating images remotely.

## Features

- Run Z-Image-Turbo on Modal GPU
- Generate images through an API
- OpenAI-compatible image generation endpoint
- Use cloud GPU resources instead of local hardware
- Store model weights in a persistent Modal Volume

## Requirements

- Python 3.12+
- A Modal account
- Modal CLI
- Modal GPU access

## Deployment

Install the dependencies:

```bash
pip install -r requirements.txt
```

Set up Modal:

```bash
modal token new
```

Create an API key secret:

```bash
modal secret create image-api-auth API_KEY=your_api_key
```

Deploy the application:

```bash
modal deploy images_app.py
```

After deployment, Modal will provide an API URL. The API endpoint uses the `/v1` path.

## API Usage

List available models:

```http
GET /v1/models
```

Generate an image:

```http
POST /v1/images/generations
```

Example request:

```json
{
  "model": "z-image-turbo",
  "prompt": "A beautiful landscape at sunset",
  "response_format": "b64_json"
}
```

## Project Goals

This project is mainly for personal use and learning:

- Experimenting with open-source image generation models
- Learning how to deploy AI inference on Modal
- Exploring cloud GPU usage and performance
- Building a personal image generation API

## Credits

This project is based on the open-source work of [NormanMises](https://github.com/NormanMises/z-image-turbo-modal-openai-api).

Please refer to the original repository and its license for the original implementation and attributions.
