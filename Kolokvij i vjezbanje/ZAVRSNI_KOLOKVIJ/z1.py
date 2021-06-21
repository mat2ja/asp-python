# Dodajte kôd na označeno mjesto tako da funkcija bsp_ispis elemente binarnog stabla
# ispisuje u sortiranom redoslijedu od najmanjeg prema najvećem.


# def flatten(root):
#     flat = []
#     for elem in root:
#         if isinstance(elem, list):
#             flat += flatten(elem)
#         else:
#             flat.append(elem)
#     return flat
output = []


def flatten(root, output):
    for elem in root:
        if isinstance(elem, list):
            flatten(elem, output)
        else:
            output.append(elem)
            output.sort()
    return output


def bsp_ispis(root):
    if isinstance(root, list):
        root = flatten(root, [])
        for elem in root:
            bsp_ispis(elem)

    else:
        if root is not None:
            print(root, end=" ")


# def bsp_ispis(start):
#     if start:
#         if isinstance(start[1], list) and len(start) > 1:
#             bsp_ispis(start[1])
#         elif len(start) > 1:
#             bsp_ispis(start[1])
#         print(start, end=" ")
#         if isinstance(start[2], list):
#             bsp_ispis(start[2])
#         elif len(start) > 1:
#             bsp_ispis(start[2])


bsp_ispis([50, [44, 30, 48], [80, [66, 60, 67], 88]])
