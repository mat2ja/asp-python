def checkIfHasChildren(lista):
    if isinstance(lista, list):
        return True
    else:
        return False


def getMinChild(lista):
    element1 = 0
    element2 = 0
    if checkIfHasChildren(lista[1]):
        element1 = lista[1][0]
    else:
        element1 = lista[1]
    if checkIfHasChildren(lista[2]):
        element2 = lista[2][0]
    else:
        element2 = lista[2]
    if element1 == None:
        return 2
    if element2 == None:
        return 1
    if element1 < element2:
        return 1
    else:
        return 2


def getMaxChild(lista):
    element1 = 0
    element2 = 0
    if checkIfHasChildren(lista[1]):
        element1 = lista[1][0]
    else:
        element1 = lista[1]
    if checkIfHasChildren(lista[2]):
        element2 = lista[2][0]
    else:
        element2 = lista[2]
    if element1 == None:
        return 1
    if element2 == None:
        return 2
    if element1 > element2:
        return 1
    else:
        return 2


def rearrangeDown(lista):
    if checkIfHasChildren(lista):
        minChild = getMinChild(lista)
        element2 = 0
        if checkIfHasChildren(lista[minChild]):
            element2 = lista[minChild][0]
        else:
            element2 = lista[minChild]
        if lista[0] > element2:
            if checkIfHasChildren(lista[minChild]):
                lista[minChild][0], lista[0] = lista[0], lista[minChild][0]
                rearrangeDown(lista[minChild])
            else:
                lista[minChild], lista[0] = lista[0], lista[minChild]


def dodajJednom(lista, element):
    if checkIfHasChildren(lista):
        maxChild = getMaxChild(lista)
        if lista[maxChild] == None:
            lista[maxChild] = element
            return "Dodano"
        if checkIfHasChildren(lista[maxChild]):
            poppedElement = lista[maxChild][0]
            lista[maxChild][0] = element
            dodajJednom(lista[maxChild], poppedElement)
        else:
            poppedElement = lista[maxChild]
            lista[maxChild] = [element, poppedElement, None]


def dodaj(lista, element):
    stariVrh = lista[0]
    lista = [element, lista[1], lista[2]]
    dodajJednom(lista, stariVrh)
    #[2, [5,[15,16,25],[9,14,12]], [6,[7,11,13],20]]]
    rearrangeDown(lista)
    print(lista)


dodaj([4, [5, [15, 16, 25], [9, 14, 12]], [6, [7, 11, 13], 20]], 2)
