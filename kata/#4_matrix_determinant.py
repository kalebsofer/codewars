'''
Write a function that accepts a square matrix (N x N 2D array) 
and returns the determinant of the matrix.
'''

# reduce to row echelon
# pivot off top left 
# pivot off frst non-zero in second row
# pivots must be 1, and 0 above & below every pivot
# take diagonal product 

import numpy as np
import sympy



def determinant(m):
    np.linalg.det(m)
    # reduced row echelon form 
    # m = sympy.Matrix(m).rref()
    # diagonal product
    # det = np.diag(m).prod()
    return det
