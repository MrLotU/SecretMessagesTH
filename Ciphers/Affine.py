from cipher import Cipher

class Affine(Cipher):
    name = 'Affine'

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def alphabet(self):
        alphabet = {}
        for i in range(26):
            alphabet[chr(i+65)] = chr(((self.a*i+self.b)%26)+65)
        return alphabet

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(self):
        g, x, y = self.egcd(self.a, 26)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % 26
    
    def encrypt(self, msg):
        msg = msg.upper()
        out = []
        for char in msg:
            out.append(chr(((self.a * (ord(char) - 65) + self.b) % 26) + 65))
        return ''.join(out)

    def decrypt(self, msg):
        msg = msg.upper()
        out = []
        for char in msg:
            out.append(chr((self.modinv() * ((ord(char) - 65) - self.b) % 26) + 65))
        return ''.join(out)