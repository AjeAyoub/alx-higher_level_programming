#!/usr/bin/python3
"""my int"""


class MyInt(int):
    def __eq__(self, other):
        """Return True if self and other are equal, else false"""
        return int(self) != other

    def __ne__(self, other):
        """Return True if self and other are not equal, else false"""
        return int(self) == other
