from binaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def inorder(root, arr):
    if not root:
        return arr
    inorder(root.left, arr)
    if root.data != None:
        arr.append(root.data)
    inorder(root.right, arr)
    return arr


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(inorder(BinaryTreeNode(None), []), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(inorder(root, []), [5, 4, 3, 2, 1])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(inorder(root, []), [1, 2, 3, 4, 5])

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
        self.assertListEqual(inorder(root, []), [8, 4, 2, 5, 1, 6, 9, 3, 7])


main()
