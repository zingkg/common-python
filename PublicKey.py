__author__ = 'zingkg'

class PublicKey(object):
    def __init__(self, modulus, coprime):
        self.modulus = long(modulus)
        self.coprime = long(coprime)

    def encrypt(self, message):
        return long(long(message) ** self.coprime % self.modulus)
