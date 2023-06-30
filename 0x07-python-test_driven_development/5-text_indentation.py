#!/usr/bin/python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 29-06-2023
"""


def text_indentation(text):
    """prints 2 newlines after the characters: '.', '?' and ':'

    Args:
        text(str): text to be formatted

    Raises:
        TypeError: if {text} is not of type str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text.strip(" ") == "":
        return

    temp = ""
    start = 0
    tlen = len(text)

    for i in range(tlen):
        if text[i] in ".?:" and start < tlen:
            temp = text[start: i + 1].strip(" ")
            start = i + 1
            print(temp, end="\n\n")

    if text[start:].strip(" ") != "":
        print(text[start:].strip(" "), end="")
