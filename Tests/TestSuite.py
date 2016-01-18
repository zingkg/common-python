import unittest
from Tests.PrivateKeyTests import PrivateKeyTests
from Tests.PublicKeyTests import PublicKeyTests
from Tests.RSATests import RSATests

__author__ = 'zingkg'

suite = unittest.TestSuite()
suite.addTest(PrivateKeyTests())
suite.addTest(PublicKeyTests())
suite.addTest(RSATests())
unittest.TextTestRunner().run(suite)
