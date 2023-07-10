#!/usr/bin/python3

"""
This module contains MyList class

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""


class MyList(list):
    """A subclass of the list python class that implements print_sorted func
    """

    def print_sorted(self):
        """prints a sorted list of integers using built_in sorted()"""
        print(sorted(self))
