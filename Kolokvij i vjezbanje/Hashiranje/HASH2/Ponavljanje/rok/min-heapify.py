from binarytree import Node


def min_heapify(arr, i):
    n = len(arr)
    najmanji = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left] < arr[i]:
        najmanji = left
    if right < n and arr[right] < arr[najmanji]:
        najmanji = right

    if i != najmanji:
        arr[i], arr[najmanji] = arr[najmanji], arr[i]
        min_heapify(arr, najmanji)


def convert_to_min_heap(arr):
    n = len(arr)
    i = n//2
    while i >= 0:
        min_heapify(arr, i)
        i -= 1


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


arr = [32, 2, 19, 12, 4, 2, 5, 11, 7]

print("Before:", arr)
convert_to_min_heap(arr)
print("After :", arr)


root = create(arr)
print(root)
