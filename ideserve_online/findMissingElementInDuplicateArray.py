import unittest
import functools

'''

https://www.ideserve.co.in/learn/find-the-missing-number-in-the-duplicate-array

Given two integer arrays where second array is duplicate of first array with just 1 element missing. Find the element.
Example:

Input:
Array1 - 9 7 8 5 4 6 2 3 1
Array2 - 2 4 3 9 1 8 5 6

Output:
7
'''


def findMissingElementInDuplicateArray(arr, duplicate):
    if not len(arr) or len(arr) != len(duplicate) + 1:
        return None
    missing = functools.reduce(lambda x, y: x ^ y, arr+duplicate, 0)
    if missing or (missing in arr and missing not in duplicate):
        return missing
    return None


class CodeTest(unittest.TestCase):
    def testEmptyArray(self):
        self.assertIsNone(findMissingElementInDuplicateArray([], []))

    def testInvalidDup(self):
        self.assertIsNone(findMissingElementInDuplicateArray([1, 2, 3], [1]))

    def testInvalidLargerDup(self):
        self.assertIsNone(
            findMissingElementInDuplicateArray([1, 2, 3], [1, 2, 3]))

    def testZeroAsAnswer(self):
        self.assertEqual(findMissingElementInDuplicateArray(
            [1, 2, 3, 0], [1, 2, 3]), 0)

    def testNonZeroAsValidAnswer(self):
        self.assertEqual(findMissingElementInDuplicateArray(
            [1, 2, 3, 4], [1, 2, 3]), 4)


unittest.main()
