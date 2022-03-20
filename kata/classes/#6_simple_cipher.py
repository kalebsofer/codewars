class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2
        self.ls = []
        self.ls2 = []
    
    def encode(self, s):
        # if character not in map, leave as is
        [self.ls.append(self.map1.index(i)) if i in self.map2 else self.ls.append(i) for i in s]
        [self.ls2.append(self.map2[j]) if type(j)==int else self.ls2.append(j) for j in self.ls]
        s = ''.join(self.ls2)
        self.ls, self.ls2 = [], []
        return s
    
    def decode(self, s):
        [self.ls.append(self.map2.index(i)) if i in self.map1 else self.ls.append(i) for i in s]
        [self.ls2.append(self.map1[j]) if type(j)==int else self.ls2.append(j) for j in self.ls]
        s = ''.join(self.ls2)
        self.ls, self.ls2 = [], []
        return s


class Cipher(object):
    def __init__(self, map1, map2): 
        self.m1 = map1
        self.m2 = map2
    def encode(self, s): 
        return ''.join([self.m2[self.m1.index(i)] if i in self.m1 else i for i in s])
    def decode(self, s): 
        return ''.join([self.m1[self.m2.index(i)] if i in self.m1 else i for i in s])


map1 = "abcdefghijklmnopqrstuvwxyz"
map2 = "etaoinshrdlucmfwypvbgkjqxz"

cipher = Cipher(map1, map2)

cipher.encode("abc") #"eta"
cipher.encode("xyz") # "qxz"
cipher.encode('a_bc&*83') # 't_fo&*83'

cipher.decode("eirfg") # "aeiou"
cipher.decode("erlang") # "aikcfu"

map2 = 'tfozcivbsjhengarudlkpwqxmy';
cipher = Cipher(map1, map2);
cipher.encode('abc') # 'tfo'
cipher.decode('tfo') # 'abc'
cipher.decode('kjpphi') # 'tjuukf'