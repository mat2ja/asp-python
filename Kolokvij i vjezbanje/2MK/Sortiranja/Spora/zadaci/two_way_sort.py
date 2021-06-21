'''Sort all even numbers in ascending order and then sort all odd numbers in descending order Given an array of integers(both odd and even), sort them in such a way that the first part of the array contains odd numbers sorted in descending order, rest portion contains even numbers sorted in ascending order.'''


def two_way_sort(arr):
    left = 0
    right = len(arr)-1

    # count the number of odd nums
    k = 0

    while left < right:
        # while left is odd
        while arr[left] % 2 != 0:
            left += 1
            k += 1

        while arr[right] % 2 == 0 and left < right:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    odd = arr[:k]
    even = arr[k:]

    odd.sort(reverse=True)
    even.sort()

    return odd+even



arr = [1, 3, 2, 7, 5, 4, 14, 6, 22, 48, 21, 33]
result = two_way_sort(arr)
print(result)
