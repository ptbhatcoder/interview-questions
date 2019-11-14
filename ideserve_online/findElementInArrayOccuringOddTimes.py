import unittest
import functools

'''

https://www.ideserve.co.in/learn/find-the-number-which-occurs-odd-number-of-times

In an array having positive integers, except for one number which occurs odd number of times, all other numbers occur even number of times. Find the number.
Example -  
Input : 2 5 9 1 5 1 8 2 8
Output: 9

Input : 2 3 4 3 1 4 5 1 4 2 5
Output: 4
'''

def findElementInArrayOccuringOddNumberOfTimes(arr):
    return  functools.reduce(lambda x,y : x^y, arr, 0)


class CodeTest(unittest.TestCase):
    def testEmptyArray(self):
        self.assertEqual(findElementInArrayOccuringOddNumberOfTimes([]), 0)

    def testAllEvenCountArray(self):
        self.assertEqual(findElementInArrayOccuringOddNumberOfTimes([1,1,3,3,2,2,6,6,4,4,3,3,5,5,7,7]), 0)

    def testSingleElementOddCountArray(self):
        self.assertEqual(findElementInArrayOccuringOddNumberOfTimes([1,1,3,3,2,2,6,6,4,4,3,3,5,5,5,7,7]), 5)


unittest.main()