__author__ = 'zingkg'

class PrivateKey(object):
    def __init__(self, modulus, multiplicative_inverse):
        self.modulus = long(modulus)
        self.multiplicative_inverse = long(multiplicative_inverse)

    def decrypt(self, cipher):
        return long(long(cipher) ** self.multiplicative_inverse % self.modulus)

    def __findpowmax__(self, cipher):
        cipher_sum = cipher
        for i in range(self.multiplicative_inverse):
            if cipher_sum > self.modulus:
                return i + 1
            else:
                cipher_sum *= cipher

    def __blockmod__(self, cipher, step):
        message = cipher
        for i in range(1, step):
            message *= cipher
        return message % self.modulus
