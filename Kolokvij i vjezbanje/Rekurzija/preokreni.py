# 2. Napišite rekurzivnu funkciju preokreni koja preokreće listu.

def preokreni(lista):
    if len(lista) <= 0:
        return lista

    lista[0], lista[-1] = lista[-1], lista[0]
    preokreni(lista[1:-1])
    return lista


def preokreni2(lista):
    if not lista:
        return lista
    return [lista[-1]] + preokreni2(lista[:-1])


def preokreni3(lista):
    if not lista:
        return lista
    return preokreni3(lista[1:]) + [lista[0]]


print(preokreni([1, 2, 3, 4, 5]))
print(preokreni2([1, 2, 3, 4, 5]))
print(preokreni3([1, 2, 3, 4, 5]))

print(preokreni([1, 2]))
print(preokreni2([1, 2]))
print(preokreni3([1, 2]))

print(preokreni([1]))
print(preokreni2([1]))
print(preokreni3([1]))

print(preokreni([]))
print(preokreni2([]))
print(preokreni3([]))
