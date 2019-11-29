from binaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def iterativePostOrderDoubleStack(root):
    s1 = [root]
    s2 = []
    while len(s1):
        cur = s1.pop(-1)
        if cur.data != None:
            s2.append(cur.data)
        if cur.left:
            s1.append(cur.left)
        if cur.right:
            s1.append(cur.right)
    return s2[::-1]


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(
            iterativePostOrderDoubleStack(BinaryTreeNode(None)), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(
            iterativePostOrderDoubleStack(root), [5, 4, 3, 2, 1])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(
            iterativePostOrderDoubleStack(root), [5, 4, 3, 2, 1])

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
        self.assertListEqual(iterativePostOrderDoubleStack(
            root), [8, 4, 5, 2, 9, 6, 7, 3, 1])


main()
