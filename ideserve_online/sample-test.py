# reference : https://www.geeksforgeeks.org/unit-testing-python-unittest/


import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)


unittest.main()