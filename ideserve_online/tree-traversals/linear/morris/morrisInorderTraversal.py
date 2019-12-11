from BinaryTree.BinaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def morrisInorder(root):
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
                if cur.data:
                    t.append(cur.data)
                pre.right = None
                cur = cur.right
            else:
                pre.right = cur
                cur = cur.left
    return t


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(morrisInorder(BinaryTreeNode(None)), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(morrisInorder(root), [5, 4, 3, 2, 1])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(morrisInorder(root), [1, 2, 3, 4, 5])

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
        self.assertListEqual(morrisInorder(root), [8, 4, 2, 5, 1, 6, 9, 3, 7])


main()
