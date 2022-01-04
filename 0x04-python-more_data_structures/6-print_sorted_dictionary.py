#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        organized = sorted(a_dictionary.keys())
        for i in organized:
            print("{:s}: {}".format(i, a_dictionary[i]))
