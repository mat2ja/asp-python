from binarytree import Node


def sortedPolje2BST(arr):
    if not arr:
        return

    n = len(arr)
    mid = n//2

    root = Node(arr[mid])
    root.left = sortedPolje2BST(arr[:mid])
    root.right = sortedPolje2BST(arr[mid+1:])

    return root


def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedPolje2BST(arr)
print(root)
print("Inorder obilazak BST ", end=" > ")
preorder(root)
print("\n")
print("Inorder obilazak BST ", end=" > ")
inorder(root)
