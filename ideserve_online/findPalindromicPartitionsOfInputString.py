import unittest
from io import BytesIO as StringIO
from contextlib import contextmanager
import sys

'''
https://www.ideserve.co.in/learn/all-palindromic-partitions
Given a string, print all palindromic partitions of the given string.
Palindromic partitioning of a string is dividing the string into parts such that each part is a palindrome.

If abcb is a string, then
a-b-c-b and a-bcb will be palindormic partitions of the string.

a-b-cb, ab-cb, ab-c-b etc are partitions but not palindromic partitions of the string abcb.
b-c-b is palindromic but not a partition of the string abcb.

Example:

Input:
IDeserve
Output:
I-D-e-s-e-r-v-e
I-D-ese-r-v-e

Input:
banana
Output:
b-a-n-a-n-a
b-a-n-ana
b-a-nan-a
b-ana-n-a
b-anana
'''

def palindromicSubstringMatrix(inp):
    if not len(inp):
        return []
    mat = [[True]*len(inp) for a in inp]
    for j in range(len(inp)):
        for i in range(0, j):
            mat[i][j] = str(inp[i]).lower() == str(inp[j]).lower() and mat[i+1][j-1]
    return mat


def printPalin(inp, start, end, mat, prefix = ''):
    if not len(inp):
        print('')
        return
    if start == len(inp):
        print(prefix)
        return
    for i in range(start, end+1):
        if mat[start][i]:
            newPrefix = prefix
            if len(prefix):
                newPrefix = newPrefix + '-'
            printPalin(inp, i+1, end, mat, newPrefix+inp[start:i+1])


def findPalindromicPartitionsOfInputString(inp):
    printPalin(inp, 0, len(inp)-1, palindromicSubstringMatrix(inp))
  

class CodeTest(unittest.TestCase):
    # https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
    @contextmanager
    def assert_stdout(self, inp, expected_output):
        intercept = StringIO()
        old_target, sys.stdout = sys.stdout, intercept # replace sys.stdout
        try:
            findPalindromicPartitionsOfInputString(inp)
            self.assertEqual(expected_output.strip(), intercept.getvalue().strip())
        finally:
            sys.stdout = old_target # restore to the previous value
            
       

    def testEmptyString(self):
        self.assert_stdout('', '')

    def testSingleCharString(self):
        self.assert_stdout('a', 'a')

    def testForStringWithNoMultiCharPalindrome(self):
        self.assert_stdout('abcdefgh', 'a-b-c-d-e-f-g-h')

    def testForIDeserve(self):
        self.assert_stdout('IDeserve', 'I-D-e-s-e-r-v-e\nI-D-ese-r-v-e')

    def testForBanana(self):
        self.assert_stdout('banana', 'b-a-n-a-n-a\nb-a-n-ana\nb-a-nan-a\nb-ana-n-a\nb-anana')

unittest.main()