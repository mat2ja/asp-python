'''1. Napišite funkciju je_bsp koja vraća True ako je zadano stablo binarno stablo pretraživanja
ili False ako nije'''


def je_bsp(root):
    turn_to_preorder(root)
    # print("Preordered:", root)

    flat_list = flatten(root)
    # print("Flatten:", flat_list)

    sorted_list = [e for e in flat_list]
    sorted_list.sort()
    # print("Sorted:", sorted_list)

    for i in range(len(flat_list)):
        if flat_list[i] != sorted_list[i]:
            return False

    return True


def turn_to_preorder(root):
    if isinstance(root, list):
        root[0], root[1] = root[1], root[0]
        for v in root:
            turn_to_preorder(v)


def flatten(root):
    flat = []
    for elem in root:
        if isinstance(elem, list):
            flat += flatten(elem)
        else:
            flat.append(elem)
    return flat


# Grgic
def je_bsp(lista):
    if not isinstance(lista, list):
        return True

    manji = lista[1]
    veci = lista[2]
    if isinstance(lista[1], list):
        manji = lista[1][0]
    if isinstance(lista[2], list):
        veci = lista[2][0]

    if lista[0] < manji or lista[0] > veci:
        return False
    return je_bsp(lista[1]) and je_bsp(lista[2])



print("\nSljedeci trebaju biti True:")
# print(je_bsp([1, 0]))
print(je_bsp([2, 1, 3]))
print(je_bsp([5, [3, 2, 4], 10]))
print(je_bsp([5, [3, 2, 4], [10, 6, [20, 15, 40]]]))
print(je_bsp([10, 2, 12]))
print(je_bsp([10, [6, 2, 8], [16, 12, 20]]))
print(je_bsp([20, [15, 8], 30]))
print(je_bsp([50, [44, 30, 48], [80, [66, 60, 67], 88]]))
print(je_bsp([20, [15, 8, 20], [30, 28, [32, 31, 33]]]))
print(je_bsp([20, [15, 8, [18, [17, 15], 19]], [30, 28, [32, 31, 33]]]))

print("\nSljedeci trebaju biti False:")
print(je_bsp([5, [3, 2, 19], 10]))
print(je_bsp([5, [3, 2, 12], 10]))
print(je_bsp([10, [6, 2, 8], [16, [13, 5, 15], 20]]))
# print(je_bsp([20, [15, 8, [20, [10, 8, 35], 100]], [30, 28, [32, 31]]]))


print("\nLabos test cases (treba true pa false):")
print(je_bsp([50, [44, 30, 48], [80, [66, 60, 67], 88]]))
print(je_bsp([50, [44, 30, 48], [49, [66, 60, 67], 88]]))
