#!/usr/bin/python3
"""writes to a file"""


def write_file(filename="", text=""):
    """writes to a file and return numer of characters"""
    with open(filename, "w") as f:
        return f.write(text)
