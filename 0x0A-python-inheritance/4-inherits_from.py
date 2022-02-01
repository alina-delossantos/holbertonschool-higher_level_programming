#!/usr/bin/python3
"""module cks if obj inhereits from class"""


def inherits_from(obj, a_class):
    """ck obj inherits from class
        Args:
            obj: object to check
            a_class: class ck with
    """
    if (type(obj) == a_class):
        return False
    return (issubclass(type(obj), a_class))
