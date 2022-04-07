'''
Create two functions to encode and then decode a string using the Rail Fence Cipher. 
This cipher is used to encode a string by placing each character successively 
in a diagonal along a set of "rails". First start off moving diagonally and down. 
When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. 
Continue until you reach the end of the string. 

Each "rail" is then read left to right to derive the encoded string.

Write a function/method that takes 2 arguments, 
a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, 
an encoded string and the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 
and that passing an empty string will return an empty string.

 Don't filter out punctuation as they are a part of the string.
'''

def encode_rail_fence_cipher(s, n):
    encoded_str = ''
    m = [['']*len(s) for x in range(n)]
    down = False
    row, col = 0, 0 
    for a in range(len(s)):
        # check current row, if top or bottom reverse direction 
        if (row == 0) or (row == n-1):
            down = not down
        # assign element
        m[row][col] = s[a]
        # update position
        col+=1
        if down == True:
            row+=1
        else:
            row-=1
    # combine elements in m
    for k in m:
        for j in k:
            if j != '':
                encoded_str += j
    return encoded_str


def decode_rail_fence_cipher(s, n):
    m = [['']*len(s) for x in range(n)]
    # fill matrix with * in zigzag
    down = False
    row, col = 0, 0
    for i in range(len(s)):
        if (row == 0) or (row == n-1):
            down = not down
        m[row][col] = '*'
        col+=1
        if down == True:
            row+=1
        else:
            row-=1

    # loop matrix, if * place letter
    idx = 0
    for j in range(n):
        for k in range(len(s)):
            if m[j][k] == '*':
                m[j][k] = s[idx]
                idx+=1

    # read matrix in zigzag
    down = False
    row, col = 0, 0 
    decoded_str = ''
    for a in range(len(s)):
        if (row == 0) or (row == n-1):
            down = not down
        decoded_str = decoded_str + m[row][col]
        col+=1
        if down == True:
            row+=1
        else:
            row-=1

    return decoded_str


    











encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3) # "WECRLTEERDSOEEFEAOCAIVDEN")
encode_rail_fence_cipher("Hello, World!", 3) # "Hoo!el,Wrdl l"
decode_rail_fence_cipher("H !e,Wdloollr", 4) # "Hello, World!")
decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3) # "WEAREDISCOVEREDFLEEATONCE")
decode_rail_fence_cipher("", 3) # "")
