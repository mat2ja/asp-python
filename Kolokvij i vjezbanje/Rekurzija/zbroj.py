# 1. Napišite rekurzivnu funkciju koja vraća zbroj svih vrijednosti u listi koja sadrži samo brojeve.

def zbroji(lista):
    if len(lista) <= 0:
        return 0
    else:
        return lista[0] + zbroji(lista[1:])


def zbroji2(lista):
    return lista[0] + zbroji(lista[1:]) if len(lista) > 0 else 0


def zbroji3(lista):
    return lista[-1] + zbroji(lista[:-1]) if len(lista) > 0 else 0


print(zbroji3([]))
print(zbroji3([20]))
print(zbroji3([1, 2, 3, 4, 5]))
