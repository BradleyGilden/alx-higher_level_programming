#!/usr/bin/python3

# prints reversed int list without casting
def print_reversed_list_integer(my_list=[]):

    if isinstance(my_list, list):
        my_list.reverse()

        for num in my_list:
            print("{:d}".format(num))
