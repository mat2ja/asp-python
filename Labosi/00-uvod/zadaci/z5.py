"""Upotrebom skupova napišite funkciju koja vraća broj duplikata u listi (bez upotrebe petlje ili rekurzije):"""


def duplikati(lista):
    return len(lista) - len(set(lista))


print(duplikati([5, 2, 5, 1, 1, 1, 2, 3]))
