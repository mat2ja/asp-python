
def kalkDubina(lista):
    max_dubina = 0
    for elem in lista:
        if isinstance(elem, list):
            dubina = kalkDubina(elem)
            if dubina > max_dubina:
                max_dubina = dubina
    return max_dubina + 1


A = [1, [2], 1, [2, [3]]]
B = [1, 1, [2, [3], [3, [4, 4, 4]]], 1, [2, [3, 3, [4, [5]]]]]
C = ['a', ['b', 'c', [['d']], '[[[X]]]']]

print(kalkDubina(A))
print(kalkDubina(B))
print(kalkDubina(C))
