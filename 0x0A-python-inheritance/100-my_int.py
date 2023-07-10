#!/usr/bin/python3

"""
This module contains subclass of int(): MyInt

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""


class MyInt(int):
    """MyInt inverts the == and != operators"""
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
