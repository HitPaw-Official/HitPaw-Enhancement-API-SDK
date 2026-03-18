# HitPaw Enhancement API - Project Description

## GitHub Repository Description (Short)

```
🎨 Official Python SDK for HitPaw AI Image & Video Enhancement API - Upscale, denoise, restore with cutting-edge AI models
```

---

## README.md - Full Project Description

```markdown
# HitPaw Enhancement API SDK

<p align="center">
  <img src="https://www.hitpaw.com/images/logo.png" alt="HitPaw" width="200"/>
</p>

<p align="center">
  <a href="https://pypi.org/project/hitpaw-upscale-api/">
    <img src="https://img.shields.io/pypi/v/hitpaw-upscale-api.svg" alt="PyPI">
  </a>
  <a href="https://github.com/HitPaw-Official/HitPaw-Upscale-API">
    <img src="https://img.shields.io/github/license/HitPaw-Official/HitPaw-Upscale-API" alt="License">
  </a>
  <a href="https://developer.hitpaw.com/">
    <img src="https://img.shields.io/badge/Documentation-HitPaw%20API-blue" alt="API Docs">
  </a>
</p>

---

## 🔥 What is HitPaw Enhancement API?

Access the world's most powerful AI media enhancement models designed for professional use. Our technology provides the **"last-mile" solution** for improving image and video quality, trusted by industry leaders to deliver industrial-grade results.

### ✨ Key Features

- **🖼️ Image Enhancement**: Upscale images 2x/4x with AI-powered super-resolution
- **🎬 Video Enhancement**: Upscale videos up to 4K with temporal stability
- **👤 Portrait Enhancement**: Specialized face restoration and beautification
- **🧹 Denoise & Restore**: Remove noise, blur, and compression artifacts
- **🎨 Generative Models**: AI reconstruction for severely degraded content

---

## 🚀 Quick Start

### Installation

```bash
pip install hitpaw-upscale-api
```

### Basic Usage

```python
from hitpaw_upscale_api import HitPawUpscaleAPI, ImageModel

# Initialize with your API key
client = HitPawUpscaleAPI(api_key="your_api_key")

# Image Enhancement - 2x upscale
result = client.enhance_image_and_wait(
    img_url="https://example.com/photo.jpg",
    model_name=ImageModel.GENERAL_2X,
    extension=".jpg"
)
print(f"Enhanced image: {result['res_url']}")
```

---

## 📋 Available Models

### Image Models

| Model | Description | Use Case |
|-------|-------------|----------|
| `general_2x/4x` | General Enhance | Social media, general photos |
| `high_fidelity_2x/4x` | High Fidelity | Preserve original artistic intent |
| `face_2x/4x` | Portrait Clear | Beautify while sharpening |
| `face_v2_2x/4x` | Portrait Natural | Realistic skin texture recovery |
| `sharpen_denoise_1x` | Sharp Denoise | Remove noise, crisp edges |
| `detail_denoise_1x` | Detail Denoise | Subject-focused enhancement |
| `generative_portrait_*` | Generative Portrait | AI face reconstruction |
| `generative_*` | Generative Enhance | Creative reconstruction |

### Video Models

| Model | Description |
|-------|-------------|
| `general_restore_1x/2x/4x` | General restoration |
| `portrait_restore_1x/2x` | Face restoration in video |
| `face_soft_2x` | Face beautification |
| `ultrahd_restore_2x` | SD/HD to 4K conversion |
| `generative_1x` | Stable Diffusion video enhancement |

---

## 📚 Documentation

- [API Documentation](https://developer.hitpaw.com/)
- [Image API Reference](https://developer.hitpaw.com/image/API-reference)
- [Video API Reference](https://developer.hitpaw.com/video/API-reference)

---

## ⚙️ Requirements

- Python 3.7+
- `requests` library

---

## 📄 License

MIT License

---

## 🛟 Support

- [Official Website](https://www.hitpaw.com/)
- [API Portal](https://developer.hitpaw.com/)
- [Purchase API Key](https://www.hitpaw.com/hitpaw-api.html)
```

---

## 📝 Repo Topics/Tags

```
python-sdk, api-client, image-enhancement, video-enhancement, ai, 
super-resolution, upscaling, denoising, portrait-enhancement, hitpaw
```

---

## 💬 One-line Description (for repo creation)

> **Official Python SDK for HitPaw AI Image & Video Enhancement API - Upscale, restore, and enhance media with cutting-edge AI models**
```

Let me know if you want me to adjust the tone, add more details, or focus on specific features! 🎯
