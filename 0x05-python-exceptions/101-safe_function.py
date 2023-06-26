#!/usr/bin/python3
from sys import stderr

"""
safe_function - executes function safely
@args: function arguments
@fct: pointer to function
Return: function return
"""


def safe_function(fct, *args):
    ret = None

    try:
        ret = fct(args[0], args[1])
    except Exception as e:
        print(f"Exception: {e}", file=stderr)
        return ret
    return ret
