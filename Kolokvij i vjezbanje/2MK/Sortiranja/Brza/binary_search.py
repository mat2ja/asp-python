# Programski kod za binarno pretraživanje
# Vraća indeks od  x ako je nađen u arr , u protivnom -1
def binarySearch(arr, l, r, x):

    # Provjera baznog slučaja
    if r >= l:

        mid = l + (r - l)//2

        # Ako je lement prisutan na sredini vrati indeks
        if arr[mid] == x:
            return mid
        # Ako je manji od sredine može biti samo u lijevom podpolju
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        # U protivnom može biti samo u desnom podpolju
        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        # Element nije prisutan u polju
        return -1


# moja varijanta
def bs(arr, x):
    n = len(arr)

    if n < 1:
        return -1

    mid = n//2

    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return bs(arr[:mid], x)
    else:
        return bs(arr[mid+1:], x)


def print_result(res):
    if res != -1:
        print("Element je prisutan na indeksu %d" % res)
    else:
        print("Element nije prisutan u polju")


arr = [2, 3, 4, 10, 40]
x = 2

# Poziv funkcije
result1 = binarySearch(arr, 0, len(arr)-1, x)
result2 = bs(arr, x)

print_result(result1)
print_result(result2)
