from BinaryTree.BinaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def iterativeReverseInorder(root):
    t = []
    cur = root
    s = []
    while len(s) or cur:
        while cur:
            s.append(cur)
            cur = cur.right
        cur = s.pop(-1)
        if cur.data != None:
            t.append(cur.data)
        cur = cur.left
    return t


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(iterativeReverseInorder(BinaryTreeNode(None)), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(iterativeReverseInorder(root), [1, 2, 3, 4, 5])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(iterativeReverseInorder(root), [5, 4, 3, 2, 1])

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
        self.assertListEqual(iterativeReverseInorder(root),
                             [7, 3, 9, 6, 1, 5, 2, 4, 8])


main()
