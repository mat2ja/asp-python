def dubina_elementa(trazeni, lista, dubina=-1):
    exists = False
    for elem in lista:
        if elem == trazeni:
            exists = True
            dubina += 1
            break
        elif isinstance(elem, list):
            exists, dubina = dubina_elementa(trazeni, elem, dubina)
            if exists:
                dubina += 1
                break
    return exists, dubina


def test(trazeni, lista):
    exists, dubina = dubina_elementa(trazeni, lista)
    if exists:
        print(f"Element {trazeni} nalazi se na dubini {dubina}")
    else:
        print(f"Element {trazeni} ne nalazi se u listi")


test('a', [['a'], [['b'], 'c'], ['d', ['e']], 'f'])
test('g', [['a'], [['b'], 'c'], ['d', ['e']], 'f'])
test('f', [['a'], [['b'], 'c'], ['d', ['e']], 'f'])
test('b', [['a'], [['b'], 'c'], ['d', ['e']], 'f'])
