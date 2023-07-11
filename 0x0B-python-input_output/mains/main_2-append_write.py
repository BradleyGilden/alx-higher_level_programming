#!/usr/bin/python3
import sys


sys.path.append("/home/nightlock/workspace/Python/alx-higher_level_programming/0x0B-python-input_output")
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("text_files/file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
