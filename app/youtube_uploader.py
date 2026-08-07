import os


def upload_video(video_path, title, description):

    channel = os.getenv(
        "YOUTUBE_CHANNEL",
        "default"
    )

    print("Uploading to channel:", channel)
    print("Title:", title)
    print("Video:", video_path)

    return {
        "success": False,
        "message": "YouTube uploader not connected yet."
    }
