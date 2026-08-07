from story_generator import create_story
from video_generator import generate_video
from video_editor import edit_video
from youtube_uploader import upload_video
from email_notify import send_notification


def run_pipeline():

    print("=== Tiny Tails Automation ===")

    # 1. Create story
    story = create_story()

    print("\nStory created:")
    print(story["title"])

    # 2. Generate video
    video = generate_video(story["scenes"])

    if not video["success"]:
        print("\nVideo generation is not connected yet.")
        return

    # 3. Edit video
    edited = edit_video(video["video_path"])

    if not edited["success"]:
        print("\nVideo editing is not connected yet.")
        return

    # 4. Upload to YouTube
    upload = upload_video(
        edited["video_path"],
        story["title"],
        "A Tiny Tails adventure for kids."
    )

    if not upload["success"]:
        print("\nYouTube upload is not connected yet.")
        return

    # 5. Send notification
    send_notification(
        f"Uploaded successfully: {story['title']}"
    )

    print("\n=== Pipeline completed ===")


if __name__ == "__main__":
    run_pipeline()
