from binaryTreeNode import BinaryTreeNode
from unittest import main, TestCase


def morrisReversePostorder(root):
    t = []
    dummy = BinaryTreeNode(None)
    dummy.right = root
    cur = dummy
    while cur:
        if not cur.right:
            cur = cur.left
        else:
            pre = cur.right
            while pre.left and pre.left != cur:
                pre = pre.left

            if pre.left:
                pre = cur.right
                count = 1
                while pre.left and pre.left != cur:
                    if pre.data:
                        t.append(pre.data)
                        count += 1
                    pre = pre.left
                if pre.data:
                    t.append(pre.data)
                t[len(t) - count:] = t[len(t)-count:][::-1]
                pre.left = None
                cur = cur.left
            else:
                pre.left = cur
                cur = cur.right
    dummy.right = None
    del dummy
    return t


class CodeTest(TestCase):
    def testEmpty(self):
        self.assertListEqual(morrisReversePostorder(BinaryTreeNode(None)), [])

    def testLeftSkewed(self):
        root = BinaryTreeNode(1, BinaryTreeNode(
            2, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5)))))
        self.assertListEqual(morrisReversePostorder(root), [5, 4, 3, 2, 1])

    def testRightSkewed(self):
        root = BinaryTreeNode(1, right=BinaryTreeNode(
            2, right=BinaryTreeNode(3, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))))
        self.assertListEqual(morrisReversePostorder(root), [5, 4, 3, 2, 1])

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
        self.assertListEqual(morrisReversePostorder(
            root), [7, 9, 6, 3, 5, 8, 4, 2, 1])


main()
