def preokreni(lista):
    if len(lista) < 2:
        return lista
    else:
        lista[0], lista[-1] = lista[-1], lista[0]
        preokreni(lista[1:-1])
        return lista


print(preokreni([1, 2, 3, 4]))
print(preokreni([1, 2, 3]))
print(preokreni([1, 2]))
print(preokreni([1]))
print(preokreni([]))
