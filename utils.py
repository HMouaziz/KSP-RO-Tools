import json


def get():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data
