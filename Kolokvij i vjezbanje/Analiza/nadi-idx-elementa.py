# Potrebno je napisati funkciju find() koja vraća index traženog elementa(item) ako je zadana lista L i element koji se traži. Kratko komentirati.

def find(lista, item):
    for elem in lista:
        if elem == item:
            return lista.index(elem)
    return "Not found"


def find2(lista, elem):
    return lista.index(elem) if elem in lista else "Not found"


def find3(lista, elem):
    try:
        return lista.index(elem)
    except ValueError:
        return "Not found"


print(find([1, 3, 5, 12, 52, 5, 6], 5))  # 2
print(find([1, 3, 5, 12, 52, 5, 6], 555))  # False

print(find2([1, 3, 5, 12, 52, 5, 6], 5))  # 2
print(find2([1, 3, 5, 12, 52, 5, 6], 555))  # False

print(find3([1, 3, 5, 12, 52, 5, 6], 5))  # 2
print(find3([1, 3, 5, 12, 52, 5, 6], 555))  # False
