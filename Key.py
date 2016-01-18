from PrivateKey import PrivateKey
from PublicKey import PublicKey

__author__ = 'zingkg'

class Key(object):
    def __init__(self, modulus, coprime, multiplicative_inverse):
        self.public_key = PublicKey(modulus, multiplicative_inverse)
        self.private_key = PrivateKey(modulus, coprime)

    def encrypt(self, message):
        return self.public_key.encrypt(message)

    def decrypt(self, cipher):
        return self.private_key.decrypt(cipher)
