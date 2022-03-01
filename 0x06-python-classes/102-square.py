#!/usr/bin/python3
""" defines square class """


class Square:
    """ square instance pv attr"""
    def __init__(self, size=0):
        self.size = size

    """ return size """
    @property
    def size(self):
        return self.__size

    """ size set as pv """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ return area """
    def area(self):
        return self.__size ** 2

    """ comparator """
    """ equals """
    def __eq__(self, other):
        if isinstance(other, Square):
            return self.size == other.size

    """ larger """
    def __gt__(self, other):
        if isinstance(other, Square):
            return self.size > other.size

    """ diff """
    def __ne__(self, other):
        if isinstance(other, Square):
            return self.size != other.size

    """ less """
    def __lt__(self, other):
        if isinstance(other, Square):
            return self.size < other.size

    """ larger or equal """
    def __ge__(self, other):
        if isinstance(other, Square):
            return self.size >= other.size

    """ less or equal """
    def __le__(self, other):
        if isinstance(other, Square):
            return self.size <= other.size
