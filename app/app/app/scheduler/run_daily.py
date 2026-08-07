import time
from app.main import run_pipeline


def start():

    print("Tiny Tails automation started")

    while True:

        try:
            run_pipeline()

            print("Video completed. Waiting for next run.")

            # Wait 24 hours
            time.sleep(86400)

        except Exception as error:
            print("Error:", error)

            # Retry after 1 hour
            time.sleep(3600)


if __name__ == "__main__":
    start()
