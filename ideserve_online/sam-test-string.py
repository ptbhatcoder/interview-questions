import unittest

class StringTest(unittest.TestCase):
    def setUp(self):
        pass

    def testCharMultiply(self):
        self.assertEqual('a'*4, 'aaaa')

    def testUpperCase(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def testIsUpper(self):
        self.assertFalse('foo'.isupper())
        self.assertTrue('FOO'.isupper())
    
    def testStrip(self):
        self.assertEqual('abcdefghijk'.strip('abcd'), 'efghijk')

    def testSplit(self):
        self.assertEqual('some person'.split(' '), ['some', 'person'])
        with self.assertRaises(TypeError):
            'abcd'.split(2)
    
unittest.main()