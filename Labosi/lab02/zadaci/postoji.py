def postoji(trazeni, lista):
    if trazeni in lista:
        return True

    for elem in lista:
        if isinstance(elem, list):
            if postoji(trazeni, elem):
                return True

    return False


print(postoji(2, [1, 2, 3, 4]))
print(postoji(999, [1, 2, 3, 4]))

A = ['a', [['b', 'c'], 'd', ['e']], 'f']
print(postoji('e', A))
print(postoji('c', A))
print(postoji('w', A))
