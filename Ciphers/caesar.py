import string

from Ciphers.cipher import Cipher


class Caesar(Cipher):
    FORWARD = string.ascii_uppercase * 3

    name = 'Caesar'

    @classmethod
    def setup(cls, e, d):
        offset = input('Please give me an offset to use with encrypting/decrypting\t')
        try:
            offset = int(offset)
        except ValueError:
            print('Can\'t convert that to an integer. Try again!')
            cls.setup(e, d)
            return
        cipher = cls(offset=offset)

        enc_or_dec = input('Would you like to \033[4mE\033[0mncrypt or decrypt\t')

        if enc_or_dec.lower().startswith('e') or enc_or_dec == '':
            e(cipher)
        else:
            d(cipher)

    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
