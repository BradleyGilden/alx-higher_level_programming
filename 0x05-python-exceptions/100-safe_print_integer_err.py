#!/usr/bin/python3
from sys import stderr

"""
safe_print_list - prints value if value is an integer, if not print
                  'Exception: ' followed by err message to stderr
@value: integer given to print
Return: True if int, False if not
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        print(f"Exception: {e}", file=stderr)
        return False
    return True
