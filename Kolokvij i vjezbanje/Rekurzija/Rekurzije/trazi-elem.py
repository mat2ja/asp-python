# Potrebno je napisati rekurzivnu funkciju koja za zadanu ugnježđenu listi(nested list) određuje da li se u listi nalazi(True) ili ne nalazi(False) zadani elemnt.

def trazi_element_u_NL(lista, trazeni):
    for elem in lista:
        if isinstance(elem, list):
            if trazi_element_u_NL(elem, trazeni):
                return True
        elif elem == trazeni:
            return True
    return False


A = [1, [2, [3], 4]]
B = [1, [2, [3], 4]]
C = [[2, 4], [6, [[[8, 11], 10]], 12], 14, 16]
D = [['x', 'y'], ['z', 'p'], ['m', ['a', 'b', 'c', ['d', 'e']]]]
print(trazi_element_u_NL(A, 4))  # True
print(trazi_element_u_NL(B, 5))  # False
print(trazi_element_u_NL(C, 11))  # True
print(trazi_element_u_NL(D, "f"))  # True
