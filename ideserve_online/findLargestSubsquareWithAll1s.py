from unittest import main, TestCase


def findLargestSubsquareWithAll1s(mat):
    mxi, mxj, mx = -1, -1, 0
    count = [[val for val in row] for row in mat]
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if mat[i][j]:
                count[i][j] = min(count[i][j-1], count[i-1]
                                  [j-1], count[i-1][j]) + 1
                if mx < count[i][j]:
                    mx = count[i][j]
                    mxi = i - mx + 1
                    mxj = j - mx + 1
    return mxi, mxj, mx


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertEqual(findLargestSubsquareWithAll1s([]), (-1, -1, 0))

    def testAllZeroes(self):
        mat = [[0 for i in range(4)] for k in range(4)]
        self.assertEqual(findLargestSubsquareWithAll1s(mat), (-1, -1, 0))

    def testSparseMatrix(self):
        mat = [[0 for i in range(5)] for k in range(5)]
        for i in range(5):
            for j in range(5):
                if not (i + j) & 1:
                    mat[i][j] = 1
        self.assertEqual(findLargestSubsquareWithAll1s(mat), (1, 1, 1))

    def testActualValidMatrix(self):
        mat = [[0, 1, 1, 0, 1],
               [1, 1, 0, 1, 0],
               [0, 1, 1, 1, 0],
               [1, 1, 1, 1, 0],
               [1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0]]

        self.assertEqual(findLargestSubsquareWithAll1s(mat), (2, 1, 3))


main()
