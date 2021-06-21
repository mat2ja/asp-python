

def frekv_sort(arr):
    frekvencije = {}
    for item in arr:
        if item in frekvencije:
            frekvencije[item] += 1
        else:
            frekvencije[item] = 1

    for i in range(1, len(arr)):
        current = arr[i]
        j = i-1

        while j >= 0 and frekvencije[current] > frekvencije[arr[j]]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current

    print(arr)


frekv_sort([4, 4, 1, 5, 4, 1, 8, 2])  # [4, 4, 4, 1, 1, 5, 8, 2]
frekv_sort([4, 3, 1, 5, 5, 1, 8, 2])
frekv_sort([1, 5, 4, 1, 8, 2, 4, 4])
