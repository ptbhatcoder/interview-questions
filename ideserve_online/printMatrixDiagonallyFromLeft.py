from unittest import TestCase, main

'''
https://www.ideserve.co.in/learn/print-matrix-diagonally

Given a matrix of mxn dimensions, print the elements of the matrix in diagonal order, starting from the top left
'''


def printMatrixDiagonallyFromLeft(mat):
    res = []
    i = -1
    rows = len(mat)
    if rows:
        cols = len(mat[0])
    else:
        cols = 0
    for row in range(rows):
        r = row
        c = 0
        i += 1
        res.append([])
        while r >= 0 and c < cols:
            res[i].append(mat[r][c])
            r -= 1
            c += 1
    for col in range(1, cols):
        r = rows - 1
        c = col
        i += 1
        res.append([])
        while r >= 0 and c < cols:
            res[i].append(mat[r][c])
            r -= 1
            c += 1

    return res


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertEqual(printMatrixDiagonallyFromLeft([]), [])

    def testSquareMatrix(self):
        mat = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
        expected = [[1],
                    [4, 2],
                    [7, 5, 3],
                    [8, 6],
                    [9]]
        self.assertEqual(printMatrixDiagonallyFromLeft(mat), expected)

    def testTowerMatrix(self):
        mat = [[1, 2],
               [4, 5],
               [7, 8]]
        expected = [[1],
                    [4, 2],
                    [7, 5],
                    [8]]
        self.assertEqual(printMatrixDiagonallyFromLeft(mat), expected)

    def testSlabMatrix(self):
        mat = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10]]
        expected = [[1],
                    [6, 2],
                    [7, 3],
                    [8, 4],
                    [9, 5],
                    [10]]
        self.assertEqual(printMatrixDiagonallyFromLeft(mat), expected)


main()
