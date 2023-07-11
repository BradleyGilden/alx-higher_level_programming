#!/usr/bin/python3

"""
This module contains append_after() function

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""


def append_after(filename="", search_string="", new_string=""):
    """appends {new_string} after {search_string} in file {filename}

    Args:
        filename(str): name of file
        search_string(str): string to append after
        new_string(str): contents to append
    """
    contents = []
    with open(filename, "r+", encoding="utf-8") as file:
        for line in file:
            contents.append(line)
        file.seek(0)
        for i, line in enumerate(contents):
            if search_string in line:
                contents.insert(i + 1, new_string)
        new_string = "".join(contents)
        file.write(new_string)
