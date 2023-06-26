#!/usr/bin/python3

"""
safe_print_list - prints int list, if index is greater then size of list then
                  an exception must occur. If element is not int then ignore
@mylist: list given to print
@x: number of elements to print
Return: returns number of elements to be printed
"""


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    i_err = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            i_err += 1
        i += 1
    print()
    return (i - i_err)
