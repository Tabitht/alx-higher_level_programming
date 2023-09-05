#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ mutiplies two matrices using numpy module
    args:
        m_a - first matrix
        m_b - second matrix
    return:
        the new matrix
    """
    return (np.matmul(m_a, m_b))
