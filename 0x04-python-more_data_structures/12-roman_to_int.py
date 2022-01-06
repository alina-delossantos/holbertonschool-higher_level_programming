#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        r_t = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        decimal = 0

        for i in range(len(roman_string)):
            if i + 1 < len(roman_string) and r_t[roman_string[i]] < r_t[roman_string[i+1]]:
                decimal = decimal - r_t[roman_string[i]]
            else:
                decimal = decimal + r_t[roman_string[i]]
        return(decimal)
