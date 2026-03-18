# HitPaw Enhancement API - English Project Descriptions

## Short Description (Repository Title)

```
HitPaw Enhancement API SDK
```

Or more descriptive:

```
HitPaw AI Image & Video Enhancement SDK - Upscale, denoise, restore with AI
```

---

## Full Description (README)

```markdown
# HitPaw Enhancement API SDK

Official Python SDK for HitPaw AI Image and Video Enhancement APIs.

## Features

- 🖼️ **Image Enhancement** - Upscale images 2x/4x with AI super-resolution
- 🎬 **Video Enhancement** - Upscale videos up to 4K with temporal stability  
- 👤 **Portrait Enhancement** - Face restoration and beautification
- 🧹 **Denoise & Restore** - Remove noise, blur, and compression artifacts
- 🎨 **Generative Models** - AI reconstruction for severely degraded content

## Installation

```bash
pip install hitpaw-upscale-api
```

## Quick Start

```python
from hitpaw_upscale_api import HitPawUpscaleAPI, ImageModel

client = HitPawUpscaleAPI(api_key="your_api_key")

# Image Enhancement
result = client.enhance_image_and_wait(
    img_url="https://example.com/photo.jpg",
    model_name=ImageModel.GENERAL_2X,
    extension=".jpg"
)
print(f"Result: {result['res_url']}")
```

## Available Models

### Image
| Model | Description |
|-------|-------------|
| general_2x/4x | General enhancement |
| high_fidelity_2x/4x | High fidelity upscaling |
| face_2x/4x | Portrait clear |
| face_v2_2x/4x | Portrait natural |
| sharpen_denoise_1x | Sharp denoise |
| detail_denoise_1x | Detail denoise |
| generative_* | AI generation |

### Video
| Model | Description |
|-------|-------------|
| general_restore_1x/2x/4x | General restoration |
| portrait_restore_1x/2x | Face restoration |
| face_soft_2x | Face beautification |
| ultrahd_restore_2x | SD/HD to 4K |

## Documentation

- [API Docs](https://developer.hitpaw.com/)
- [Image API](https://developer.hitpaw.com/image/API-reference)
- [Video API](https://developer.hitpaw.com/video/API-reference)

## License

MIT
```

---

## One-line for GitHub Repo Creation

> **Official Python SDK for HitPaw AI Image & Video Enhancement API**

---

## Topics/Tags

```
python, python-sdk, api-client, ai, machine-learning, image-processing, 
video-processing, super-resolution, upscaling, denoising, ai-enhancement
```

---

Copy whichever you need! 🚀
