#!/usr/bin/python3


ascii = 0
for nbr in range(122, 96, -1):
    if nbr % 2 == 0:
        ascii = nbr
    else:
        ascii = nbr - 32
    print("{}".format(chr(ascii)), end='')
