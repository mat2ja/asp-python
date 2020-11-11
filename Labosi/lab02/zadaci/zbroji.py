def zbroji(lista):
    if len(lista) <= 0:
        return 0
    else:
        return lista[0] + zbroji(lista[1:])


print(zbroji([]))
print(zbroji([20]))
print(zbroji([1, 2, 3, 4, 5]))
