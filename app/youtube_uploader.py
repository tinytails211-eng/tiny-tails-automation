import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def upload_video(video_file, title, description=""):
    print(f"Uploading to YouTube: {title}")

    if not os.path.exists(video_file):
        return {
            "success": False,
            "message": f"Video file not found: {video_file}"
        }

    credentials_file = "config/client_secret.json"
    token_file = "config/youtube_token.json"

    try:
        credentials = None

        if os.path.exists(token_file):
            from google.oauth2.credentials import Credentials
            credentials = Credentials.from_authorized_user_file(
                token_file,
                SCOPES
            )

        if not credentials or not credentials.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file,
                SCOPES
            )

            credentials = flow.run_local_server(
                port=0,
                access_type="offline",
                prompt="consent"
            )

            os.makedirs("config", exist_ok=True)

            with open(token_file, "w") as token:
                token.write(credentials.to_json())

        youtube = build(
            "youtube",
            "v3",
            credentials=credentials
        )

        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                    "categoryId": "24"
                },
                "status": {
                    "privacyStatus": "private"
                }
            },
            media_body=MediaFileUpload(
                video_file,
                chunksize=-1,
                resumable=True
            )
        )

        response = request.execute()

        return {
            "success": True,
            "video_id": response["id"],
            "message": "Video uploaded successfully."
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }
