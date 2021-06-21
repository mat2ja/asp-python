# 5. Napišite rekurzivnu funkciju dubina koja utvrđuje maksimalnu dubinu liste.
# Primjerice, lista ['a', ['b', 'c', [['d']], '[[[X]]]']] ima dubinu 3 (na kojoj se nalazi element ‘d’; element ‘a’ je na dubini 0, element '[[[X]]]' je string, ne lista).

def izr_dubinu(lista):
    if not isinstance(lista, list):
        return -1  # ako vracamo -1 u slucaju greske

    max_dubina = 0
    for elem in lista:
        if isinstance(elem, list):
            dubina = izr_dubinu(elem) + 1
            if dubina > max_dubina:
                max_dubina = dubina

    return max_dubina 


# A = [1, [2], 1, [2, [3]]]
# B = [1, 1, [2, [3], [3, [4, 4, 4]]], 1, [2, [3, 3, [4, [5]]]]]
# C = ['a', ['b', 'c', [['d']], '[[[X]]]']]

# print(izr_dubinu("nijelista"))  # -1
# print(izr_dubinu([]))  # 0
# print(izr_dubinu([1, 2]))  # 0
# print(izr_dubinu(A))  # 2
# print(izr_dubinu(B))  # 4
# print(izr_dubinu(C))  # 3

