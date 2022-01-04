#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maximum = 0
    for i, j in enumerate(my_list):
        if i == 0 or j > maximum:
            maximum = j
    return maximum
