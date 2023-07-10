#!/usr/bin/python3
"""gets all attributes of an object"""


def lookup(obj):
    """the function that gets all the attributes and methods of an object """
    attributes = []
    methods = []

    attributes =
    [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    return attributes + methods
