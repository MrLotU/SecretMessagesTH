from cipher import Cipher
from Affine import Affine

class Atbash(Cipher):
    name = 'Atbash'

    def __init__(self):
        self.affine = Affine(25, 25)

    @classmethod
    def setup(cls, e, d):
        cipher = cls()

        enc_or_dec = raw_input('Would you like to \033[4mE\033[0mncrypt or decrypt\t')

        if enc_or_dec.lower().startswith('e') or enc_or_dec == '':
            e(cipher)
        else:
            d(cipher)

    def alphabet(self):
        return self.affine.alphabet()
    
    def encrypt(self, msg):
        return self.affine.encrypt(msg)

    def decrypt(self, msg):
        return self.affine.decrypt(msg)