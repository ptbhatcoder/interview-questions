from binaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def reversePreorder(root, t):
    if root:
        if root.data != None:
            t.append(root.data)
        reversePreorder(root.right, t)
        reversePreorder(root.left, t)
    return t


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(reversePreorder(BinaryTreeNode(None), []), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(reversePreorder(root, []), [1, 2, 3, 4, 5])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(reversePreorder(root, []), [1, 2, 3, 4, 5])

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
        self.assertListEqual(reversePreorder(root, []),
                             [1, 3, 7, 6, 9, 2, 5, 4, 8])


main()
