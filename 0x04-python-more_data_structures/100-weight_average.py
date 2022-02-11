#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        dividend = 0
        divisor = 0
        for tupl in my_list:
            dividend += tupl[0] * tupl[1]
            divisor += tupl[1]

        return dividend / divisor

    return 0
