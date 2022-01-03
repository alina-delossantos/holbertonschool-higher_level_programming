#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    total = 0
    for i, arg in enumerate(argv[1:]):
        total += int(arg)

    print('{:d}'.format(total))
