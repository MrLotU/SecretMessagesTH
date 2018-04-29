from cipher import Cipher

class Polybius(Cipher):
    name = 'Polybius'

    def __init__(self):
        self.grid = {(x, y): z for (x, y), z in zip([(1*a, 1*b) for a in range(1, 6) for b in range(1, 6)], 'ABCDEFGHIJKLMNOPQRSTUVXYZ')}

    @classmethod
    def setup(cls, e, d):
        cipher = cls()

        enc_or_dec = raw_input('Would you like to \033[4mE\033[0mncrypt or decrypt\t')

        if enc_or_dec.lower().startswith('e') or enc_or_dec == '':
            e(cipher)
        else:
            d(cipher)
    
    def encrypt(self, msg):
        msg = msg.upper()
        out = []
        for char in msg:
            for coord, letter in self.grid.items():
                if letter == char:
                    x, y = coord
                    out.append('{}{}'.format(x, y))
        return ' '.join(out)
    
    def decrypt(self, msg):
        out = []
        for char in msg.split(' '):
            x, y = tuple(list(char))
            try:
                x = int(x)
                y = int(y)
            except ValueError:
                return 'Invalid code provided!'
            out.append(self.grid[(x, y)])
        return ''.join(out)