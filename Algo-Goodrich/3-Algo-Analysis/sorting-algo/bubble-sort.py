import random
a = [random.randint(1, 100) for i in range(8)]


def sort(L):
    n = len(L)
    for i in range(n-1):
        for j in range(i+1, n):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L


print("Original: ", a)
print("Sorted  : ", sort(a))
