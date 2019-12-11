import sys
from os import path
curDirname = path.dirname(__file__)
while path.basename(path.normpath(curDirname)) != 'ideserve_online':
    curDirname = path.dirname(curDirname)
sys.path.insert(0, curDirname)

from BinaryTree.BinaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def morrisPreorder(root):
    cur = root
    t = []
    while cur:
        if not cur.left:
            if cur.data:
                t.append(cur.data)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right

            if pre.right:
                pre.right = None
                cur = cur.right
            else:
                if cur.data:
                    t.append(cur.data)
                pre.right = cur
                cur = cur.left
    return t


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(morrisPreorder(BinaryTreeNode(None)), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(morrisPreorder(root), [1, 2, 3, 4, 5])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(morrisPreorder(root), [1, 2, 3, 4, 5])

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
        self.assertListEqual(morrisPreorder(root), [1, 2, 4, 8, 5, 3, 6, 9, 7])


main()
