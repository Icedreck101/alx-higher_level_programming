#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for i in matrix:
        squared.append([element**2 for element in line])
    return squared
