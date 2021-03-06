
from unittest import main, TestCase

'''
https://www.ideserve.co.in/learn/number-of-clusters-of-1s

Given a 2D matrix of 0s and 1s, find total number of clusters formed by elements with value 1.  For example, in the below shown 2D matrix there are total three such clusters.

This problem is also known as 'Number of Islands' problem.
'''


def visit(visited, i, j, mi, mj, mat):
    if i < mi and j < mj:
        visited[i][j] = True
    nr = [-1, -1, -1, 0, 0, 1, 1, 1]
    nc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for ro in nr:
        for co in nc:
            r = i + ro
            c = j + co
            if r >= 0 and r < mi and c >= 0 and c < mj and not visited[r][c] and mat[r][c]:
                visited = visit(visited, r, c, mi, mj, mat)
    return visited


def findNumberOfIslands(mat):
    visited = [[False for k in mat[0]] for p in mat]
    count = 0
    rows = len(mat)
    cols = 0
    if rows:
        cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] and not visited[i][j]:
                count += 1
                visited = visit(visited, i, j, rows, cols, mat)
    return count


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertEqual(findNumberOfIslands([]), 0)

    def testNoIslands(self):
        mat = [
            [0, 0, 0, 0, 0, 0] * 8
        ]
        self.assertEqual(findNumberOfIslands(mat), 0)

    def testSquare(self):
        mat = [[1, 1, 0, 0, 0],
               [0, 1, 0, 0, 1],
               [1, 0, 0, 1, 1],
               [0, 0, 0, 0, 0],
               [1, 0, 1, 0, 1]]
        self.assertEqual(findNumberOfIslands(mat), 5)


main()
