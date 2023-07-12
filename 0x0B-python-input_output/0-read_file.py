#!/usr/bin/python3
"""Reads a file"""


def read_file(filename=""):
    """reads and print to standard output"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
