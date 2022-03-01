#!/usr/bin/python3
"""
    splits and prints string after certain special chars
"""


def text_indentation(text):
    """splits string
    Args:
        text (str): string
    Raises:
        TypeError: if not string
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    text = text.strip()
    while i < len(text):
        print(text[i], end='')
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            print('\n')
            if i == len(text) - 1:
                break
            if text[i + 1] == ' ':
                i += 1
            while text[i] == ' ' and text[i + 1] == ' ' and i + 1 < len(text):
                i += 1
        i += 1
