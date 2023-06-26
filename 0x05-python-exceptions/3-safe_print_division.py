#!/usr/bin/python3

"""
check for zero division errors
@a: divident
@b: divisor
"""


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
        return result
