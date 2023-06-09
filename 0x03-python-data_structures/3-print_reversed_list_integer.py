#!/usr/bin/python3

# prints reversed int list without casting
def print_reversed_list_integer(my_list=[]):

    for num in my_list[::-1]:
        print("{:d}".format(num))


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
