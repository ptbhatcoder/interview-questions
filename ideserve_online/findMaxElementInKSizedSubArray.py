from os import path as ospath
from sys import path as syspath
curDir = ospath.dirname(__file__)
while ospath.basename(ospath.normpath(curDir)) != 'ideserve_online':
    curDir = ospath.dirname(curDir)
syspath.insert(0, curDir)

from AVLTree.AVLTree import AVLTree


def findMaxElementInKSizedSubArrayBruteForce(arr, k):
    mins = []
    if len(arr) <= k:
        return [min(arr)]
    for i in range(len(arr) - k):
        mins.append(min(arr[i:i + k]))
    return mins


def findMaxElementInKSizedSubArrayAvlTree(arr, k):
    mins = []
    if not (arr and len(arr)):
        return mins
    if len(arr) <= k:
        return [min(arr)]
    tree = AVLTree(arr[0])
    root = tree.getRoot()
    for i in range(1, k):
        root = tree.insert(arr[i], root)
    mins.append(tree.findMax(root).data)
    for i in range(k, len(arr)):
        root = tree.delete(arr[i - k], root)
        root = tree.insert(arr[i], root)
        mins.append(tree.findMax(root).data)
    return mins
