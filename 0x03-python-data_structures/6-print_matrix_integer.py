#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        x = len(matrix)
        y = len(matrix[0])
        for item in range(x):
            for subitem in range(y):
                if subitem == y - 1:
                    print('{:d}'.format(matrix[item][subitem]))
                else:
                    print('{:d} '.format(matrix[item][subitem]), end='')
    else:
        print()
