'''
shell sort
'''


from random import randint


def shell_sort(original):
    arr = original[:]
    n = len(arr)

    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr


a = [15, 7, 6, 11, 31, 1, 5, 14, 25, 28]

print(shell_sort(a))
