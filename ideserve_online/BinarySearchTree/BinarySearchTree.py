from os import path as ospath
from sys import path as syspath
curPath = ospath.dirname(__file__)
while ospath.basename(ospath.normpath(curPath)) != 'ideserve_online':
    curPath = ospath.dirname(curPath)
syspath.insert(0, curPath)

from BinaryTree.BinaryTreeNode import BinaryTreeNode
from unittest import TestCase, main


class BinarySearchTree():
    treeRoot = None

    def __init__(self, data):
        self.treeRoot = BinaryTreeNode(data)

    def getRoot(self):
        return self.treeRoot

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print('data:' + str(root.data))
            self.inorder(root.right)

    def search(self, key, root=treeRoot):
        if not root:
            return None

        if root.data == key:
            return root

        if root.data < key:
            return self.search(key, root.right)

        return self.search(key, root.left)

    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root

    def findMax(self, root):
        while root and root.right:
            root = root.right
        return root

    def insert(self, key, root):
        if not root:
            return BinaryTreeNode(key)

        if key < root.data:
            root.left = self.insert(key, root.left)
        elif key > root.data:
            root.right = self.insert(key, root.right)
        return root

    def delete(self, key, root):
        if not root:
            return root

        if key < root.data:
            root.left = self.delete(key, root.left)
        elif key > root.data:
            root.right = self.delete(key, root.right)
        else:
            if root.left and root.right:
                swapper = self.findMin(root.right)
                root.data = swapper.data
                root.right = self.delete(swapper.data, root.right)
                return root
            elif root.left:
                left = root.left
                del root
                return left
            else:
                right = root.right
                del root
                return right

        return root


class CodeTest(TestCase):
    def testSearch(self):
        binarySearchTree = BinarySearchTree(5)
        root = binarySearchTree.getRoot()
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(7)
        root.left.left = BinaryTreeNode(2)
        root.left.right = BinaryTreeNode(4)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(8)
        root.left.left.left = BinaryTreeNode(1)
        # binarySearchTree.inorder(root)
        self.assertEqual(binarySearchTree.search(4, root), root.left.right)
        self.assertIsNone(binarySearchTree.search(10, root))

    def testFindMinAndFindMax(self):
        binarySearchTree = BinarySearchTree(5)
        root = binarySearchTree.getRoot()
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(7)
        root.left.left = BinaryTreeNode(2)
        root.left.right = BinaryTreeNode(4)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(8)
        root.left.left.left = BinaryTreeNode(1)
        # binarySearchTree.inorder(root)
        self.assertEqual(binarySearchTree.findMin(root).data, 1)
        self.assertEqual(binarySearchTree.findMax(root).data, 8)

    def testFindMinAndFindMaxNotComplete(self):
        binarySearchTree = BinarySearchTree(5)
        root = binarySearchTree.getRoot()
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(7)
        root.left.left = BinaryTreeNode(2)
        root.left.right = BinaryTreeNode(4)
        root.right.left = BinaryTreeNode(6)
        # binarySearchTree.inorder(root)
        self.assertEqual(binarySearchTree.findMin(root).data, 2)
        self.assertEqual(binarySearchTree.findMax(root).data, 7)

    def testInsert(self):
        binarySearchTree = BinarySearchTree(5)
        root = binarySearchTree.getRoot()
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(7)
        root.left.left = BinaryTreeNode(2)
        root.left.right = BinaryTreeNode(4)
        root.right.left = BinaryTreeNode(6)
        # binarySearchTree.inorder(root)
        root = binarySearchTree.insert(8, root)
        self.assertEqual(root.right.right.data, 8)
        root = binarySearchTree.insert(1, root)
        self.assertEqual(1, root.left.left.left.data)
        root = binarySearchTree.insert(7, root)
        self.assertEqual(7, root.right.data)

    def testDelete(self):
        binarySearchTree = BinarySearchTree(5)
        root = binarySearchTree.getRoot()
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(7)
        root.left.left = BinaryTreeNode(2)
        root.left.right = BinaryTreeNode(4)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(8)
        root.left.left.left = BinaryTreeNode(1)
        # binarySearchTree.inorder(root)
        root = binarySearchTree.delete(1, root)
        self.assertIsNone(root.left.left.left)
        root = binarySearchTree.delete(4, root)
        self.assertIsNone(root.left.right)
        root = binarySearchTree.delete(3, root)
        self.assertEqual(2, root.left.data)
        root = binarySearchTree.delete(5, root)
        self.assertEqual(6, root.data)
        self.assertIsNone(root.right.left)

    def testImbalance(self):
        binarySearchTree = BinarySearchTree(1)
        root = binarySearchTree.getRoot()
        for i in range(2, 9):
            root = binarySearchTree.insert(i, root)
        k = [i for i in range(1, 9)]
        node = root
        for x in k:
            self.assertEqual(node.data, x)
            self.assertIsNone(node.left)
            node = node.right


main()
