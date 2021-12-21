#!/usr/bin/python3
for nbr in range(100):
    separator = '\n'
    if (nbr < 99):
        separator = ", "
    print("{:02d}{}".format(nbr, separator), end="")
