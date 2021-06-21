'''
selection sort

Best Case: Theta(𝑛2)
Worst Case: O(𝑛2)
'''


def selection_sort(original):
    arr = original[:]
    n = len(arr)

    for i in range(n):
        idx_min = i
        for j in range(i+1, n):
            if arr[j] < arr[idx_min]:
                idx_min = j
        arr[idx_min], arr[i] = arr[i], arr[idx_min]
        # print(f"Korak {i+1}: {arr}")

    return arr


# copy arr
# arr = [i for i in original]
# arr = list(original)
# arr = original.copy()
