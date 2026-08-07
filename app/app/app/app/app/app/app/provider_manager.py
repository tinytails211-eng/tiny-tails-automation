import json


def load_providers():

    with open("config/providers.json", "r") as file:
        return json.load(file)


def get_primary_provider():

    providers = load_providers()
    return providers["primary"]


def get_backup_provider():

    providers = load_providers()
    return providers["backup"]
