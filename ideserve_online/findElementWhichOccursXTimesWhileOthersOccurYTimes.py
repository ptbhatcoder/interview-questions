import unittest

'''
Find the element that occurs X times in a given set of integers while all the other numbers occur Y times.
Example -  
Input : 3 3 3 4
Output: 4

Input : 5 5 4 8 4 5 8 9 4 8
Output: 9

'''


def findElementWhichOccursXTimesWhileOthersOccurYTimes(arr, x, y):
    n = len(arr)
    if not n:
        return None
    expectedBitCount = y % x
    if not expectedBitCount:
        return None
    if n % x != expectedBitCount:
        return None

    maxVal = max(arr)
    if not maxVal:
        return None

    p = 1
    bitCount = 0
    while p <= maxVal:
        bitCount += 1
        p <<= 1

    bits = [0] * bitCount
    for elem in arr:
        v = 1
        for i in range(len(bits)):
            if v & elem:
                bits[i] += 1
            v <<= 1

    bits = list(map(lambda a: a % x, bits))
    missingVal = 0
    for i in range(len(bits)):
        if bits[i] != expectedBitCount and bits[i] != 0:
            return None
        if bits[i]:
            missingVal += (2**i)
    return missingVal


class CodeTest(unittest.TestCase):
    def testEmpty(self):
        self.assertIsNone(
            findElementWhichOccursXTimesWhileOthersOccurYTimes([], 5, 2))

    def testXIsSameAsY(self):
        self.assertIsNone(findElementWhichOccursXTimesWhileOthersOccurYTimes(
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5], 5, 5))

    def testIncorrectLengthWhenXGreaterThanY(self):
        self.assertIsNone(findElementWhichOccursXTimesWhileOthersOccurYTimes(
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 8, 8, 8], 5, 2))

    def testIncorrectLengthWhenXLessThanY(self):
        self.assertIsNone(findElementWhichOccursXTimesWhileOthersOccurYTimes(
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 8, 8, 8], 5, 7))

    def testMaxZeroWhenXLessThanY(self):
        self.assertIsNone(
            findElementWhichOccursXTimesWhileOthersOccurYTimes([0] * 12, 5, 7))

    def testCorrectInputXGreaterThanY(self):
        self.assertEqual(findElementWhichOccursXTimesWhileOthersOccurYTimes(
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 8, 8, 8], 5, 3), 8)

    def testCorrectInputXLessThanY(self):
        self.assertEqual(findElementWhichOccursXTimesWhileOthersOccurYTimes(
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 8, 8, 8, 8, 8, 8, 8, 8], 5, 8), 8)


unittest.main()
