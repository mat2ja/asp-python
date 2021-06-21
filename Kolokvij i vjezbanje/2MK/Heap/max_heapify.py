from random import randint


def max_heapify(arr, i, n):
    najveci = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[i]:
        najveci = left

    if right < n and arr[right] > arr[najveci]:
        najveci = right

    if najveci != i:
        arr[najveci], arr[i] = arr[i], arr[najveci]
        max_heapify(arr, najveci, n)


def to_heap(arr):
    n = len(arr)
    i = n//2
    while i >= 0:
        max_heapify(arr, i, n)
        i -= 1


A = [8, 22, 19, 9, 5, 14, 2, 18, 24, 30]
print(A)
to_heap(A)
print(A)
