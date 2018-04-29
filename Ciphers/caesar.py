import string

from Ciphers.cipher import Cipher


class Caesar(Cipher):
    """Class for the Caesar Cipher"""
    FORWARD = string.ascii_uppercase * 3

    name = 'Caesar'

    @classmethod
    def setup(cls, e, d, inp):
        """Setup Caesar Cipher for use"""
        ### Get required data to instantiate cipher (offset)
        offset = inp('Please give me an offset to use with encrypting/decrypting\t')
        try:
            offset = int(offset)
        except ValueError:
            print('Can\'t convert that to an integer. Try again!')
            cls.setup(e, d)
            return
        ### Instantiate cipher
        cipher = cls(offset=offset)

        ### Ask if we want to encrypt or decrypt
        enc_or_dec = inp('Would you like to \033[4mE\033[0mncrypt or decrypt\t')

        ### Start encryption or decryption flow
        if enc_or_dec.lower().startswith('e') or enc_or_dec == '':
            e(cipher)
        else:
            d(cipher)

    def __init__(self, offset=3):
        """Initialize Caesar Cipher"""
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text):
        """Encrypt a message using the Caesar Cipher"""
        output = []
        ### Uppercase the message
        text = text.upper()
        ### Convert every character
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        ### Return encrypted message
        return ''.join(output)

    def decrypt(self, text):
        output = []
        ### Uppercase the message
        text = text.upper()
        ### Convert every character
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        ### Return decrypted message
        return ''.join(output)
