'''
bubble sort

Best Case: Theta(𝑛) - ako je vec sortiran
Worst Case: O(𝑛2) - selection je 60% brzi
'''

# usporedujemo susjedne elemente, najveci ispliva na kraj


def bubble_sort(original):
    arr = original[:]
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # print(f"Korak {i+1}: {arr}")

    return arr


# ako je sortirano, izat ce iz pelje nakon te iteracije iteracije
def bubble_sort_optimized(original):
    arr = original[:]
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort_2(original):
    arr = original[:]
    n = len(arr)

    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr


a = [15, 7, 6, 11, 31, 1, 5, 14, 25, 28]

print(bubble_sort_2(a))
