import random
a = [random.randint(1, 100) for i in range(3)]


def sort(L):
    n = len(L)
    for i in range(n-1):
        # We first assume that the first element is the lowest
        min_index = i
        for j in range(i+1, n):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]
    return L


print("Original: ", a)
print("Sorted  : ", sort(a))
