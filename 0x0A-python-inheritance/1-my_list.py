#!/usr/bin/python3
"""class inherits from list"""


class MyList(list):

    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints list sorted in ascending order"""

        print(sorted(self))
