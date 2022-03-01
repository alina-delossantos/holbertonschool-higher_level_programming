#!/usr/bin/python3
""" define square class """


class Square:
    """ square instance with pl attributes"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        if isinstance(self.__size, int) is False:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

        if type(self.__position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(isinstance(i, int) is False for i in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(i < 0 for i in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")

    """ gets size """
    @property
    def size(self):
        return self.__size

    """ sets size as pv """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ fetch position """
    @property
    def position(self):
        return self.__position

    """ sets pos as pv """
    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """ determine area """
    def area(self):
        return self.__size ** 2

    """ prints square """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for line in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print()

    """ square as printable """
    def __str__(self):
        p = ''
        if self.__size == 0:
            p += '\n'
        else:
            for line in range(self.__position[1]):
                p += '\n'
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    p += " "
                for j in range(self.__size):
                    p += '#'
                p += '\n'
        return p[:-1]
