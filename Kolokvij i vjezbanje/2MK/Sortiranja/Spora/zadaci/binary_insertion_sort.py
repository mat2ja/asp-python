# binary insertion sort

def binary_search(arr, val, start, end):
    # moramo razlikovati gdje moramo napraviti insert prije ili poslije lijeve granice
    # zamislite da je [0] zadnji korak binarnog traženja i mi moramo odlučiti gdje insertiramo -1
    print("\nISPIS ARR", arr)
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    # this occurs if we are moving beyond left\'s boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    print("\nISPIS U BS", val, start, end, end=" ")
    if start > end:
        return start

    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid


def insertion_sort(arr):
    print(arr, end=" ")
    for i in range(1, len(arr)):
        print("\n", i, arr[i], end=" ")
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr


print("Sortirano polje:")
print("\n", insertion_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]))
