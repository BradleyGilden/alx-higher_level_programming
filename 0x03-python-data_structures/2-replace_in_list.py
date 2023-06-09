#!/usr/bin/python3

# replace element in list at index
def replace_in_list(my_list, idx, element):
    a_len = len(my_list)

    if idx > a_len - 1 or idx < 0:
        return my_list

    my_list[idx] = element
    return my_list
