import os
import subprocess


def combine_clips(clips, output_file):
    """
    Combines multiple video clips into one final video.
    Requires ffmpeg on the server.
    """

    list_file = "clips.txt"

    with open(list_file, "w") as f:
        for clip in clips:
            f.write(f"file '{clip}'\n")

    command = [
        "ffmpeg",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        list_file,
        "-c",
        "copy",
        output_file
    ]

    subprocess.run(command, check=True)

    os.remove(list_file)

    return output_file
