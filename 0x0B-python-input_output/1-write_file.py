#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """
        writes str into file (UTF8)
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
