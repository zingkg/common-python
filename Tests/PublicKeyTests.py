import unittest
from PublicKey import PublicKey

__author__ = 'zingkg'

class PublicKeyTests(unittest.TestCase):
    def runTest(self):
        self.test_assignment()

    def test_assignment(self):
        public_key = PublicKey(5, 23)
        self.assertEquals(public_key.modulus, 5)
        self.assertEquals(public_key.coprime, 23)
