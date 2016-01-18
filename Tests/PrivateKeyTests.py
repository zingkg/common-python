import unittest

from PrivateKey import PrivateKey

__author__ = 'zingkg'

class PrivateKeyTests(unittest.TestCase):
    def runTest(self):
        self.test_assignment()

    def test_assignment(self):
        private_key = PrivateKey(5, 3)
        self.assertEquals(private_key.modulus, 5, 'Assignment should equal')
        self.assertEquals(private_key.multiplicative_inverse, 3)
