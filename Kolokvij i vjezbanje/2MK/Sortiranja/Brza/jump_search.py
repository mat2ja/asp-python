import math


def jumpSearch(arr, x, n):

    # Određivanje veličine bloka (kotrak) za skokove
    step = math.sqrt(n)

    # Traženje bloka gdje je element prisutan (ako je prisutan)

    prev = 0

    while arr[int(min(step, n)-1)] < x:
        #print(step, prev,arr[int(min(step, n)-1)])
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Radimo lienarno traženje elementa x u bloku koji počinje s prev

    while arr[int(prev)] < x:
        prev += 1

        # Ako smo dostigli sljedeći blok ili kraj polja element nije prisutan

        if prev == min(step, n):
            return -1

    # Ako je element nađen
    if arr[int(prev)] == x:
        return prev

    return -1


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]
x = 55
n = len(arr)

# Tražimo indeks od 'x' korištenjem Jump Search
index = jumpSearch(arr, x, n)

# Ispis indeksa trađženog elementa
print("Broj", x, "je nađen na indeksu ", "%.0f" % index)
