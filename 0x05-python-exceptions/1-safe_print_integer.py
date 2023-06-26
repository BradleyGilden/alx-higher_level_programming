#!/usr/bin/python3

"""
safe_print_list - prints value if value is an integer
@mylist: integer given to print
Return: True if int, False if not
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True
