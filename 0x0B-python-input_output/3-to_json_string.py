#!/usr/bin/python3
"""serialize object"""


def to_json_string(my_obj):
    """converts to json representation"""
    import json
    return json.dumps(my_obj)
