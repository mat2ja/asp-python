# 1. Upotrebom mape napišite funkciju frekv koja vraća broj pojavljivanja svih elementa liste.

def frekv(arr, broj):
    freq = {}
    for n in arr:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    broj_ponavljanja = 0
    for k in freq:
        if k == broj:
            broj_ponavljanja = freq[k]
            break
    return broj_ponavljanja


def frekv(arr, broj):
    freq = {n: arr.count(n) for n in arr}
    return freq[broj] if broj in freq else 0


print(frekv([1, 2, 1, 2, 3, 1, 1, 4], 1))
print(frekv([1, 2, 1, 2, 3, 1, 1, 4], 143))
