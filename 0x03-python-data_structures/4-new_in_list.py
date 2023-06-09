#!/usr/bin/python3

# modify element at index without modifying original list
def new_in_list(my_list, idx, element):
    a_len = len(my_list)

    if idx > a_len - 1 or idx < 0:
        return my_list

    new_list = my_list[:]  # creates a copy of list
    new_list[idx] = element

    return(new_list)
