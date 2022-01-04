#!/usr/bin/python3


def no_c(my_string):
    if my_string:
        not_allowed = "cC"
        for letter in not_allowed:
            new_string = my_string.replace(letter, "")
            return(new_string)
