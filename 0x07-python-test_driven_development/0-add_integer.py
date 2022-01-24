#!/usr/bin/python3

""" add_integer
Adds two int (a, b) and returns its sum
Float is converted to int, otherwise raise TypeError
"""


def add_integer(a, b=98):

    """Returns: integer sum"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a + b)
