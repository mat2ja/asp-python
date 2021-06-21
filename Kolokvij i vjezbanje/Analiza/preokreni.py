'''
4. Napišite funkciju koja preokreće elemente liste (na primjer, za listu [1, 2, 3] daje listu
[3, 2, 1]). Koja je vremenska složenost vaše funkcije?
'''

# O(log(n))
def preokreni(lista):
    for i in range(len(lista) // 2):
        lista[i], lista[-i-1] = lista[-i-1], lista[i]
    return lista


print(preokreni([4, 3, 2, 1]))
print(preokreni([3, 2, 1]))
