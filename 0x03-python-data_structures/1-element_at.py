#!/usr/bin/python3

# a function that retrieves an element from a list like in C
def element_at(my_list, idx):
    a_len = len(my_list)

    if idx > a_len - 1 or idx < 0:
        return None

    return my_list[idx]
