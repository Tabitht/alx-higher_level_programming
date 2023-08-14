#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        print(' '.join("{:d}".format(columns) for columns in rows))
