'''
2 zadatak
Zadan je niz brojeva S = [20, 30, 25, 21, 25, 9, 5, 27, 5, 23, 21, 4, 5, 25, 5, 20, 22, 20, 26, 25, 4, 24, 23, 20, 16, 5, 11, 25, 16, 22, 9, 6, 29, 27, 5, 15, 11, 3, 16, 12, 7, 16, 18, 29, 1, 14, 17, 20, 7, 1]

Napišite funkciju koja će na najučinkovitiji način sortirati brojeve ali po frekvenciji pojave svakog broja u podajućem redoslijedu npr [32 32 32 32 8 8 8 21 21 ….].
'''


# todo

# def partition(arr, start, end):
#     pivot = arr[end]
#     low = start
#     high = end - 1

#     while True:

#         if low < high and arr.count(arr[low]) > arr.count(arr[pivot]):
#             low += 1

#         if low < high and arr.count(arr[high]) < arr.count(arr[pivot]):
#             high -= 1

#         if low <= high:
#             arr[low], arr[high] = arr[high], arr[low]
#             low += 1
#             high -= 1
#         else:
#             break

#         arr[end], arr[low] = arr[low], arr[end]
#         return low


# def quick_sort(arr, start, end):
#     if start >= end:
#         return

#     pi = partition(arr, start, end)
#     quick_sort(arr, start, pi-1)
#     quick_sort(arr, pi+1, end)
#     return arr

from collections import Counter


def sortiraj_po_frekv2(arr):
    result = [item for items, c in Counter(
        arr).most_common() for item in [items] * c]
    return result


# def sortiraj_po_frekv(arr):
#     mapa = {}
#     for v in arr:
#         if v in mapa:
#             mapa[v] += 1
#         else:
#             mapa[v] = 1

#     new_arr = []

#     for k, v in {k: v for k, v in sorted(mapa.items(),  key=lambda item: item[1])}:
#         for i in range(v):
#             new_arr.append(k)

#     return new_arr


S = [20, 30, 25, 21, 25, 9, 5, 27, 5, 23, 21, 4, 5, 25, 5, 20, 22, 20, 26,  25, 4, 24, 23, 20,
     16, 5, 11, 25, 16, 22, 9, 6, 29, 27, 5, 15, 11, 3, 16, 12, 7, 16, 18, 29, 1, 14, 17, 20, 7, 1]

print(sortiraj_po_frekv(S))
