'''
a) Napište funkciju merge_sort koja ovaj algoritam implementira rekurzivno.
b) Proširite gornju implementaciju tako da daje ukupan broj usporedbi vrijednosti. Isto
    napravite i za vašu implementaciju bubble sort algoritma i usporedite i komentirajte
    rezultate.
c) Nađite veličinu niza kod koje funkcija bubble_sort sortira brže od funkcije merge_sort.
Objasnite zašto je to tako.
'''

mergeCounter = 0
bubbleCounter = 0


def merge_sort(arr):

    if len(arr) <= 1:
        return

    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        global mergeCounter
        mergeCounter = mergeCounter + 1
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return mergeCounter


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        switched = False
        for j in range(0, n-i-1):
            global bubbleCounter
            bubbleCounter = bubbleCounter + 1
            if arr[j] > arr[j+1]:
                switched = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not switched:
            break
    return arr


def reset_counters():
    global mergeCounter
    mergeCounter = 0
    global bubbleCounter
    bubbleCounter = 0


A = [38, 27, 43, 3, 9, 82, 10]
B = A[:]
merge_sort(A)
print("Merge: ", A)
bubble_sort(B)
print("Bubble:", B)
print(
    f"Merge je imao {mergeCounter} usporedba, a Bubble {bubbleCounter} usporedba\n")

reset_counters()

C = [1, 2, 3, 4, 5, 6, 7]
D = C[:]
merge_sort(C)
print("Merge: ", C)
bubble_sort(D)
print("Bubble:", D)
print(
    f"Merge je imao {mergeCounter} usporedba, a Bubble {bubbleCounter} usporedba")
