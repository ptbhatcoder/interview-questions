from sys import path as syspath
from os import path as ospath
curpath = ospath.dirname(__file__)
while ospath.basename(ospath.normpath(curpath)) != 'ideserve_online':
    curpath = ospath.dirname(curpath)
syspath.insert(0, curpath)

from BinaryTree.BinaryTreeNode import BinaryTreeNode
from BinarySearchTree.BinarySearchTree import BinarySearchTree


class AVLTree(BinarySearchTree):
    treeRoot = None

    def __init__(self, data):
        super.__init__(data)
        self.treeRoot.height = 0

    def getRoot(self):
        return self.treeRoot

    def search(self, key, root):
        return super.search(key, root)

    def findMin(self, root):
        return super.findMin(root)

    def findMax(self, root):
        return super.findMax(root)

    def __getHeight__(self, root):
        if not root:
            return 0
        root.height = max(self.__getHeight__(root.left),
                          self.__getHeight__(root.right)) + 1
        return root.height

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
            root = BinaryTreeNode(key)
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
