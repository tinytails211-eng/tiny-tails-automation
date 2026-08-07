import os


def generate_voice(text, output_path):

    provider = os.getenv(
        "VOICE_PROVIDER",
        "default"
    )

    print("Voice provider:", provider)
    print("Narration text:", text)

    # Real voice API connection will be added later.

    return {
        "success": False,
        "provider": provider,
        "output": output_path,
        "message": "Voice provider not connected yet."
    }
