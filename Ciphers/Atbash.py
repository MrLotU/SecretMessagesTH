from cipher import Cipher
from Affine import Affine

class Atbash(Cipher):
    name = 'Atbash'

    def __init__(self):
        self.affine = Affine(25, 25)

    def alphabet(self):
        return self.affine.alphabet()
    
    def encrypt(self, msg):
        return self.affine.encrypt(msg)

    def decrypt(self, msg):
        return self.affine.decrypt(msg)