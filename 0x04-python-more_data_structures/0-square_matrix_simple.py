#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = []
    for i in matrix:
        result = list(map(lambda x: x**2, i))
        n.append(result)
    return n
