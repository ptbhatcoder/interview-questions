import unittest

'''
Find the element that occurs only once in a given set of integers while all the other numbers occur thrice.
Example -  
Input : 3 3 3 4
Output: 4

Input : 5 5 4 8 4 5 8 9 4 8
Output: 9

'''


def findElementWhichOccursOnceWhileOthersOccurThrice(arr):
    n = len(arr)
    if not n or n % 3 != 1:
        return None

    maxVal = max(arr)
    if not maxVal:
        return None

    p = 1
    bitCount = 0
    while p < maxVal:
        bitCount += 1
        p <<= 1

    bits = [0] * bitCount
    for elem in arr:
        v = 1
        for i in range(len(bits)):
            if v & elem:
                bits[i] += 1
            v <<= 1
    bits = list(map(lambda x: x % 3, bits))
    missingVal = 0
    for i in range(len(bits)):
        if bits[i] > 1:
            return None
        if bits[i]:
            missingVal += (2**i)
    return missingVal


class CodeTest(unittest.TestCase):
    def testEmpty(self):
        self.assertIsNone(findElementWhichOccursOnceWhileOthersOccurThrice([]))

    def testIncorrectLength(self):
        self.assertIsNone(findElementWhichOccursOnceWhileOthersOccurThrice(
            [1, 1, 1, 2, 2, 5, 5, 5, 3, 3, 3]))

    def testTwoElementsOccuringTwice(self):
        # note the length is still 3x + 1
        self.assertIsNone(findElementWhichOccursOnceWhileOthersOccurThrice(
            [1, 1, 1, 2, 2, 5, 5, 5, 3, 3, 3, 4, 4]))

    def testMaxZero(self):
        # note the length is still 3x + 1
        self.assertIsNone(
            findElementWhichOccursOnceWhileOthersOccurThrice([0, 0, 0, 0, 0, 0, 0]))

    def testOnlyOneElementOccursOnce(self):
        self.assertEqual(findElementWhichOccursOnceWhileOthersOccurThrice(
            [1, 1, 1, 2, 5, 5, 5, 3, 3, 3]), 2)


unittest.main()
