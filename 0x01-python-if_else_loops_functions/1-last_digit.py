#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = (number % 10)

else:
    if (number % 10) != 0:
        last_digit = (number % 10) - 10
    else:
        last_digit = 0

if last_digit > 5:
    banner = 'and is greater than 5'
if last_digit == 0:
    banner = 'and is 0'
if last_digit < 6 and last_digit != 0:
    banner = 'and is less than 6 and not 0'

print('Last digit of {:d} is {:d} {}'.format(number, last_digit, banner))
