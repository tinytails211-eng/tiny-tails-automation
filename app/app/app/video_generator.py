import os
import requests


def generate_video(prompt, output_path):
    """
    Placeholder for the video-generation provider.

    The provider will be connected later after we
    choose the API that can run automatically in the VPS.
    """

    provider = os.getenv("VIDEO_PROVIDER", "flow")

    print(f"Video provider: {provider}")
    print(f"Video prompt: {prompt}")

    # API connection will be added here later.
    return {
        "success": False,
        "provider": provider,
        "output": output_path,
        "message": "Video provider not connected yet."
    }
