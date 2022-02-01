#!/usr/bin/python3
"""verifies class instance"""


def is_same_class(obj, a_class):
    """chekcs if insatnce of certain class
    Return:
        True or False
    """

    if type(obj) == a_class:
        return True
    else:
        return False
