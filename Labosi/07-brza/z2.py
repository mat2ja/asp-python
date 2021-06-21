from z1 import merge_sort, bubble_sort

'''
a) Napišite funkciju quick_sort koja ovaj algoritam implementira rekurzivno.
b) Generirajte 10 nizova koji se sastoje od 10.000 slučajnih brojeva. Za svaki niz pozovite
quick_sort funkciju i izmjerite vrijeme izvršavanja. Sada generirajte jedan niz od 10.000
brojeva sortiranih u rastućem poretku i izmjerite vrijeme izvršavanja, te komentirajte
rezultat.
c) Za svaki od gore generiranih nizova pozovite i vašu funkciju za merge-sort i usporedite
vremena te funkcije s ovom za quick-sort
'''

from copy import deepcopy
from random import randint
from time import time


def quick_sort(arr, start, end):
    if start >= end:
        return

    pi = partition(arr, start, end)
    quick_sort(arr, start, pi-1)
    quick_sort(arr, pi+1, end)


def partition(arr, start, end):
    pivot = arr[end]
    low = start
    high = end - 1

    while True:

        while low <= high and arr[low] <= pivot:
            low += 1

        while low <= high and arr[high] >= pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
        else:
            break

    arr[end], arr[low] = arr[low], arr[end]

    return low


A = [38, 27, 43, 3, 9, 82, 10]
B = A[:]
quick_sort(A, 0, len(A)-1)
print("Quick: ", A)
merge_sort(B)
print("Merge: ", B)

nizovi = []

for i in range(10):
    rand_array = [randint(1, 10000) for i in range(10000)]
    nizovi.append(rand_array)

nizoviA = deepcopy(nizovi)
nizoviB = deepcopy(nizovi)
nizoviC = deepcopy(nizovi)

startQ = time()
for niz in nizoviA:
    quick_sort(niz, 0, len(niz)-1)
endQ = time()
print(f"\nQuick sort took {endQ-startQ} ms")


startM = time()
for niz in nizoviB:
    merge_sort(niz)
endM = time()
print(f"Merge sort took {endM-startM} ms")


#startB = time()
#for niz in nizoviC:
#    bubble_sort(niz)
#endB = time()
#print(f"Bubble sort took {endB-startB} ms")


# for 50,000
#Quick sort took 1.7932462692260742 ms
#Merge sort took 3.8788604736328125 ms
