import os
import smtplib
from email.message import EmailMessage


def send_email(subject, message):

    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    email = EmailMessage()
    email["From"] = sender
    email["To"] = receiver
    email["Subject"] = subject

    email.set_content(message)

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            sender,
            password
        )

        smtp.send_message(email)


if __name__ == "__main__":
    send_email(
        "Tiny Tails Automation",
        "Test email sent successfully."
    )
