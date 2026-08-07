import os
import subprocess


def edit_video(video_file):

    if not os.path.exists(video_file):
        return {
            "success": False,
            "message": f"Video file not found: {video_file}"
        }

    output_file = "edited_video.mp4"

    command = [
        "ffmpeg",
        "-y",
        "-i", video_file,
        "-vf", "scale=1280:720",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "23",
        "-c:a", "aac",
        output_file
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        return {
            "success": False,
            "message": result.stderr[-1000:]
        }

    return {
        "success": True,
        "video_path": output_file
    }
