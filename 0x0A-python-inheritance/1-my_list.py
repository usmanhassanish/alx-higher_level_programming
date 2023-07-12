#!/usr/bin/python3
"""
contains the class MYLIST
"""


class MyList(list):
    """a subclass"""
    def __init__(self):
        """initializes an object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
