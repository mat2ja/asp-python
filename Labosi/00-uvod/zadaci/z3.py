"""Napišite funkciju sortiraj koja sortira vrijednosti tako da svaki put nađe najmanju vrijednost u nizu."""


def sortiraj(niz):
    return sorted(niz)

# bubble sort


def sortirajBubble(niz):
    for i in range(len(niz) - 1):
        for j in range(0, len(niz) - i - 1):
            if niz[j] > niz[j + 1]:
                niz[j], niz[j + 1] = niz[j + 1], niz[j]
    return niz

# selection sort


def sortirajSelection(niz):
    for i in range(len(niz)):
        minIdx = i  # index najmanjeg je trenutni index
        for j in range(i + 1, len(niz)):
            if niz[j] < niz[minIdx]:
                minIdx = j
        niz[minIdx], niz[i] = niz[i], niz[minIdx]
    return niz


# print(sortiraj([243, 12, 5, 132, 45, 11, 29]))
# print(sortirajBubble([243, 12, 5, 132, 45, 11, 29]))
print(sortirajSelection([243, 12, 5, 132, 45, 11, 29]))

print('hey')
