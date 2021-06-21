# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


from binarytree import Node


def arr_to_bsp(arr):
    if not arr:
        return None

    n = len(arr)

    mid = n//2

    root = Node(arr[mid])

    root.left = arr_to_bsp(arr[:mid])
    root.right = arr_to_bsp(arr[mid+1:])

    return root


# root -> left -> right
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)


# left -> root -> right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")


arr = [1, 2, 3, 4, 5, 6, 7]
root = arr_to_bsp(arr)
print(root)  # metoda importa
preorder(root)  # 4 2 1 3 6 5 7
print()
inorder(root)  # 1 2 3 4 5 6 7
print()
postorder(root)  # 1 3 2 5 7 6 4

'''
    __4__
   /     \
  2       6
 / \     / \
1   3   5   7
'''
