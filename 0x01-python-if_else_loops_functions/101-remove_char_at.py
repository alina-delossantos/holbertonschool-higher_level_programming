#!/usr/bin/python3


def remove_char_at(str, n):
    clone = ''
    if len(str) == 0:
        return str
    for i in range(len(str)):
        if i != n:
            clone += str[i]
    return clone
