#!/usr/bin/python3
from sys import argv


"""
This program lists all program arguments in argv
They are numbered starting from 0
"""
if __name__ == "__main__":
    a_len = len(argv)

    if a_len <= 1:
        print("0 arguments.")
    else:
        if a_len == 2:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(a_len - 1))
        for i in range(1, a_len):
            print("{:d}: {}".format(i, argv[i]))
