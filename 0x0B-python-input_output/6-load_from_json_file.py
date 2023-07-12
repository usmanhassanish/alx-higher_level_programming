#!/usr/bin/python3
"""creates an object from json"""


def load_from_json_file(filename):
    """creates object"""
    import json
    with open(filename) as file:
        obj = json.load(file)
        return obj
