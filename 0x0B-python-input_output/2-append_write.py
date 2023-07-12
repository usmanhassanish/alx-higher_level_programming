#!/usr/bin/python3
"""appends to a file"""


def append_write(filename="", text=""):
    """append to a file and returns number of characters"""
    with open(filename, "a") as f:
        f.write(text)
