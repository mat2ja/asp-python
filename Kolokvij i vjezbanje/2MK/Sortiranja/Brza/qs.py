def partition(arr, start, end):
    pivot = arr[end]
    low = start
    high = end - 1

    while low < high:

        while low <= high and arr[low] < pivot:
            low += 1

        while low <= high and arr[high] > pivot:
            high -= 1

        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
            # napravimo da low bude veci od high
            low += 1
            high -= 1
    print("🟣", arr)

    # umetnemo pivota (end) na pravo mjesto
    # pivota mjenjamo sa low jer su low i high isprepleteni i s krivim vrijednostima, zato su i stali
    # low ima veci broj i na vecem je indeksu
    arr[end], arr[low] = arr[low], arr[end]

    return low


def quick_sort(arr, start, end):
    if start >= end:
        return

    # print("🟡", arr)
    pi = partition(arr, start, end)

    # print("🟢", arr)
    quick_sort(arr, start, pi-1)
    quick_sort(arr, pi+1, end)

    return arr


A = [8, 3, 1, 10, 12, 2, 14, 4, 6]
print(f"Unsorted: {A}")
quick_sort(A, 0, len(A)-1)
print(A)
