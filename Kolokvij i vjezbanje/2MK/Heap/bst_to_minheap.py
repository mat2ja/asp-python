from binarytree import Node


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


def bst_to_minheap(root):
    sorted_arr = []
    store_inorder(root, sorted_arr)
    # print(sorted_arr)
    minify(root, sorted_arr)


# preorder
def minify(root, arr, i=-1):
    if root:
        i += 1
        root.value = arr[i]

        i = minify(root.left, arr, i)
        i = minify(root.right, arr, i)
    return i


def store_inorder(root, arr):
    if root:
        store_inorder(root.left, arr)
        arr.append(root.value)
        store_inorder(root.right, arr)


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)
print("BST:", root)

bst_to_minheap(root)

print("\nMin-Heap:", root)
