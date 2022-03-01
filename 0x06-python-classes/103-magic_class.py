#!/usr/bin/python3
"""Python class MagicClass"""
import math


class MagicClass:
    """define class"""
    def __init__(self, radius=0):
        """create circle"""
        self.__radius = 0
        if (type(radius) is not int):
            if (type(radius) is not float):
                raise TypeError("radius must be a number")
        self.__radius = radius
        return None

    def area(self):
        """calculate are"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """calculate circumference"""
        return((2 * math.pi) * self.__radius)
