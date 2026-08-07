import os
from provider_manager import (
    get_primary_provider,
    get_backup_provider
)


def generate_video(prompt, output_path):

    primary = get_primary_provider()
    backup = get_backup_provider()

    print(f"Trying primary provider: {primary}")

    # Real API connection will be added here later.
    # For now we test the switching logic.

    result = {
        "success": False,
        "provider": primary,
        "output": output_path,
        "message": "Provider connection not added yet."
    }

    if not result["success"]:
        print(f"Primary failed. Backup: {backup}")

        result["provider"] = backup

    return result
