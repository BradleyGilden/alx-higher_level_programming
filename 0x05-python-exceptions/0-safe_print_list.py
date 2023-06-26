#!/usr/bin/python3

"""
safe_print_list - prints list, if index is greater then size of list then
                  print the whole list and return size of list
@mylist: list given to print
@x: number of elements to print
Return: returns number of elements to be printed
"""


def safe_print_list(my_list=[], x=0) -> int:
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
        except IndexError:
            print()
            return i
        i += 1
    print()
    return i
