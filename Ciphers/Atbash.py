from Ciphers.cipher import Cipher
from Ciphers.Affine import Affine

class Atbash(Cipher):
    name = 'Atbash'

    def __init__(self):
        """Initalize Atbash Cipher"""
        ### The atbash cipher is a special form of the Affine cipher with a = b = (m − 1)
        ### In our case where m = 26, we can use our Affine Cipher with a = b = 25
        self.affine = Affine(25, 25)

    @classmethod
    def setup(cls, e, d, inp):
        """Setup Atbash Cipher for use"""
        cipher = cls()

        ### Ask if we want to encrypt or decrypt
        enc_or_dec = inp('Would you like to \033[4mE\033[0mncrypt or decrypt\t')

        ### Start encryption or decryption flow
        if enc_or_dec.lower().startswith('e') or enc_or_dec == '':
            e(cipher)
        else:
            d(cipher)
    
    def encrypt(self, msg):
        """Encrypt message using Atbash Cipher"""
        ### Return message encrypted by underlying Affine Cipher
        return self.affine.encrypt(msg)

    def decrypt(self, msg):
        """Deycrypt message using Atbash Cipher"""
        ### Return message decrypted by underlying Affine Cipher
        return self.affine.decrypt(msg)