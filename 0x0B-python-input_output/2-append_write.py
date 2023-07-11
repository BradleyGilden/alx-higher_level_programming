#!/usr/bin/python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""


def append_write(filename="", text=""):
    """write to file with conditions:
    * Creat file if file does not exist
    * Appends contents of file if file exists

    Args:
        filename(str): name of file to write to
        text(str): contents to write to {filename}

    Returns:
        number of characters written to destination file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
