class Cipher():
    """Base Cipher class"""
    def encrypt(self, msg):
        """Encrypt a message"""
        raise NotImplementedError()

    def decrypt(self, msg):
        """Decrypt a message"""
        raise NotImplementedError()

    @classmethod
    def setup(cls, e, d, inp, pad):
        """Setup a cipher for use"""
        raise NotImplementedError()

    ### Name of the cipher
    name = ''

    def __str__(self):
        """Get the name of the Cipher"""
        return self.name.lower()
