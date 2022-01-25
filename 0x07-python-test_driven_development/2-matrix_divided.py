 #!/usr/bin/python3
"""
    Matrix division: divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divides all every item in a matrix by a given num"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    item_size = None
    for num in matrix:
        if type(num) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if item_size is None:
            item_size = len(num)
        elif item_size != len(num):
            raise TypeError("Each row of the matrix must have the same size")
        for i in num:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in num] for num in matrix]
