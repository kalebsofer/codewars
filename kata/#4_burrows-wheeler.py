'''
following hints:

The output contains the last matrix column.
The first column can be acquired by sorting the last column.
For every row of the table: 
    Symbols in the first column follow on symbols in the last column, 
    in the same way they do in the input string.
You don't need to reconstruct the whole table to get the input back.

'''
from collections import deque
import string
import numpy as np

def encode(s: str):
    if len(s) == 0:
        return '', 0
    else:
        row1 = deque(list(s))
        matrix = []
        for i in s:
            row1.rotate(1)
            matrix.append(list(row1))
        for i in sorted(matrix): 
            if ''.join(i) == s:
                idx = sorted(matrix).index(i)
        last_c = ''.join([k[-1] for k in sorted(matrix)])
        return last_c, idx 

def decode(s, n):
    a = list(s)
    b = sorted(a)
    while len(b[0]) < len(s):    
        b = [(m+n) for m,n in zip(a,b)]
        b = sorted(b)

    return b[n]

encode("bananabar") # ('nnbbraaaa', 4)
encode("Humble Bundle") #('e emnllbduuHB', 2)
encode("Mellow Yellow") # ('ww MYeelllloo', 1)
decode("nnbbraaaa", 4) # "bananabar" 




