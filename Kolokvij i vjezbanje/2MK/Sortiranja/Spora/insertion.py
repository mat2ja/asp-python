'''
Insertion sort
Best Case: O(n)
Worst Case: O(𝑛2)
'''

def insertion_sort(original):
    arr = original[:]

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

