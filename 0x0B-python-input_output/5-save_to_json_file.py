#!/usr/bin/python3
"""save to a file"""


def save_to_json_file(my_obj, filename):
    """writes to a json file"""
    import json
    with open(filename, "w") as f:
        json.dump(my_obj, f)
