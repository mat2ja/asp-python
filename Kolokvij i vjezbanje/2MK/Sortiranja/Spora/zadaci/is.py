from random import randint


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j] # povlacimo gore na mjesto keya
            j -= 1 # idemo dalje ulijevo
        arr[j+1] = key # stavljamo key na pravo mjesto

    return arr



A = [randint(1,30) for i in range(12)]
print(A)
print(insertion_sort(A))
