#!/usr/bin/python3
"""creates an object from json"""


def load_from_json_file(filename):
    """creates an object"""
    import json
    with open(filename, "w") as f:
        json.loads(f)
