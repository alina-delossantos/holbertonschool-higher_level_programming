#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """True if obj of same instance as class or False
    Args:
        obj (obj): object
        a_class (class): class to be compared with
    """
    if isinstance(obj, a_class):
        return True
    return False
