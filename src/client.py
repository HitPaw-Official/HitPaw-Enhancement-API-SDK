"""
HitPaw Upscale API - Python SDK
Official SDK for HitPaw Image and Video Enhancement APIs

@author: HitPaw Official
@license: MIT
@version: 1.0.0
"""

import requests
import time
import json
from typing import Optional, Dict, Any, List, Tuple
from enum import Enum


# ==================== Image Models ====================

class ImageModel(str, Enum):
    """
    Available image enhancement models
    
    Standard Models (Fidelity & Accuracy):
    - General Enhance: Go-to for general upscaling
    - High Fidelity: For high-quality source preservation
    - Portrait Clear: Beauty + clarity balance
    - Portrait Natural: Realistic skin texture
    - Sharp/Detail Denoise: Noise removal
    
    Generative Models (Creativity & Reconstruction):
    - Diffusion-based for severely degraded images
    """
    
    # === Standard Models ===
    
    # General Enhancement
    GENERAL_2X = "general_2x"
    GENERAL_4X = "general_4x"
    
    # High Fidelity (for high-quality sources)
    HIGH_FIDELITY_2X = "high_fidelity_2x"
    HIGH_FIDELITY_4X = "high_fidelity_4x"
    
    # Portrait - Clear (beauty + sharp background)
    FACE_2X = "face_2x"
    FACE_4X = "face_4x"
    
    # Portrait - Natural (realistic texture)
    FACE_V2_2X = "face_v2_2x"
    FACE_V2_4X = "face_v2_4x"
    
    # Denoise (1x - no upscale)
    SHARPEN_DENOISE_1X = "sharpen_denoise_1x"
    DETAIL_DENOISE_1X = "detail_denoise_1x"
    
    # === Generative Models ===
    
    # Generative Portrait (for human subjects)
    GENERATIVE_PORTRAIT_1X = "generative_portrait_1x"
    GENERATIVE_PORTRAIT_2X = "generative_portrait_2x"
    GENERATIVE_PORTRAIT_4X = "generative_portrait_4x"
    
    # Generative Enhance (for general content)
    GENERATIVE_1X = "generative_1x"
    GENERATIVE_2X = "generative_2x"
    GENERATIVE_4X = "generative_4x"


class ImageModelCategory:
    """Helper class to categorize image models"""
    
    # Upscale Models
    UPSCALE = [
        ImageModel.GENERAL_2X, ImageModel.GENERAL_4X,
        ImageModel.HIGH_FIDELITY_2X, ImageModel.HIGH_FIDELITY_4X,
    ]
    
    # Portrait Models
    PORTRAIT_CLEAR = [ImageModel.FACE_2X, ImageModel.FACE_4X]
    PORTRAIT_NATURAL = [ImageModel.FACE_V2_2X, ImageModel.FACE_V2_4X]
    PORTRAIT = PORTRAIT_CLEAR + PORTRAIT_NATURAL
    
    # Denoise Models (1x)
    DENOISE = [ImageModel.SHARPEN_DENOISE_1X, ImageModel.DETAIL_DENOISE_1X]
    
    # Generative Models
    GENERATIVE_PORTRAIT = [
        ImageModel.GENERATIVE_PORTRAIT_1X, 
        ImageModel.GENERATIVE_PORTRAIT_2X, 
        ImageModel.GENERATIVE_PORTRAIT_4X
    ]
    GENERATIVE = [
        ImageModel.GENERATIVE_1X,
        ImageModel.GENERATIVE_2X, 
        ImageModel.GENERATIVE_4X
    ]
    GENERATIVE_ALL = GENERATIVE_PORTRAIT + GENERATIVE
    
    @classmethod
    def get_description(cls, model: ImageModel) -> str:
        """Get model description"""
        descriptions = {
            # General
            ImageModel.GENERAL_2X: "General Enhance 2x - Go-to solution for 2x upscaling in general scenarios",
            ImageModel.GENERAL_4X: "General Enhance 4x - Go-to solution for 4x upscaling in general scenarios",
            ImageModel.HIGH_FIDELITY_2X: "High Fidelity 2x - Preserve original artistic intent and fine textures",
            ImageModel.HIGH_FIDELITY_4X: "High Fidelity 4x - Preserve original artistic intent and fine textures",
            
            # Portrait Clear
            ImageModel.FACE_2X: "Portrait Clear 2x - Beautify faces while sharpening background",
            ImageModel.FACE_4X: "Portrait Clear 4x - Beautify faces while sharpening background",
            
            # Portrait Natural
            ImageModel.FACE_V2_2X: "Portrait Natural 2x - Realistic skin texture recovery",
            ImageModel.FACE_V2_4X: "Portrait Natural 4x - Realistic skin texture recovery",
            
            # Denoise
            ImageModel.SHARPEN_DENOISE_1X: "Sharp Denoise 1x - Aggressively remove noise while sharpening",
            ImageModel.DETAIL_DENOISE_1X: "Detail Denoise 1x - Remove noise preserving original texture",
            
            # Generative Portrait
            ImageModel.GENERATIVE_PORTRAIT_1X: "Generative Portrait 1x - Diffusion-based for human subjects",
            ImageModel.GENERATIVE_PORTRAIT_2X: "Generative Portrait 2x - Diffusion-based for human subjects",
            ImageModel.GENERATIVE_PORTRAIT_4X: "Generative Portrait 4x - Diffusion-based for human subjects",
            
            # Generative Enhance
            ImageModel.GENERATIVE_1X: "Generative Enhance 1x - Diffusion for general content",
            ImageModel.GENERATIVE_2X: "Generative Enhance 2x - Diffusion for general content",
            ImageModel.GENERATIVE_4X: "Generative Enhance 4x - Diffusion for general content",
        }
        return descriptions.get(model, "Unknown model")


# ==================== Video Models ====================

class VideoModel(str, Enum):
    """
    Available video enhancement models
    
    - Ultra HD: SD/HD to 4K conversion
    - General Restore: GAN-based restoration
    - Portrait Restore: Face restoration in video
    - Face Soft: Face beautification
    - Generative: Stable Diffusion for video
    """
    
    # === Restoration & Upscale ===
    
    # Ultra HD (SD/HD to 4K)
    ULTRAD_HD_RESTORE_2X = "ultrahd_restore_2x"
    
    # General Restoration
    GENERAL_RESTORE_1X = "general_restore_1x"
    GENERAL_RESTORE_2X = "general_restore_2x"
    GENERAL_RESTORE_4X = "general_restore_4x"
    
    # Portrait Restoration
    PORTRAIT_RESTORE_1X = "portrait_restore_1x"
    PORTRAIT_RESTORE_2X = "portrait_restore_2x"
    
    # Face Soft (Beautification)
    FACE_SOFT_2X = "face_soft_2x"
    
    # Generative
    GENERATIVE_1X = "generative_1x"


class VideoModelCategory:
    """Helper class to categorize video models"""
    
    # Ultra HD
    ULTRA_HD = [VideoModel.ULTRAD_HD_RESTORE_2X]
    
    # General Restoration
    GENERAL_RESTORE = [
        VideoModel.GENERAL_RESTORE_1X,
        VideoModel.GENERAL_RESTORE_2X,
        VideoModel.GENERAL_RESTORE_4X
    ]
    
    # Portrait
    PORTRAIT_RESTORE = [
        VideoModel.PORTRAIT_RESTORE_1X,
        VideoModel.PORTRAIT_RESTORE_2X
    ]
    FACE_SOFT = [VideoModel.FACE_SOFT_2X]
    
    # Generative
    GENERATIVE = [VideoModel.GENERATIVE_1X]
    
    @classmethod
    def get_description(cls, model: VideoModel) -> str:
        """Get model description"""
        descriptions = {
            VideoModel.ULTRAD_HD_RESTORE_2X: "Ultra HD 2x - Convert SD/HD to 4K with deep convolution",
            VideoModel.GENERAL_RESTORE_1X: "General Restore 1x - GAN-based de-noise and de-blur",
            VideoModel.GENERAL_RESTORE_2X: "General Restore 2x - GAN-based de-noise and de-blur",
            VideoModel.GENERAL_RESTORE_4X: "General Restore 4x - GAN-based de-noise and de-blur",
            VideoModel.PORTRAIT_RESTORE_1X: "Portrait Restore 1x - Multi-frame face restoration",
            VideoModel.PORTRAIT_RESTORE_2X: "Portrait Restore 2x - Multi-frame face restoration",
            VideoModel.FACE_SOFT_2X: "Face Soft 2x - Face beautification with identity preservation",
            VideoModel.GENERATIVE_1X: "Generative 1x - Stable Diffusion for impossible restoration",
        }
        return descriptions.get(model, "Unknown model")


# ==================== Job Status ====================

class JobStatus(str, Enum):
    """Job status values"""
    CONVERTING = "CONVERTING"
    COMPLETED = "COMPLETED"
    ERROR = "ERROR"


# ==================== Main Client ====================

class HitPawUpscaleAPI:
    """
    Python SDK for HitPaw Image and Video Enhancement APIs
    
    Base URL: https://api-base.hitpaw.com
    
    Usage:
        client = HitPawUpscaleAPI(api_key="your_api_key")
        
        # Image enhancement
        result = client.enhance_image(
            img_url="https://example.com/image.jpg",
            model_name=ImageModel.GENERAL_2X,
            extension=".jpg"
        )
        
        # Video enhancement
        result = client.enhance_video(
            video_url="https://example.com/video.mp4",
            model_name=VideoModel.GENERAL_RESTORE_2X,
            resolution=[1920, 1080]
        )
    """
    
    BASE_URL = "https://api-base.hitpaw.com"
    
    def __init__(self, api_key: str, base_url: Optional[str] = None):
        """
        Initialize the HitPaw API client
        
        Args:
            api_key: Your HitPaw API key
            base_url: Optional custom base URL
        """
        self.api_key = api_key
        self.base_url = base_url or self.BASE_URL
        self.headers = {
            "Content-Type": "application/json",
            "Apikey": api_key
        }
    
    # ==================== Image Enhancement ====================
    
    def enhance_image(
        self,
        img_url: str,
        model_name: str = ImageModel.GENERAL_2X,
        extension: str = ".jpg",
        exif: bool = False,
        dpi: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Submit an image enhancement job
        
        Args:
            img_url: URL of the image to enhance (must be publicly accessible)
            model_name: Enhancement model (see ImageModel enum)
            extension: Output file extension (.jpg, .png, .webp, etc.)
            exif: Whether to preserve EXIF data (default: False)
            dpi: Target DPI for output (only for non-generative models)
            
        Returns:
            Dict with job_id and consume_coins
            
        Raises:
            requests.HTTPError: If the API returns an error
        """
        url = f"{self.base_url}/api/photo-enhancer"
        
        payload = {
            "img_url": img_url,
            "model_name": model_name,
            "extension": extension,
            "exif": exif
        }
        
        if dpi is not None:
            payload["DPI"] = dpi
        
        response = requests.post(
            url, 
            headers=self.headers, 
            data=json.dumps(payload)
        )
        response.raise_for_status()
        
        data = response.json()
        return {
            "job_id": data["data"]["job_id"],
            "consume_coins": data["data"]["consume_coins"]
        }
    
    # ==================== Video Enhancement ====================
    
    def enhance_video(
        self,
        video_url: str,
        model_name: str,
        resolution: List[int],
        extension: str = ".mp4",
        original_resolution: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        """
        Submit a video enhancement job
        
        Args:
            video_url: URL of the video to enhance (must be publicly accessible)
            model_name: Enhancement model (see VideoModel enum)
            resolution: Target resolution as [width, height], e.g., [1920, 1080]
            extension: Output file extension (default: .mp4)
            original_resolution: Original video resolution as [width, height]
            
        Returns:
            Dict with job_id and consume_coins
            
        Raises:
            requests.HTTPError: If the API returns an error
        """
        url = f"{self.base_url}/api/video-enhancer"
        
        payload = {
            "video_url": video_url,
            "model_name": model_name,
            "resolution": resolution,
            "extension": extension
        }
        
        if original_resolution:
            payload["original_resolution"] = original_resolution
        
        response = requests.post(
            url, 
            headers=self.headers, 
            data=json.dumps(payload)
        )
        response.raise_for_status()
        
        data = response.json()
        return {
            "job_id": data["data"]["job_id"],
            "consume_coins": data["data"]["consume_coins"]
        }
    
    # ==================== Job Status ====================
    
    def check_status(self, job_id: str) -> Dict[str, Any]:
        """
        Check the status of a submitted job
        
        Args:
            job_id: Job ID returned from enhance_image or enhance_video
            
        Returns:
            Dict with job_id, status, res_url (if completed), original_url
        """
        url = f"{self.base_url}/api/task-status"
        payload = {"job_id": job_id}
        
        response = requests.post(
            url, 
            headers=self.headers, 
            data=json.dumps(payload)
        )
        response.raise_for_status()
        
        data = response.json()["data"]
        return {
            "job_id": data["job_id"],
            "status": data["status"],
            "res_url": data.get("res_url"),
            "original_url": data.get("original_url")
        }
    
    def wait_for_completion(
        self,
        job_id: str,
        max_attempts: int = 120,
        poll_interval: int = 5,
        callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """
        Poll job status until completion or error
        
        Args:
            job_id: Job ID to wait for
            max_attempts: Maximum number of polling attempts
            poll_interval: Seconds between polls
            callback: Optional callback function called on each poll
            
        Returns:
            Final job status dict with res_url on success
            
        Raises:
            TimeoutError: If max_attempts is reached
            Exception: If job status is ERROR
        """
        attempt = 0
        
        while attempt < max_attempts:
            result = self.check_status(job_id)
            status = result["status"]
            
            if callback:
                callback(attempt + 1, status)
            
            if status == JobStatus.COMPLETED:
                return result
            elif status == JobStatus.ERROR:
                raise Exception(f"Job {job_id} failed with ERROR status")
            elif status == JobStatus.CONVERTING:
                time.sleep(poll_interval)
                attempt += 1
            else:
                raise Exception(f"Unknown status: {status}")
        
        raise TimeoutError(f"Job {job_id} did not complete within {max_attempts * poll_interval} seconds")
    
    # ==================== Convenience Methods ====================
    
    def enhance_image_and_wait(
        self,
        img_url: str,
        model_name: str = ImageModel.GENERAL_2X,
        extension: str = ".jpg",
        exif: bool = False,
        dpi: Optional[int] = None,
        max_attempts: int = 120,
        poll_interval: int = 5
    ) -> Dict[str, Any]:
        """
        Convenience method: submit image job and wait for completion
        
        Returns final result with res_url
        """
        result = self.enhance_image(
            img_url=img_url,
            model_name=model_name,
            extension=extension,
            exif=exif,
            dpi=dpi
        )
        
        print(f"Image job submitted: {result['job_id']} (coins: {result['consume_coins']})")
        
        final_result = self.wait_for_completion(
            job_id=result["job_id"],
            max_attempts=max_attempts,
            poll_interval=poll_interval,
            callback=lambda a, s: print(f"  Attempt {a}: {s}")
        )
        
        print(f"✅ Complete! Result: {final_result['res_url']}")
        return final_result
    
    def enhance_video_and_wait(
        self,
        video_url: str,
        model_name: str,
        resolution: List[int],
        extension: str = ".mp4",
        original_resolution: Optional[List[int]] = None,
        max_attempts: int = 300,
        poll_interval: int = 10
    ) -> Dict[str, Any]:
        """
        Convenience method: submit video job and wait for completion
        
        Returns final result with res_url
        """
        result = self.enhance_video(
            video_url=video_url,
            model_name=model_name,
            resolution=resolution,
            extension=extension,
            original_resolution=original_resolution
        )
        
        print(f"Video job submitted: {result['job_id']} (coins: {result['consume_coins']})")
        
        final_result = self.wait_for_completion(
            job_id=result["job_id"],
            max_attempts=max_attempts,
            poll_interval=poll_interval,
            callback=lambda a, s: print(f"  Attempt {a}: {s}")
        )
        
        print(f"✅ Complete! Result: {final_result['res_url']}")
        return final_result


# ==================== Error Handling ====================

class HitPawAPIError(Exception):
    """Base exception for HitPaw API errors"""
    def __init__(self, error_code: int, message: str):
        self.error_code = error_code
        self.message = message
        super().__init__(f"[{error_code}] {message}")


ERROR_MESSAGES = {
    110400000: "api_key is not valid",
    110400002: "The task does not exist",
    110400003: "The task failed, please try again",
    110400005: "The model is not supported, please try again",
    110400007: "The extension is not valid",
    110400008: "The video URL is not valid",
    110400009: "The input resolution is over limit",
    110400010: "The target resolution is over limit",
    110400011: "The video duration is over limit",
    110402000: "The coins are not enough",
    110402001: "The coins are not enough",
    110402004: "The Demo try times exceeded",
}


def handle_api_error(response_data: dict) -> None:
    """
    Handle API error responses
    
    Raises appropriate exception based on error code
    """
    if "error_code" in response_data:
        error_code = response_data["error_code"]
        message = response_data.get("message", ERROR_MESSAGES.get(error_code, "Unknown error"))
        raise HitPawAPIError(error_code, message)


# ==================== CLI Usage ====================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="HitPaw Upscale API CLI")
    parser.add_argument("--api-key", required=True, help="Your HitPaw API key")
    parser.add_argument("--mode", choices=["image", "video"], required=True)
    parser.add_argument("--url", required=True, help="URL of image/video to enhance")
    parser.add_argument("--model", required=True, help="Model name")
    parser.add_argument("--extension", default=".jpg", help="Output extension")
    parser.add_argument("--resolution", help="Target resolution (e.g., 1920,1080)")
    parser.add_argument("--wait", action="store_true", help="Wait for completion")
    
    args = parser.parse_args()
    
    client = HitPawUpscaleAPI(api_key=args.api_key)
    
    if args.mode == "image":
        result = client.enhance_image(
            img_url=args.url,
            model_name=args.model,
            extension=args.extension
        )
        print(f"Job submitted: {result['job_id']}")
        print(f"Coins: {result['consume_coins']}")
        
        if args.wait:
            final = client.wait_for_completion(result["job_id"])
            print(f"Result: {final['res_url']}")
    
    elif args.mode == "video":
        resolution = [int(x) for x in args.resolution.split(",")] if args.resolution else [1920, 1080]
        result = client.enhance_video(
            video_url=args.url,
            model_name=args.model,
            resolution=resolution,
            extension=args.extension
        )
        print(f"Job submitted: {result['job_id']}")
        print(f"Coins: {result['consume_coins']}")
        
        if args.wait:
            final = client.wait_for_completion(result["job_id"], max_attempts=300)
            print(f"Result: {final['res_url']}")
