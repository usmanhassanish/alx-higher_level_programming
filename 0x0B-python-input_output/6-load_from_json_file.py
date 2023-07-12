#!/usr/bin/python3
import json
"""creates object from json"""


def load_from_json_file(filename):
    """creates object"""
    with open(filename) as file:
        json_data = file.read()
        obj = json.loads(json_data)
        return obj
