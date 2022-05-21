'''
Write a function that accepts a square matrix (N x N 2D array) 
and returns the determinant of the matrix.
'''
import numpy as np
# import sympy

def determinant(m):
    det = round(np.linalg.det(m), 5)
    # reduced row echelon form 
    # m = sympy.Matrix(m).rref()
    # diagonal product
    # det = np.diag(m).prod()
    return det
