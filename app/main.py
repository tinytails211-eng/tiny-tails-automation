from story_generator import create_story
from video_generator import generate_video
from video_editor import combine_clips


def run_pipeline():

    story = create_story()

    print("Story created:")
    print(story["title"])

    clips = []

    for scene in story["scenes"]:
        result = generate_video(
            scene["description"],
            f"scene_{scene['scene']}.mp4"
        )

        if result["success"]:
            clips.append(result["output"])

    if clips:
        final_video = combine_clips(
            clips,
            "tiny_tails_final.mp4"
        )

        print("Video ready:")
        print(final_video)

    else:
        print("No video clips generated yet.")


if __name__ == "__main__":
    run_pipeline()
