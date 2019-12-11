from BinaryTree.BinaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def morrisPostorder(root):
    t = []
    dummy = BinaryTreeNode(None)
    dummy.left = root
    cur = dummy
    while cur:
        if not cur.left:
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right

            if pre.right:
                pre = cur.left
                count = 1
                while pre.right and pre.right != cur:
                    if pre.data:
                        t.append(pre.data)
                        count += 1
                    pre = pre.right
                if pre.data:
                    t.append(pre.data)
                t[len(t) - count:] = t[len(t)-count:][::-1]
                pre.right = None
                cur = cur.right
            else:
                pre.right = cur
                cur = cur.left
    dummy.left = None
    del dummy
    return t


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(morrisPostorder(BinaryTreeNode(None)), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(morrisPostorder(root), [5, 4, 3, 2, 1])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(morrisPostorder(root), [5, 4, 3, 2, 1])

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
        self.assertListEqual(morrisPostorder(
            root), [8, 4, 5, 2, 9, 6, 7, 3, 1])


main()
