#!/usr/bin/python3
"""an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class.

    Args:
        obj (any): The object.
        a_class (type): The class to check.
    Returns:
        true or false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
