#!/usr/bin/python3
"""a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class.

    Args:
        obj (any): The object.
        a_class (type): The class to check.
    Returns:
        true or false
    """
    if isinstance(obj, a_class):
        return True
    return False
