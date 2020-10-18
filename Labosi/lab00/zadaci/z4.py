"""Upotrebom mape (dictionary) napišite funkciju frekv koja vraća broj pojavljivanja svakog elementa liste:"""


def frekv(lista):
    mapa = {}
    for elem in lista:
        mapa[elem] = mapa[elem] + 1 if elem in mapa else 1
    return mapa


print(frekv([5, 2, 4, 4, 3, 1, 3, 8]))
