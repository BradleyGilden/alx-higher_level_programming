#!/usr/bin/python3

"""
this module contains pascal_triangle()

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""


def pascal_triangle(n):
    """returns a nested list of integers of n rows of pascals triangle

    Args:
        n(int): number of rows
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(1, n+1):
        triangle.append([])
        for j in range(i):
            if j == 0 or j == i - 1:
                triangle[i-1].append(1)
            else:
                triangle[i-1].append((triangle[i-2][j-1] + triangle[i-2][j]))

    return triangle
