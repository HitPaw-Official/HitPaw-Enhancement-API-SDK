# HitPaw Upscale API

Official Python SDK for HitPaw Image and Video Enhancement APIs.

[![PyPI version](https://img.shields.io/pypi/v/hitpaw-upscale-api.svg)](https://pypi.org/project/hitpaw-upscale-api/)
[![Python](https://img.shields.io/pypi/pyversions/hitpaw-upscale-api.svg)](https://pypi.org/project/hitpaw-upscale-api/)
[![License](https://img.shields.io/pypi/l/hitpaw-upscale-api.svg)](https://pypi.org/project/hitpaw-upscale-api/)

## Features

- 🎨 **Image Enhancement**: Upscale images 2x or 4x with AI models
- 🎬 **Video Enhancement**: Upscale videos up to 4K with AI models
- 🔄 **Async Jobs**: Submit jobs and poll for status
- ⚡ **Convenience Methods**: One-line submit-and-wait functionality

## Installation

```bash
pip install hitpaw-upscale-api
```

Or install from source:

```bash
git clone https://github.com/HitPaw-Official/HitPaw-Upscale-API.git
cd HitPaw-Upscale-API
pip install -e .
```

## Quick Start

```python
from hitpaw_upscale_api import HitPawUpscaleAPI, ImageModel, VideoModel

# Initialize with your API key
client = HitPawUpscaleAPI(api_key="your_api_key")

# Image Enhancement
result = client.enhance_image_and_wait(
    img_url="https://example.com/photo.jpg",
    model_name=ImageModel.GENERAL_2X,
    extension=".jpg"
)
print(f"Enhanced image: {result['res_url']}")

# Video Enhancement
result = client.enhance_video_and_wait(
    video_url="https://example.com/video.mp4",
    model_name=VideoModel.GENERAL_RESTORE_2X,
    resolution=[1920, 1080]
)
print(f"Enhanced video: {result['res_url']}")
```

## API Models

### Image Models

| Model | Description | Resolution |
|-------|-------------|------------|
| `face_2x`, `face_4x` | Face Clear Model | 2x/4x |
| `face_v2_2x`, `face_v2_4x` | Face Natural Model | 2x/4x |
| `general_2x`, `general_4x` | General Enhance Model | 2x/4x |
| `high_fidelity_2x`, `high_fidelity_4x` | High Fidelity Model | 2x/4x |
| `sharpen_denoise_1x` | Sharp Denoise Model | 1x |
| `detail_denoise_1x` | Detail Denoise Model | 1x |
| `generative_portrait_*` | Generative Portrait Model | 1x/2x/4x |
| `generative_*` | Generative Enhance Model | 1x/2x/4x |

### Video Models

| Model | Description |
|-------|-------------|
| `face_soft_2x` | Face Soft Model |
| `portrait_restore_1x`, `portrait_restore_2x` | Portrait Restore Model |
| `general_restore_1x`, `general_restore_2x`, `general_restore_4x` | General Restore Model |
| `ultrahd_restore_2x` | Ultra HD Model |
| `generative_1x` | Generative Model |

## CLI Usage

```bash
# Image enhancement
python -m hitpaw_upscale_api --api-key KEY --mode image \
  --url https://example.com/image.jpg \
  --model general_2x \
  --extension .jpg \
  --wait

# Video enhancement
python -m hitpaw_upscale_api --api-key KEY --mode video \
  --url https://example.com/video.mp4 \
  --model general_restore_2x \
  --resolution 1920,1080 \
  --wait
```

## Documentation

For detailed API documentation, visit:
- [Image API Reference](https://developer.hitpaw.com/image/API-reference)
- [Video API Reference](https://developer.hitpaw.com/video/API-reference)

## License

MIT License

## Support

For API key requests and technical support, visit [HitPaw API](https://developer.hitpaw.com/).
