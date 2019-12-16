from sys import path as syspath
from os import path as ospath
curpath = ospath.dirname(__file__)
while ospath.basename(ospath.normpath(curpath)) != 'ideserve_online':
    curpath = ospath.dirname(curpath)
syspath.insert(0, curpath)

from unittest import TestCase, main


class AVLTreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


class AVLTree():
    treeRoot = None

    def __init__(self, data):
        self.treeRoot = AVLTreeNode(data)
        self.treeRoot.height = 0

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

    def __getHeight__(self, root):
        if root:
            root.height = max(self.__getHeight__(root.left),
                              self.__getHeight__(root.right)) + 1
            return root.height
        else:
            return 0

    def __getBalance__(self, root):
        if not root:
            return 0
        return self.__getHeight__(root.left) - self.__getHeight__(root.right)

    def __rotateRight__(self, root):
        if not root:
            return root
        y = root.left
        if y:
            t2 = y.right
            root.left = t2
            y.right = root
            return y
        return root

    def __rotateLeft__(self, root):
        if not root:
            return root
        y = root.right
        if y:
            t2 = y.left
            root.right = t2
            y.left = root
            return y
        return root

    def insert(self, key, root):
        if not root:
            root = AVLTreeNode(key)
            root.height = 0
            return root

        if key < root.data:
            root.left = self.insert(key, root.left)
        else:
            root.right = self.insert(key, root.right)

        # time to balance if there is an imbalance
        balance = self.__getBalance__(root)
        if balance > 1 and key < root.left.data:
            # left-left case
            root = self.__rotateRight__(root)
        elif balance > 1 and key > root.left.data:
            # left-right case
            root.left = self.__rotateLeft__(root.left)
            root = self.__rotateRight__(root)
        elif balance < -1 and key > root.right.data:
            # right-right case
            root = self.__rotateLeft__(root)
        elif balance < -1 and key < root.right.data:
            # right-left case
            root.right = self.__rotateRight__(root.right)
            root = self.__rotateLeft__(root)

        root.height = self.__getHeight__(root)
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
                swapper = self.findMax(root.left)
                root.data = swapper.data
                root.left = self.delete(swapper.data, root.left)
            elif root.left:
                left = root.left
                del root
                root = left
            else:
                right = root.right
                del root
                root = right
        # balancing the nodes
        balance = self.__getBalance__(root)
        if balance < -1 and root.right.right and root.right.left and root.right.right.height > root.right.left.height:
            # right-right case
            root = self.__rotateLeft__(root)
        elif balance < -1 and root.right.right and root.right.left and root.right.right.height < root.right.left.height:
            # right-left case
            root.right = self.__rotateRight__(root.right)
            root = self.__rotateLeft__(root)
        elif balance > 1 and root.left.right and root.left.left and root.left.left.height > root.left.right.height:
            # left-left case
            root = self.__rotateRight__(root)
        elif balance > 1 and root.left.left and root.left.right and root.left.left.height < root.left.right.height:
            # left-right case
            root.left = self.__rotateLeft__(root.left)
            root = self.__rotateRight__(root)

        root.height = self.__getHeight__(root)
        return root


class CodeTest(TestCase):
    def testNoImbalanceInsert(self):
        binarySearchTree = AVLTree(1)
        root = binarySearchTree.getRoot()
        for i in range(2, 9):
            root = binarySearchTree.insert(i, root)

        self.assertEqual(root.data, 4)
        self.assertEqual(root.left.data, 2)
        self.assertEqual(root.right.data, 6)
        self.assertEqual(root.left.left.data, 1)
        self.assertEqual(root.left.right.data, 3)
        self.assertEqual(root.right.left.data, 5)
        self.assertEqual(root.right.right.data, 7)
        self.assertEqual(root.right.right.right.data, 8)


main()
