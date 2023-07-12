#!/usr/bin/python3
"""appends to a file"""


def append_write(filename="", text=""):
    """append to a file and returns number of characters"""
    with open(filename, "wb") as f:
        f.write(text.encode("utf-8"))
    return len(text)
