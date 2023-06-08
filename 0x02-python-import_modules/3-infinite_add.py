#!/usr/bin/python3
from sys import argv


# This program prints an infinite sum of arguments in the argv list.
if __name__ == '__main__':
    sum = 0
    a_len = len(argv)

    if a_len > 1:
        for i in range(1, a_len):
            sum += int(argv[i])

    print(sum)
