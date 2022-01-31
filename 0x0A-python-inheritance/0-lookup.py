#!/usr/bin/python3


"""Lookup module
function that returns the list of available attributes and methods of an object
"""


def lookup(object):
    """function that returns the list of available attributes of obj"""
    return dir(object)
