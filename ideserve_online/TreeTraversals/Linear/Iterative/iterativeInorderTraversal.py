import sys
from os import path
curDirname = path.dirname(__file__)
while path.basename(path.normpath(curDirname)) != 'ideserve_online':
    curDirname = path.dirname(curDirname)
sys.path.insert(0, curDirname)

from BinaryTree.BinaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def iterativeInorder(root):
    t = []
    s = []
    cur = root
    while cur or len(s):
        while cur:
            s.append(cur)
            cur = cur.left

        cur = s.pop(-1)
        if cur.data != None:
            t.append(cur.data)
        cur = cur.right

    return t


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(iterativeInorder(BinaryTreeNode(None)), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(iterativeInorder(root), [5, 4, 3, 2, 1])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(iterativeInorder(root), [1, 2, 3, 4, 5])

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
        self.assertListEqual(iterativeInorder(
            root), [8, 4, 2, 5, 1, 6, 9, 3, 7])


main()
