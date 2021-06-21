# 3. Napišite funkciju koja sortira elemente tako da uzastopno traži najmanji element u listi
# (pod uvjetom da je prethodni najmanji element uklonjen iz liste). Koja je vremenska
# složenost ove funkcije?

def sortiraj(lista):
    nova_lista = []
    while len(lista):
        smallest = lista[0]
        for i in range(1, len(lista)):
            if lista[i] < smallest:
                smallest = lista[i]
        lista.remove(smallest)
        nova_lista.append(smallest)

    return nova_lista


# selection sort
def sortiraj_s(lista):
    for i in range(len(lista)):
        idxMin = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[idxMin]:
                idxMin = j
        lista[i], lista[idxMin] = lista[idxMin], lista[i]

    return lista


# bubble sort
def sortiraj_b(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


print(sortiraj([4, 1, 3, 0, 21, 2, 11]))
print(sortiraj_s([4, 1, 3, 0, 21, 2, 11]))
print(sortiraj_b([4, 1, 3, 0, 21, 2, 11]))
