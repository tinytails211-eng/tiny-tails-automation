import json
import os


def load_providers():
    config_path = os.path.join(
        "config",
        "providers.json"
    )

    with open(config_path, "r") as file:
        return json.load(file)


def get_primary_provider():
    config = load_providers()
    return config["primary_provider"]


def get_backup_provider():
    config = load_providers()
    return config["backup_provider"]


if __name__ == "__main__":
    print("Primary:", get_primary_provider())
    print("Backup:", get_backup_provider())
