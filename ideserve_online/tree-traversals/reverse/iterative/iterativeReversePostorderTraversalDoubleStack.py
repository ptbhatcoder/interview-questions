import sys
from os import path
curDirname = path.dirname(__file__)
while path.basename(path.normpath(curDirname)) != 'ideserve_online':
    curDirname = path.dirname(curDirname)
sys.path.insert(0, curDirname)

from BinaryTree.BinaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def iterativeReversePostorderDoubleStack(root):
    s1 = [root]
    s2 = []
    while len(s1):
        cur = s1.pop(-1)
        if cur.data != None:
            s2.append(cur.data)
        if cur.right:
            s1.append(cur.right)
        if cur.left:
            s1.append(cur.left)
    return s2[::-1]


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(
            iterativeReversePostorderDoubleStack(BinaryTreeNode(None)), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(
            iterativeReversePostorderDoubleStack(root), [5, 4, 3, 2, 1])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(
            iterativeReversePostorderDoubleStack(root), [5, 4, 3, 2, 1])

    def testNormalTree(self):
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(7)
        root.left.left.left = BinaryTreeNode(8)
        root.right.left.right = BinaryTreeNode(9)
        self.assertListEqual(iterativeReversePostorderDoubleStack(
            root), [7, 9, 6, 3, 5, 8, 4, 2, 1])


main()
