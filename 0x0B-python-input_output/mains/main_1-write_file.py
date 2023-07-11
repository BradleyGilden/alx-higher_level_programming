#!/usr/bin/python3
import sys


sys.path.append("/home/nightlock/workspace/Python/alx-higher_level_programming/0x0B-python-input_output")
write_file = __import__('1-write_file').write_file

nb_characters = write_file("text_files/my_first_file.txt", "กรุงเทพมหานคร\n")
print(nb_characters)
