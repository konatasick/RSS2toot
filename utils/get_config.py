import json


def GetConfig():
    with open("conf.json", "r") as f:
        config = json.load(f)
    return config
