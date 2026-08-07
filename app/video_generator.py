import os


def generate_video(scenes):

    provider = os.getenv(
        "VIDEO_PROVIDER",
        "default"
    )

    print("Video provider:", provider)

    for scene in scenes:
        print("Generating scene:", scene)

    return {
        "success": False,
        "provider": provider,
        "message": "Video generator not connected yet."
    }
