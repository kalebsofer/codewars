# Write a class that, when given a string, 
# will return an uppercase string with each 
# letter shifted forward in the alphabet by 
# however many spots the cipher was initialized to.
import string
from collections import deque

abc = list(string.ascii_lowercase)
st = 'C*d£wars'


class CaesarCipher(object):

    def __init__(self, shift: int):
        self.shift = shift
        self.abc = list(string.ascii_lowercase)
        self.n = []

    def encode(self, st):
        bca = deque(self.abc)
        bca.rotate(-self.shift)
        [self.n.append(bca[self.abc.index(i)]) if i in self.abc else self.n.append(i) for i in st.lower()]
        new = ''.join(self.n).upper()
        self.n = []
        return new
        
    def decode(self, st):
        bca = deque(self.abc)
        bca.rotate(self.shift)
        [self.n.append(bca[self.abc.index(i)]) if i in self.abc else self.n.append(i) for i in st.lower()]
        new = ''.join(self.n).upper()
        self.n = []
        return new



c = CaesarCipher(5)
 
c.encode('Codewars') # 'HTIJBFWX'
c.encode('C*d£wars') # H*T£BFWX

c.decode('HTIJBFWX') # 'CODEWARS'

