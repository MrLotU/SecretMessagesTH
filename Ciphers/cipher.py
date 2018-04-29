class Cipher:
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    name = ''

    def __str__(self):
        return self.name.lower()