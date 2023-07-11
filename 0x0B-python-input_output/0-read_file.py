#!/usr/bin/python3

"""
This module contains read_file() for reading files

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""


def read_file(filename=""):
    """reads file and displays contents out to the screen

    Args:
        filename(str): name of file to be read
    """

    with open(filename, "r", encoding="ascii") as file:
        for line in file:
            print(line, end="")
