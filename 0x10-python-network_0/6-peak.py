#!/usr/bin/python3

"""
This module contains only find_peak() which finds peak of unsorted list

Author: Bradley Dillion Gilden
Date: 28-09-2023
"""


def find_peak(list_of_integers):
    """finds peak of unsorted list of integers"""
    size = len(list_of_integers)
    if (size == 1):
        return list_of_integers[0]
    for i in range(size):
        j = i if i - 1 < 0 else i - 1
        k = i if i + 1 >= size else i + 1
        if (list_of_integers[i] >= list_of_integers[j] and
                list_of_integers[i] >= list_of_integers[k]):
            return list_of_integers[i]
    return None


if __name__ == '__main__':
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
