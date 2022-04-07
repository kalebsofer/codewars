'''
We have a square matrix M of dimension n x n 
that has positive and negative numbers in the ranges [-9,-1] and [0,9],
( the value 0 is excluded).

We want to add up all the products of the elements 
of the diagonals UP-LEFT to DOWN-BOTTOM, 
that is the value ofsum1; 
and the elements of the diagonals UP-RIGHT to LEFT-DOWN and 
that is sum2. 
Then, as a final result, the value of sum1 - sum2.
'''
import numpy as np

M1 = [[ 1,  4, 7,  6,  5],
     [-3,  2, 8,  1,  3],
     [ 6,  2, 9,  7, -4],
     [ 1, -2, 4, -2,  6],
     [ 3,  2, 2, -4,  7]]

def sum_prod_diags(matrix):
    r, l = 0, 0
    # m = np.matrix(M1)
    for x in range(-len(m), len(m)):
        r += np.diag(m, k=x).prod()
        l += np.diag(np.fliplr(m), k=x).prod()
    
    return r - l


from solution import sum_prod_diags
import codewars_test as test

@test.describe("Basic Tests")
def f():
    @test.it("it should pass basic tests")
    def f():
        M1 = [[ 1,  4, 7,  6,  5],
             [-3,  2, 8,  1,  3],
             [ 6,  2, 9,  7, -4],
             [ 1, -2, 4, -2,  6],
             [ 3,  2, 2, -4,  7]]

        test.assert_equals(sum_prod_diags(M1), 1098)

        M2 = [[ 1,  4, 7,  6],
             [-3,  2, 8,  1],
             [ 6,  2, 9,  7],
             [ 1, -2, 4, -2]]

        test.assert_equals(sum_prod_diags(M2), -11)

        M3 = [[1,2,3,2,1],
              [2,3,4,3,2],
              [3,4,5,4,3],
              [4,5,6,5,4],
              [5,6,7,6,5]]

        test.assert_equals(sum_prod_diags(M3), 0)