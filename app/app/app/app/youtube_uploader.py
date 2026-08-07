import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def get_youtube_service():
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET_FILE")

    if not client_secret:
        raise RuntimeError("GOOGLE_CLIENT_SECRET_FILE is not configured.")

    flow = InstalledAppFlow.from_client_secrets_file(
        client_secret,
        SCOPES
    )

    credentials = flow.run_local_server(port=0)

    return build(
        "youtube",
        "v3",
        credentials=credentials
    )


def upload_video(video_path, title, description):
    youtube = get_youtube_service()

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "categoryId": "24"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(
            video_path,
            mimetype="video/mp4",
            resumable=True
        )
    )

    response = request.execute()

    return response["id"]
