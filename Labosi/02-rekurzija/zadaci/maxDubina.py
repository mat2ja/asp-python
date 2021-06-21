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


A = [1, [2], 1, [2, [3]]]
B = [1, 1, [2, [3], [3, [4, 4, 4]]], 1, [2, [3, 3, [4, [5]]]]]
C = ['a', ['b', 'c', [['d']], '[[[X]]]']]

print(izr_dubinu(A))
print(izr_dubinu(B))
print(izr_dubinu(C))
print("['a', ['b', 'c', [['d']], '[[[X]]]']]:", izr_dubinu(
    ['a', ['b', 'c', [['d']], '[[[X]]]']]))  # 3
print("['a', ['b', 'c', [['d']], [[['X']]]]]:",
      izr_dubinu(['a', ['b', 'c', [['d']], [[['X']]]]]))
