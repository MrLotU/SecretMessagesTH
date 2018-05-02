from Ciphers.cipher import Cipher

class Affine(Cipher):
    """Class for the Affine Cipher"""
    name = 'Affine'

    def __init__(self, a, b, pad):
        """Initialize the Affine Cipher"""
        self.a = a
        self.b = b
        self.pad = pad

    @classmethod
    def setup(cls, e, d, inp, pad):
        """Setup the Affine Cipher"""
        ### Get required data to instantiate cipher (a, b)
        a = inp('Please give me an a to use with encrypting/decrypting\t')
        b = inp('Please give me a b to use with encrypting/decrypting\t')
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            print('Can\'t convert that to an integer. Try again!')
            cls.setup(e, d, inp, pad)
            return
        ### These are all possible values for a. Check if we got a usable input
        possible_a_values = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        if a not in possible_a_values:
            print('a should be one of the following: {}'.format(', '.join(possible_a_values)))
            cls.setup(e, d, inp, pad)
            return
        ### Setup the pad
        p = 0
        if not pad is None:
            for c in pad.upper():
                p += ord(c)
        ### Instantiate cipher
        cipher = cls(a, b, p)

        ### Ask if we want to encrypt or decrypt
        enc_or_dec = inp('Would you like to \033[4mE\033[0mncrypt or decrypt\t')

        ### Start encryption or decryption flow
        if enc_or_dec.lower().startswith('e') or enc_or_dec == '':
            e(cipher)
        else:
            d(cipher)


    def egcd(self, a, b):
        """Implementation of the GCD algorithm"""
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)


    def modinv(self):
        """Get the inversed modulo for our stored a"""
        g, x, y = self.egcd(self.a, 26)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % 26

    def encrypt(self, msg):
        """Encrypt a message using the Affine Cipher"""
        ### Uppercase the message and remove whitespace
        msg = msg.upper()
        msg = ''.join(msg.split())
        out = []
        ### Convert each character
        for char in msg:
            out.append(chr(((self.a * (ord(char) - 65) + (self.b * self.pad)) % 26) + 65))
        ### Return encrypted message
        return ''.join(out)

    def decrypt(self, msg):
        ### Uppercase the message
        msg = msg.upper()
        out = []
        ### Convert each character
        for char in msg:
            out.append(chr((self.modinv() * ((ord(char) - 65) - (self.b * self.pad)) % 26) + 65))
        ### Return decrypted message
        return ''.join(out)
