from Ciphers.cipher import Cipher

class Polybius(Cipher):
    """Class for the Polybius Cipher"""
    name = 'Polybius'

    def __init__(self, pad):
        ### Create the a grid or type (x, y): character
        self.grid = {
            (x, y): z for (x, y), z in zip(
                [(1*a, 1*b) for a in range(1, 6) for b in range(1, 6)], 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
            )
        }
        self.pad = pad

    @classmethod
    def setup(cls, e, d, inp, pad):
        """Setup the Polybius Cipher for use"""
        ### Setup pad
        p = 0
        if not pad == None:
            for c in pad.upper():
                p += ord(c)
        ### Instantiate cipher
        cipher = cls(p)

        ### Ask if we want to encrypt or decrypt
        enc_or_dec = inp('Would you like to \033[4mE\033[0mncrypt or decrypt\t')

        ### Start encryption or decryption flow
        if enc_or_dec.lower().startswith('e') or enc_or_dec == '':
            e(cipher)
        else:
            d(cipher)
    
    def encrypt(self, msg):
        """Encrypt a message using the Polybius Cipher"""
        ### Convert the message to all uppercase
        msg = msg.upper()
        ### Replace all W's with V's since the W didn't fit in our 5*5 square
        msg = msg.replace('W', 'V')
        out = []
        ### Loop over characters and find the coords that go with it
        for char in msg:
            for coord, letter in self.grid.items():
                if letter == char:
                    x, y = coord
                    out.append('{}{}'.format(x, y))
        ### Return the encrypted message
        return ' '.join(out)
    
    def decrypt(self, msg):
        """Decrypt a message using the Polybius Cipher"""
        out = []
        ### Get character for each set of coordinates we recieve
        for char in msg.split(' '):
            x, y = tuple(list(char))
            try:
                x = int(x)
                y = int(y)
            except ValueError:
                return 'Invalid code provided!'
            out.append(self.grid[(x, y)])
        ### Return the decrypted message
        return ''.join(out)