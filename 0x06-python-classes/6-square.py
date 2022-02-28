#!/usr/bin/python3
"""define class Square"""


class Square:
    """Define square:"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialises object"""

        self.__size = size
        self.__position = position

    def area(self):
        """returns area in private __size"""

        return self.__size ** 2

    @property
    def size(self):
        """retrieves size"""

        return self.__size

    @size.setter
    def size(self, value):
        """assigns size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints square"""

        position = self.position[0]
        size = self.size
        [print('\n', end='') for _ in range(self.position[1])]

        for _ in range(self.size):
            for _ in range(position):
                print(' ', end='')
            print(size * '#')

    @property
    def position(self):
        """returns pos """

        return self.__position

    @position.setter
    def position(self, value):
        """assigns position"""

        if type(value) is not tuple or len(value) > 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value
