#!/usr/bin/python3
""" module that finds peak value """


def find_peak(list_of_integers):
    """finds peak value"""
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
