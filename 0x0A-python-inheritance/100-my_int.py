#!/usr/bin/python3
"""a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int == and !=."""

    def __eq__(self, value):
        """Override behaviour."""
        return self.real != value

    def __ne__(self, value):
        """Override behavior."""
        return self.real == value
