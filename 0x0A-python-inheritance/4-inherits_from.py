#!/usr/bin/python3

"""
This module contains a function inherits_from()

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""


def inherits_from(obj, a_class):
    """Determines if object {obj} is an instance of a subclass of {a_class}

    Return:
        True: if {obj} is an instance of a subclass of {a_class}
        False: otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
