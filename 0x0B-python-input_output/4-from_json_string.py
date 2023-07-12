#!/usr/bin/python3
"""deserialize"""


def from_json_string(my_str):
    """converts json to pyhton object"""
    import json
    return json.loads(my_str)
