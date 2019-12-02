from unittest import TestCase, main


def printMatrixDiagonallyFromRight(mat):
    res = []
    i = -1
    rows = len(mat)
    if rows:
        cols = len(mat[0])
    else:
        cols = 0
    for row in range(rows):
        r = row
        c = cols-1
        i += 1
        res.append([])
        while r >= 0 and c >= 0:
            res[i].append(mat[r][c])
            r -= 1
            c -= 1
    for col in range(cols-2, -1, -1):
        r = rows - 1
        c = col
        i += 1
        res.append([])
        while r >= 0 and c >= 0:
            res[i].append(mat[r][c])
            r -= 1
            c -= 1

    return res


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertEqual(printMatrixDiagonallyFromRight([]), [])

    def testSquareMatrix(self):
        mat = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
        expected = [[3],
                    [6, 2],
                    [9, 5, 1],
                    [8, 4],
                    [7]]
        self.assertEqual(printMatrixDiagonallyFromRight(mat), expected)

    def testTowerMatrix(self):
        mat = [[1, 2],
               [4, 5],
               [7, 8]]
        expected = [[2],
                    [5, 1],
                    [8, 4],
                    [7]]
        self.assertEqual(printMatrixDiagonallyFromRight(mat), expected)

    def testSlabMatrix(self):
        mat = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10]]
        expected = [[5],
                    [10, 4],
                    [9, 3],
                    [8, 2],
                    [7, 1],
                    [6]]
        self.assertEqual(printMatrixDiagonallyFromRight(mat), expected)


main()
