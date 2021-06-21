import random
import time

# Python program za implementaciju heap Sort algoritma

# Funkcija za izgradnju (heapify) podstabla koji ima root za indeks i
# n je veličina gomile


def heapify(arr, n, i):
    largest = i  # Inicijalizacija največeg kao korijen (root)
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # Provjera da li lijevo dijete root-a postoji i da li je veće od root-a
    if l < n and arr[i] < arr[l]:
        largest = l

    # Provjera da li desno dijete root-a postoji i da li je veće od root-a
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Promijeni root ako treba
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify  root
        heapify(arr, n, largest)


# Glavna funkcija za sortiranje polja zadane duljine n
def heapSort(arr):
    n = len(arr)

    # Izgradnja maxheapa
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Izdavajanje jednog po jednog elementa
    # radi sortiranja.
    # Poslije svakog izdvajanja treba ponovno izgraditi hrpu (heap)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver program
arr = [4, 12, 11, 13, 5, 6, 7]
heapSort(arr)
print("\nSortirano polje je: ")
for i in arr:
    print(i, end=" ")
