#!/usr/bin/python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""


def write_file(filename="", text=""):
    """writes to file with conditions:
    * Creat file if file does not exist
    * Overwrite file if file exists with contents

    Args:
        filename(str): name of file to write to
        text(str): contents to write to {filename}

    Returns:
        number of characters written to destination file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
