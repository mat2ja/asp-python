
from binarytree import Node


def BS_to_BSP(root):
    if not root:
        return
    inorder_arr = []
    inorder_obilazak(root, inorder_arr)
    inorder_arr.sort()

    root = arr_to_bsp(inorder_arr)

    return root


def arr_to_bsp(arr):
    if not arr:
        return None

    print(arr)
    n = len(arr)

    mid = n//2
    root = Node(arr[mid])
    root.left = arr_to_bsp(arr[:mid])
    root.right = arr_to_bsp(arr[mid+1:])

    return root


# left -> root -> right
def inorder_obilazak(node, arr):
    if node:
        inorder_obilazak(node.left, arr)
        arr.append(node.value)
        inorder_obilazak(node.right, arr)


root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(8)
root.right.right = Node(5)

print(root)
root = BS_to_BSP(root)
print(root)
