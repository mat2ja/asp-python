from binarytree import Node


def max_heapify(arr, i, n):
    left = i*2 + 1
    right = i*2 + 2
    najveci = i

    if left < n and arr[left] > arr[i]:
        najveci = left

    if right < n and arr[right] > arr[najveci]:
        najveci = right

    if najveci != i:
        arr[i], arr[najveci] = arr[najveci], arr[i]
        max_heapify(arr, najveci, n)


# def swap(arr,a,b):
#     arr[a],arr[b] = arr[b],arr[a]

def convert_to_max_heap(arr):
    n = len(arr)

    i = n//2
    while i >= 0:
        max_heapify(arr, i, n)
        i -= 1

    # for i in range(n//2, -1, -1):
    #     max_heapify(arr, i, n)

# Function to insert nodes in level order


def create(arr, root=None, i=0, n=None):
    if n is None:
        n = len(arr)

    if i < n:
        root = Node(arr[i])

        # insert left child
        root.left = create(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = create(arr, root.right, 2 * i + 2, n)
    return root


arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
convert_to_max_heap(arr)
print(arr)


root = create(arr)
print(root)
