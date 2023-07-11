#!/usr/bin/python3

"""
This module is a script that reads from stdin and computes metrics

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""


def print_stats(size, codes):
    """display all metrics.

    Args:
        size (int): total readfile size.
        codes (dict): count of status codes
    """
    print("File size: {}".format(size))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if codes.get(line[-2], -1) == -1:
                        codes[line[-2]] = 1
                    else:
                        codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, codes)

    except KeyboardInterrupt:
        print_stats(size, codes)
        raise
