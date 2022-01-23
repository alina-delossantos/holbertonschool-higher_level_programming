#!/usr/bin/python3

""" add_integer
Adds two int (a, b) and returns its sum
Float is converted to int, otherwise raise TypeError
"""

def add_integer(a, b=98):

    """ add_integer - adds two integers (a, b)
    Returns: integer sum
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        b = int(b)

    return a + b
