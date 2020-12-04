import unittest
from simplecaesar import encode, decode

class SCCipherTest(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode('ABC'), 'DEF')

    def test_encode_long(self):
        self.assertEqual(encode('A big house'), 'D elj krxvh')

    def test_decode(self):
    	self.assertEqual(decode('DEF'), 'ABC')

    def test_decode_long(self):
        self.assertEqual(decode('Wkh voB uhg irA'), 'The sly red fox')

    def test_null(self):
    	self.assertEqual(encode(''), '')

    def test_reflex(self):
    	self.assertEqual(decode(encode('Reflexive Property')), 'Reflexive Property')

