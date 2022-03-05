#!/usr/bin/python3
""" read file """


def read_file(filename=""):
    """Fx to read file and print contents to stdout
    Argument:
        filename (str): filename to open
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
