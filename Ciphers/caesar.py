import string

from Ciphers.cipher import Cipher


class Caesar(Cipher):
    """Class for the Caesar Cipher"""
    # FORWARD = string.ascii_uppercase * 3

    name = 'Caesar'

    @classmethod
    def setup(cls, e, d, inp, pad):
        """Setup Caesar Cipher for use"""
        ### Get required data to instantiate cipher (offset)
        offset = inp('Please give me an offset to use with encrypting/decrypting\t')
        try:
            offset = int(offset)
        except ValueError:
            print('Can\'t convert that to an integer. Using default')
            offset = 3
        ### Setup pad
        p = 0
        if not pad == None:
            for c in pad.upper():
                p += ord(c)
        ### Instantiate cipher
        cipher = cls(p, offset=offset)

        ### Ask if we want to encrypt or decrypt
        enc_or_dec = inp('Would you like to \033[4mE\033[0mncrypt or decrypt\t')

        ### Start encryption or decryption flow
        if enc_or_dec.lower().startswith('e') or enc_or_dec == '':
            e(cipher)
        else:
            d(cipher)

    def __init__(self, pad, offset=3):
        """Initialize Caesar Cipher"""
        self.offset = offset
        self.pad = pad

    def encrypt(self, text):
        """Encrypt a message using the Caesar Cipher"""
        output = []
        ### Uppercase the message
        text = text.upper()
        ### Convert every character
        for char in text:
            index = ord(char) - 65
            index += self.offset + self.pad
            output.append(chr((index % 26) + 65))
            print(self.offset, self.pad, index)
        ### Return encrypted message
        return ''.join(output)

    def decrypt(self, text):
        output = []
        ### Uppercase the message
        text = text.upper()
        ### Convert every character
        for char in text:
            index = ord(char) - 65
            index -= self.offset + self.pad
            output.append(chr((index % 26) + 65))
        ### Return decrypted message
        return ''.join(output)
