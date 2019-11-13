import unittest


'''
https://www.ideserve.co.in/learn/last-index-of-element-in-sorted-array-with-duplicates

Given a sorted array of integers containing duplicates, write a program which returns the last index of an element.

Example:
Input:
array = {0, 1, 2, 2, 4, 5, 5, 5, 8};
num = 5;
Output:
Element 5 found at index 7
'''

def findLastIndexInSortedArrayWithDuplicates(arr, elem):
    start = 0
    end = len(arr) - 1
    if end < start or elem < arr[start] or elem > arr[end]:
        return -1
        
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == elem:
            if mid == end or arr[mid+1] != arr[mid]:
                return mid
            else:
                start = mid+1
        elif arr[mid] < elem:
            # now we have to find in the right side
            start = mid+1
        else:
            end = mid-1
    return -1



class CodeTest(unittest.TestCase):


    def setUp(self):
        pass

    def testEmptyArrayInput(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([], 4), -1)

    def testElementNotFound(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([0,1,2,2,4,5,5,5,8], 3), -1)
    
    def testElementOutsideStartRange(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([0,1,2,2,4,5,5,5,8], -1), -1)

    def testElementOutsideEndRange(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([0,1,2,2,4,5,5,5,8], 9), -1)

    def testElementExistingSingly(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([0,1,2,2,4,5,5,5,8], 1), 1)

    def testElementExistingAsDuplicate(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([0,1,2,2,4,5,5,5,8], 5), 7)

    def testLastElementAsNotDuplicate(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([0,1,2,2,4,5,5,5,8], 8), 8)

    def testFirstElementAsNotDuplicate(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([0,1,2,2,4,5,5,5,8], 0), 0)

    def testLastElementAsDuplicate(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([0,1,2,2,4,5,5,5,8, 8], 8), 9)

    def testFirstElementAsDuplicate(self):
        self.assertEqual(findLastIndexInSortedArrayWithDuplicates([0,0,1,2,2,4,5,5,5,8], 0), 1)

unittest.main()