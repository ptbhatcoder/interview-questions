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

    def search(self, key, root=treeRoot):
        if not root:
            return None

        if root.data == key:
            return root

        if root.data < key:
            return self.search(key, root.right)

        return self.search(key, root.left)

    def findMin(self, root=treeRoot):
        while root and root.left:
            root = root.left
        return root

    def findMax(self, root=treeRoot):
        while root and root.right:
            root = root.right
        return root

    def insert(self, key, root=treeRoot):
        if not root:
            return BinaryTreeNode(key)

        if key < root.data:
            root.left = self.insert(key, root.left)
        else:
            root.right = self.insert(key, root.right)
        return root

    def delete(self, key, root=treeRoot):
        if not root:
            return root

        if key < root.data:
            root.left = self.delete(key, root.left)
        elif key > root.data:
            root.right = self.delete(key, root.right)
        else:
            if root.left and root.right:
                root.data = self.findMin(root.right)
                root.right = self.delete(root.data, root.right)
            elif root.left:
                left = root.left
                del root
                return left
            else:
                right = root.right
                del root
                return right

        return root
