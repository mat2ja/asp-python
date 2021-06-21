def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high -= 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low += 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1
            # The loop continues
        else:
            # We exit out of the loop
            break
        print("🟣", array)

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    print("🟡", array)
    p = partition(array, start, end)
    print("🟢", array)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


A = [8, 3, 1, 10, 12, 2, 14, 4, 6]
quick_sort(A, 0, len(A)-1)
print(A)
