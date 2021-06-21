from binarytree import build


def heap_sort(arr):
    n = len(arr)

    # pretvori u max heap, krecmeo s pola (prvi roditelji koji imaju djecu)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    # print("After building heap\n", build(arr))

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        # print("After replacing root and last\n", build(arr))
        heapify(arr, i, 0)
        # print("After removing largest and turning to heap\n", build(arr[0:i]))

    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[i]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        # zamjeni roditelja i vece dijete
        arr[i], arr[largest] = arr[largest], arr[i]
        # nizu granu pretvori u stablo (djecu od elementa nakon zamjene)
        # index najveceg je ostao isti ali na to mjesto smo stavili manjeg bivseg roditelja
        heapify(arr, n, largest)


# sorts in reverse in regular heap sort
def heapify_min(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[i]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_min(arr, n, smallest)


A = [3, 10, 6, 12, 1, 2, 9, 17]
B = A[:]
# B = [3,2,12,10,6,9,17]

tree1 = build(A)
# print(tree1)

print(heap_sort(A))
