# Convert a BST to a Binary Tree such that sum of all greater keys is added to every key

from binarytree import Node


def add_smallerf_util(root, suma_ptr):

    if root is None:
        return

    add_smallerf_util(root.left, suma_ptr)

    suma_ptr[0] = suma_ptr[0] + root.value
    root.value = suma_ptr[0]

    add_smallerf_util(root.right, suma_ptr)


def add_smaller(root):
    suma = [0]  # ARR REFERENCA OSTAJE!!!!!!
    add_smallerf_util(root, suma)


def addSmaller(root,suma=0):
    if root:
        suma = addSmaller(root.left, suma)
        suma += root.value
        root.value = suma
        suma = addSmaller(root.right, suma)
    return suma




root = Node(5)
root.left = Node(2)
root.right = Node(13)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(9)
root.right.right = Node(18)
'''
    __5__
   /     \
  2       13
 / \     /  \
1   4   9    18
'''

print(root)

addSmaller(root)
print(root)
'''
     ____45___
    /         \
  _51         _31
 /   \       /   \
52    49    40    18
'''
