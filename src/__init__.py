"""
HitPaw Upscale API
Official Python SDK for HitPaw Image and Video Enhancement APIs
"""

from .client import HitPawUpscaleAPI, ImageModel, VideoModel, JobStatus, HitPawAPIError

__version__ = "1.0.0"
__all__ = ["HitPawUpscaleAPI", "ImageModel", "VideoModel", "JobStatus", "HitPawAPIError"]
