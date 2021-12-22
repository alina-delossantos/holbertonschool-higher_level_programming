#!/usr/bin/python3


def printdigit(nbr):
    lastdigit = 0
    if nbr >= 0:
        lastdigit = nbr % 10
    else:
        lastdigit = 10 - (nbr % 10)

    print('{:d}'.format(lastdigit), end='')
    return lastdigit


if __name__ == '__main__':
    printdigit(12345)
