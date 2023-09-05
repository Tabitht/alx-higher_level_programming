#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """ multiplies two matrices
    args:
        m_a - first mattrix
        m_b - second matrix
    Error to raise:
        TypeError - if m_a or m_b is not a list of lists
        TypeError - if m_a or m_b is not a list of integer or float
        TypeError - if the rows in the matrix are not same size
        ValueError - if any or both of the matrix is empty
        ValueError - if the matrix cannot be multiplied
    Returns:
        the new matrix that has been multiplied
    """
    if (not isinstance(m_a, list)):
        raise TypeError(" m_a must be a list")
    if (not isinstance(m_b, list)):
        raise TypeError(" m_b must be a list")
    if (not all(isinstance(row, list) for row in m_b)):
        raise TypeError(" m_a must be a list of lists")
    if (not all(isinstance(row, list) for row in m_b)):
        raise TypeError(" m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if (not all(isinstance(i, int) or isinstance(i, float))
            for i in [i for row in m_a for i in row]):
        raise TypeError("m_a should contain only integers or floats")
    if (not all(isinstance(i, int) or isinstance(i, float))
            for i in [i for row in m_b for i in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_a):
        raise ValueError("m_a and m_b can't be multiplied")
    inverse_b = []
    for columns in range(len(m_b[0])):
        row_b = []
        for rows in range(len(m_b)):
            row_b.append(m_b[rows][columns])
        inverse_b.append(row_b)
    new_matrix = []
    for r in m_a:
        new_row = []
        for c in inverse_b:
            product = 0
            for k in range(len(inverse_b[0])):
                product += c[k] * r[k]
            new_row.append(product)
        new_matrix.append(new_row)
    return new_matrix
