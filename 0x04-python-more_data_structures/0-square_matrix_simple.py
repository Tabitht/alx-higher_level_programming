#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for rows in range(len(matrix)):
        new_matrix[rows] = list(map(lambda x: x ** 2, matrix[rows]))
    """ it squares the elements present in each row of the list """
    return new_matrix
