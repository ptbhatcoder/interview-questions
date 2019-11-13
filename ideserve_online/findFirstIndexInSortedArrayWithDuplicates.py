
import unittest

'''

https://www.ideserve.co.in/learn/first-index-of-element-in-sorted-array-with-duplicates

Given a sorted array of integers containing duplicates, write a program which returns the first index of an element.

Example:
Input:
array = {0, 1, 2, 2, 4, 5, 5, 5, 8};
num = 5;
Output:
Element 5 found at index 5
'''

def findFirstIndexInSortedArrayWithDuplicates(arr, elem):
    start = 0
    end = len(arr) - 1
    
    if end < start or elem < arr[start] or elem > arr[end]:
        return -1
    
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == elem:
            if mid == 0 or arr[mid] != arr[mid-1]:
                return mid
            else:
                end = mid-1
        elif arr[mid] < elem:
            # search on the right
            start = mid+1
        else:
            end = mid-1
    return -1 #not found

class CodeTest(unittest.TestCase):
    def setup(self):
        pass

    def testEmptyArray(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([], 2), -1)

    def testLeftExclusionBoundary(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([0, 1, 2,2,4,5,5,5,8], -1), -1) 
    
    def testRightExclusionBoundary(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([0, 1, 2,2,4,5,5,5,8], 10), -1) 

    def testRightBoundaryWithoutDuplicates(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([0, 1, 2,2,4,5,5,5,8], 8), 8)

    def testLeftBoundaryWithoutDuplicates(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([0, 1, 2,2,4,5,5,5,8], 0), 0)

    def testLeftBoundaryWithDuplicates(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([0, 0, 1, 2,2,4,5,5,5,8], 0), 0) 

    def testRightBoundaryWithDuplicates(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([0, 1, 2,2,4,5,5,5,8, 8], 8), 8) 

    def testNonExistantMiddleElement(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([0, 1, 2,2,4,5,5,5,8], 3), -1) 

    def testExistantNonDuplicateMiddleElement(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([0, 1, 2,2,4,5,5,5,8], 4), 4) 

    def testExistantDuplicateMiddleElement(self):
        self.assertEqual(findFirstIndexInSortedArrayWithDuplicates([0, 1, 2,2,4,5,5,5,8], 5), 5) 

unittest.main()
