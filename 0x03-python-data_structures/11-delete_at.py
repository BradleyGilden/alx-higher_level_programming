#!/usr/bin/python3

# removes item from list without list methods
def delete_at(my_list=[], idx=0):
    l_len = len(my_list) - 1

    if idx < 0 or idx > l_len:
        return my_list

    del my_list[idx]

    return my_list
