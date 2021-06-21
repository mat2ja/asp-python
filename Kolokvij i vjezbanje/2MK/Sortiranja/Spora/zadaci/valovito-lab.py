# 4. Sortiranje niza u obliku vala

# Zadani nesortirani niz cijelih brojeva, sortirajte kao niz u obliku vala kao npr. 'niz arr [0..n-1]' sortiran je u obliku vala ako je arr[0] > = arr[1] <= arr[2] > = arr[3] <= arr[4] > = ... .

# Primjer:

# Ulaz: arr[] = [3, 6, 5, 10, 7, 20]

# Sortirani izlaz: arr[] = [6, 3, 10, 5, 20, 7]

# U ovom primjeru vidimo praktički dva sortirana niza, gdje je prvi niz ima vrijednosti na indeksima 0, 2, 4 .. (parni indeksi), a drugi niz ima vrijednosti na neparnim indeksima 1, 3, 5... (neparni). Implemntirajte algoritam sortiranja koji neće imati goru vremensku složenost od O(n log n). U driver programu pokažite funkcioniranje vašeg algoritma na nizu od N = 50 slučajno generiranih brojeva između 1 i 100. Ispisati prvo nesortirani niz, a zatim valno sortirani niz.

# Preporuka: sortirati niz koristeći bilo koji algoritam sortiranja(može Python funkcija sort()). Zatim swop dviju susujednih vrijednosti da dobijete valovito sortiran niz.

from random import randint


def valno_sortiraj_2(original):
    n = len(original)

    even = [original[i] for i in range(n) if i % 2 != 1]
    odd = [original[i] for i in range(n) if i % 2 == 1]

    odd.sort()
    even.sort()

    arr = []
    for i in range(0, n//2 + 1):
        if i < len(even):
            arr.append(even[i])
        if i < len(odd):
            arr.append(odd[i])

    for i in range(1, n):
        if i % 2 == 1:
            if arr[i-1] < arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr


def valno_sortiraj(original):
    arr = original[:]
    n = len(arr)

    special_insertion_sort(arr, n)

    for i in range(1, n):
        if i % 2 == 1:
            if arr[i-1] < arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]

    return arr


def special_insertion_sort(arr, n):
    for i in range(2, n):
        num = arr[i]
        j = i-2
        while j >= 0 and num < arr[j]:
            arr[j+2] = arr[j]
            j -= 2
        arr[j+2] = num
    return arr


A = [3, 6, 5, 10, 7, 20]
B = [3, 6, 5, 10, 7, 20, 4]
# C = [3, 60, 5, 10, 7, 20, 4]
# D = [6, 16, 1, 3, 21, 7, 9, 22]

# print("A", A)                  # [3, 6, 5, 10, 7, 20]
print(" ", valno_sortiraj(A))  # [6, 3, 10, 5, 20, 7]
# print("B", B)                  # [3, 6, 5, 10, 7, 20, 4]
print(" ", valno_sortiraj(B))  # [6, 3, 10, 4, 20, 5, 7]
# print("C", C)                  # [3, 60, 5, 10, 7, 20, 4]
# print(" ", valno_sortiraj(C))  # [10, 3, 20, 4, 60, 5, 7]
# print("D", D)                  # [6, 16, 1, 3, 21, 7, 9, 22]
# print(" ", valno_sortiraj(D))  # [3, 1, 7, 6, 16, 9, 22, 21]


# randArr = [randint(1, 100) for i in range(10)]

# print(randArr)
# print(valno_sortiraj(randArr))
# # print(valno_sortiraj_ss(randArr))
# print(valno_sortiraj_2(randArr))
# # [12, 19, 28, 9, 10, 20, 21, 23]
# # [10, 9, 19, 12, 28, 20, 23, 21]
# # [10, 9, 19, 12, 21, 20, 28, 23]


# Python function to sort the array arr[0..n-1] in wave form,
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]
def sortInWave(arr):
    n = len(arr)

    # sort the array
    arr.sort()
    # print(arr)

    # Swap adjacent elements
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]


arr = [3, 6, 5, 10, 7, 20]
sortInWave(arr)
print(arr)
