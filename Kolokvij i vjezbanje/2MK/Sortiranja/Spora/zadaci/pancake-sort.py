# Python3 program to
# sort array using
# pancake sort

# Reverses arr[0..i] */
def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1


# Returns index of the maximum
# element in arr[0..n-1] */
def findMax(arr):
    mi = 0
    for i in range(0, len(arr)):
        if arr[i] > arr[mi]:
            mi = i
    return mi


# The main function that
# sorts given array
# using flip operations


def pancakeSort(arr):

    # Start from the complete
    # array and one by one
    # reduce current size
    # by one
    curr_size = len(arr)
    while curr_size > 1:
        # Find index of the maximum
        # element in
        # arr[0..curr_size-1]

        # mi = findMax(arr, curr_size)
        mi = arr.index(max(arr[:curr_size]))

        # Move the maximum element
        # to end of current array
        # if it's not already at
        # the end
        if mi != curr_size-1:
            # To move at the end,
            # first move maximum
            # number to beginning
            flip(arr, mi)

            # Now move the maximum
            # number to end by
            # reversing current array
            flip(arr, curr_size-1)
        curr_size -= 1


# Driver program
arr = [23, 10, 20, 11, 12, 6, 7]
pancakeSort(arr)
print("Sorted Array ")
print(arr)

# This code is contributed by shreyanshi_arun.
