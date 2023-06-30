#!/usr/bin/python3

"""
This module contains a function that divides a matrix

Author: Bradley Dillion Gilden
Date: 29-06-2023
"""


def matrix_divided(matrix, div):
    """
    This function divides all matrix elements of 'matrix' by 'div'. All
    elements are rounded to 2 decimal places

    Args:
    div(int / float): matrix divisor
    matrix(int / float): matrix to be divided

    Raises:
        TypeError - if matrix is not a list of list of ints or floats
        TypeError - if each row of matrix is not the same size
        TypeError - if div is not an int or float
        ZeroDivisionError - if div is 0

    Returns:
        copy of a new matrix with <matrix elements> / div
    """
    if (not isinstance(matrix, list) or not matrix or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(item, int) or isinstance(item, float))
                for item in [col for row in matrix for col in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num/div, 2) for num in row] for row in matrix]
