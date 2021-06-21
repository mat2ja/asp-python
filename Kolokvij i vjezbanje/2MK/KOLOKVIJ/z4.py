

def ukloni(gomila):
    gomila = gomila[1:]

    flat_list = flatten(gomila)

    # print(flat_list)
    min_heap = convert_to_min_heap(flat_list, len(flat_list))

    print("Min heap:", min_heap)
    # to_nested_heap(min_heap, len(min_heap))


def to_nested_heap(arr, n, nested=[]):
    nested.append(arr[0])
    for i in range(1, n):
        inside = []
        nested.append(inside)
        if 2*i+1 < n:
            inside.append(arr[2*i-1])
        else:
            nested.append(None)
        if 2*i+2 < n:
            inside.append(arr[2*i-2])
        else:
            nested.append(None)
    print(nested)


def convert_to_min_heap(arr, n):
    i = n//2
    while i >= 0:
        min_heapify(arr, i)
        i -= 1

    return arr


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


def flatten(root):
    flat = []
    for elem in root:
        if isinstance(elem, list):
            flat += flatten(elem)
        else:
            flat.append(elem)
    return flat


ukloni([4, [5, [15, 16, 25], [9, 14, 12]], [6, [7, 11, 13], 20]])
[5, [9, [15, 16, 25], [12, 14, 13]], [6, [7, 11, None], 20]]  # rezultat
