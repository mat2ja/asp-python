def napravi_binarno_stablo(values):
    stablo = [None, None, None]
    for v in values:
        if stablo[0] is None:
            stablo.append(v)
        elif v <= stablo[0]:
            if not stablo[1]:
                stablo[1] = [].append(v)
        elif v >= stablo[0]:
            stablo[2] = [].append(v)
    return stablo

# Grgic
# def napravi_binarno_stablo(lista):
#     stablo = Tree()
#     for element in lista:
#         stablo.add(element)
#     return stablo.toList(stablo.root)


# Grgic
# def dubina_bsp(lista, d=0):
#     if not isinstance(lista, list) or len(lista) < 1:
#         return d
#     x = dubina_bsp(lista[1], d + 1)
#     y = dubina_bsp(lista[2], d + 1)
#     if x > y:
#         return x
#     return y

print(napravi_binarno_stablo([17, 8, 31, 12, 9, 45, 29, 32, 56]))
