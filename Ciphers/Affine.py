from cipher import Cipher

class Affine(Cipher):
    name = 'Affine'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def setup(cls, e, d):
        a = raw_input('Please give me an a to use with encrypting/decrypting\t')
        b = raw_input('Please give me a b to use with encrypting/decrypting\t')
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            print('Can\'t convert that to an integer. Try again!')
            cls.setup(e, d)
            return
        possible_a_values = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        if not a in possible_a_values:
            print('a should be one of the following: {}'.format(', '.join(possible_a_values)))
            cls.setup(e, d)
            return
        cipher = cls(a, b)

        enc_or_dec = raw_input('Would you like to \033[4mE\033[0mncrypt or decrypt\t')

        if enc_or_dec.lower().startswith('e') or enc_or_dec == '':
            e(cipher)
        else:
            d(cipher)
    
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