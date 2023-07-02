#!/usr/bin/python3

"""
This repo contains matrix_mul() which returns the result of 2 multiplied
matrices

Author: Bradley Dillion Gilden
Date: 01-07-2023
"""


def matrix_mul(m_a, m_b):
    """returns multiplied matrix: m_a * m_b

    Args:
        m_a(list): a list matrix of int/float
        m_b(list): a list matrix of int/float

    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: m_a is not a list of lists
        TypeError: if an element of m_a or m_b is not a an int/float
        TypeError: if m_a or m_b are not rectangular matrices
        ValueError: if m_a or m_b is empty (==[] or ==[[]])
        ValueError: if m_a and m_b can't be multiplied: m_a.rows != m_b.cols
    """
    if not isinstance(m_a, list):  # checking validity of m_a
        raise TypeError("m_a must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not (all((isinstance(item, int) or isinstance(item, float)))
            for row in m_a for item in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not isinstance(m_b, list):  # checking validity of m_b
        raise TypeError("m_b must be a list")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not (all((isinstance(item, int) or isinstance(item, float)))
            for row in m_b for item in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):  # checking validity of multiplication
        raise ValueError("m_a and m_b can't be multiplied")

    m_list = []
    for i in range(len(m_a)):
        m_list.append([])
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_a[0])):
                sum += m_a[i][k] * m_b[k][j]
            m_list[i].append(sum)
    return m_list
