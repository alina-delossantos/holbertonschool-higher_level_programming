#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is not None:
        replaced_list = []
        for i, j in enumerate(my_list):
            if my_list[i] == search:
                replaced_list.append(replace)
            else:
                replaced_list.append(my_list[i])
        return replaced_list
