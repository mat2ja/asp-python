# 1. slučaj - Kvadratni problem
def quad(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        # Računamo j-tu usrednjenu vrijednost na osnovu prethodnih i vrijednosti polja S[i]
        A[j] = total / (j+1)
    return A

print(quad([10, 20, 5, 4, 8]))


# 2. slučaj - Koristi se funkcija sum() iz Pythona
def summ(S):
    n = len(S)
    A = [0] * n

    for j in range(n):
        # j-ta usrednjena vrijednost izračunata korištenjem Python funkcije sum().Ž
        A[j] = sum(S[0:j+1])/(j+1)
    return A

print(summ([10, 20, 5, 4, 8]))



# Koristi se prethodni rezultat
def prev(S):
    n = len(S)
    A = [0] * n

    for j in range(n):
        if j == 0:
            A[j] = S[j]
        else:
            A[j] = (A[j-1]*j + S[j]) / (j+1)
    return A

print(prev([10, 20, 5, 4, 8]))
