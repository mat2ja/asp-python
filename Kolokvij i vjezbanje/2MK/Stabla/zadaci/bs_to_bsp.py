from binarytree import Node


def arr_to_bsp(arr, root):
    if root:
        arr_to_bsp(arr, root.left)

        root.value = arr[0]
        arr.pop(0)

        arr_to_bsp(arr, root.right)


def binarytree_to_bsp(root):
    if not root:
        return
    arr = []
    store_inorder(root, arr)

    arr.sort()

    arr_to_bsp(arr, root)


def store_inorder(root, inorder):
    if root:
        store_inorder(root.left, inorder)
        inorder.append(root.value)
        store_inorder(root.right, inorder)


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.value, end=" ")
        print_inorder(root.right)


def get_tree_height(root):
    if root is None:
        return -1

    return (max(get_tree_height(root.left), get_tree_height(root.right)) + 1)


# def arr2bsp(arr):
#     if not arr:
#         return None

#     n = len(arr)

#     mid = n//2

#     root = Node(arr[mid])
#     root.left = arr2bsp(arr[:mid])
#     root.right = arr2bsp(arr[mid+1:])

#     return root


# def binarytree_to_bsp(root):
#     if not root:
#         return

#     arr = []
#     store_inorder(root, arr)

#     arr.sort()

#     root = arr_to_bsp(arr, root)


root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(8)
root.right.right = Node(5)

print(root)
binarytree_to_bsp(root)
print(root)
print_inorder(root)
