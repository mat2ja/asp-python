def partition(arr, low, high):
    i = low - 1         # index manjeg elementa
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # Ako je trentni element manji ili jednak pivitu
        if arr[j] <= pivot:

            # inkrement indeksa manjeg elementa
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:

        # pi indeks particioniranja, arr[p] je sada
        # na pravom mjestu
        pi = partition(arr, low, high)
        print("prvi prolaz", arr)

        # Odvojeno sortirati elemente prije particioniranja i nakon particioniranja
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


A = [8, 3, 1, 10, 12, 2, 14, 4, 9]
quick_sort(A, 0, len(A)-1)
print(A)
