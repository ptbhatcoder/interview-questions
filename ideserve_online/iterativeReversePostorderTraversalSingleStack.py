from BinaryTree.BinaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def iterativeReversePostorderSingleStack(root):
    t = []
    cur = root
    s = []
    while len(s) or cur:
        while cur:
            if cur.left:
                s.append(cur.left)
            s.append(cur)
            cur = cur.right

        cur = s.pop(-1)
        if cur and len(s) and cur.left == s[-1]:
            temp, cur = cur, s.pop(-1)
            s.append(temp)
        else:
            if cur.data != None:
                t.append(cur.data)
            cur = None

    return t


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(
            iterativeReversePostorderSingleStack(BinaryTreeNode(None)), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(
            iterativeReversePostorderSingleStack(root), [5, 4, 3, 2, 1])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(
            iterativeReversePostorderSingleStack(root), [5, 4, 3, 2, 1])

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
        self.assertListEqual(iterativeReversePostorderSingleStack(
            root), [7, 9, 6, 3, 5, 8, 4, 2, 1])


main()
