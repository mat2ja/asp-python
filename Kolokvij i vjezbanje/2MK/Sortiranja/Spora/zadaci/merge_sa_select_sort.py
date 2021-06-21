'''
1 zadatak
Zadan je niz brojeva L = [20, 45, 45, 40, 12, 48, 67, 90, 0, 56, 12, 45, 67, 45, 34, 32, 20,20,20, 45, 45, 40, 12, 48, 67, 90, 0, 56, 12, 45, 67, 45, 34, 32, 20,20] čija duljina je n = 36.

Razbijte niz L na 3 pod niza L1, L2 i L3 duljine n1 = 7, n2 = 13 i n3=16.

Sortirajte sva tri niza korištenjem algoritma Selection sort (napišite funkciju za sortiranje). Napišite funkciju def merge_sort() koja spaja sva tri sortirana podniza L1, L2 i L3 u jedan sortirani niz. Ocijenite ukupnu složenost cijelog procesa u O-notaciji. Ocijenite složenost merge_sort algoritma u O-notaciji.
'''


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        najmanji = i
        for j in range(i+1, n):
            if arr[j] < arr[najmanji]:
                najmanji = j
        arr[i], arr[najmanji] = arr[najmanji], arr[i]

    return arr


def merge_sort(arr1, arr2=None, arr3=None):

    if arr2 and arr3:
        arr = arr1 + arr2 + arr3
    else:
        arr = arr1

    if not len(arr) > 1:
        return

    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # leftovers
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


L = [20, 45, 45, 40, 12, 48, 67, 90, 0, 56, 12, 45, 67, 45, 34, 32, 20, 20,
     20, 45, 45, 40, 12, 48, 67, 90, 0, 56, 12, 45, 67, 45, 34, 32, 20, 20]
# n = 36

n1 = L[:7]
n2 = L[7:7+13]
n3 = L[7+13:]

selection_sort(n1)
selection_sort(n2)
selection_sort(n3)

print(merge_sort(n1, n2, n3))
