#!/usr/bin/python3
""" defines the division of matrix elements """


def matrix_divided(matrix, div):
    """ divides all the element in a matrix.
    args:
        matrix - a list of lists containing int or floats.
        div - the number to be divided with.
    Error to raise:
        TypeError - if not a list of lists of integers or float.
        TypeError - if each row is not the same size.
        TypeError - if div is not an integer or float.
        ZeroDivisionError - if div equals to zero.
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(element, int) or isinstance(element, float))
            for element in [num for row in matrix for num in row]):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) or not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
