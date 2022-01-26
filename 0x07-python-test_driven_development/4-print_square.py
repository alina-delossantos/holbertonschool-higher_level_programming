#!/usr/bin/python3
"""
This is the "4-print_square" module

It provides the print_square fx
"""


def print_square(size):
    """prints a square with # of size n"""
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
