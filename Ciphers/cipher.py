class Cipher:
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    @classmethod
    def setup(cls, e, d):
        raise NotImplementedError()

    name = ''

    def __str__(self):
        return self.name.lower()