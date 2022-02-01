#!/usr/bin/python3
"""Module cks if object is instance of certain class"""

def is_kind_of_class(obj, a_class):
    """True if obj of same instance as class or False
    Args:
        obj (obj): object
        a_class (class): class to be compared with
    """
    return isinstance(obj, a_class)
