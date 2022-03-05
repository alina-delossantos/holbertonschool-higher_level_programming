#!/usr/bin/python3
"""appends to file"""


def append_write(filename="", text=""):
    """ appends file to end of string """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
