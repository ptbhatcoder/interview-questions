import unittest


'''
https://www.ideserve.co.in/learn/all-palindromic-partitions
Non print version
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


def printPalin(inp, start, end, mat, ):
    if not len(inp):
        return ['']
    if end == start:
        return [inp[end]]
    ret = []
    for i in range(end, start-1, -1):
        if mat[i][end]:
            suffix = inp[i:end+1]
            prefices = printPalin(inp, start, i-1, mat)
            for prefix in prefices:
                ret.append(prefix+'-'+suffix)
    return ret


def findPalindromicPartitionsOfInputStringNonPrint(inp):
    return printPalin(inp, 0, len(inp)-1, palindromicSubstringMatrix(inp))
  


class CodeTest(unittest.TestCase):
  
    def assert_stdout(self, inp, expected_output):
        retvals = findPalindromicPartitionsOfInputStringNonPrint(inp)
        self.assertListEqual(sorted(retvals), sorted(expected_output))
            
    def testEmptyString(self):
        self.assert_stdout('', [''])

    def testSingleCharString(self):
        self.assert_stdout('a', ['a'])

    def testForStringWithNoMultiCharPalindrome(self):
        self.assert_stdout('abcdefgh', ['a-b-c-d-e-f-g-h'])

    def testForIDeserve(self):
        self.assert_stdout('IDeserve', ['I-D-e-s-e-r-v-e','I-D-ese-r-v-e'])

    def testForBanana(self):
        self.assert_stdout('banana', ['b-a-n-a-n-a','b-a-n-ana','b-a-nan-a','b-ana-n-a','b-anana'])

unittest.main()
