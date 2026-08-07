import os


def send_notification(message):

    email = os.getenv(
        "NOTIFY_EMAIL",
        "default"
    )

    print("Sending notification to:", email)
    print("Message:", message)

    return {
        "success": False,
        "message": "Email notification not connected yet."
    }
