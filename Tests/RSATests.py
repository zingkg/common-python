import unittest
import RSA

__author__ = 'zingkg'

def encrypt_and_decrypt(key, message):
    cipher = key.encrypt(message)
    return key.decrypt(cipher)

class RSATests(unittest.TestCase):
    def runTest(self):
        self.test_rsa()
        self.test_rsa_random()

    def test_rsa(self):
        key = RSA.generate_key(661, 547)
        self.assertEquals(255, encrypt_and_decrypt(key, 255))

    def test_rsa_random(self):
        key = RSA.generate_random_key()
        self.assertEquals(651, encrypt_and_decrypt(key, 651))
