#!/usr/bin/python3

"""
contains lazy_matrix_mul that utilizes numpy module to multiply matrices

Author: Bradley Dillion Gilden
Date: 02-07-2023
"""
from numpy import array, matmul


def lazy_matrix_mul(m_a, m_b):
    """returns result of matrix multiplication: m_a * m_b

    Args:
        m_a(list): a list matrix of int/float
        m_b(list): a list matrix of int/float
    """
    matrix_a = array([m_a])
    matrix_b = array([m_b])

    return matmul(matrix_a, matrix_b)
