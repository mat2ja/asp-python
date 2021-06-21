class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarnoStablo:
    def __init__(self):
        self.podatak = None
        self.lijevi = None
        self.desni = None

    def provjeri_dubinu(self, current):
        if self.lijevi is None and self.desni is None:
            return current
        elif self.lijevi is None:
            return self.desni.provjeri_dubinu(current+1)
        elif self.desni is None:
            return self.lijevi.provjeri_dubinu(current+1)
        else:
            depth_left = self.lijevi.provjeri_dubinu(current+1)
            depth_right = self.desni.provjeri_dubinu(current+1)
            if depth_left > depth_right:
                return depth_left
            else:
                return depth_right

    def dubina(self):
        return self.provjeri_dubinu(0)

    def umetni(self, podatak, node='root'):  # <-- DOVRŠITI OVU METODU
        kljuc = podatak[0]
        vrijednost = podatak[1]
        print(kljuc, vrijednost)

        if node == "root":
            node = self.podatak

        if node is None:
            return Node(podatak)

        # if vrijednost <= node.value:
        #     node.left = self.umetni(podatak, node.left)
        # elif vrijednost > node.value:
        #     node.right = self.umetni(podatak, node.right)

    def ispis(self, dubina):  # <-- DOVRŠITI OVU METODU
        print(self)


# elementi iz kojih je potrebno izgraditi potpuno binarno stablo su:
# ('A', 113), ('B', 89), ('C', 126), ('D', 102), ('E', 123), ('F', 107), ('G', 117)

stablo = BinarnoStablo()
stablo.umetni(('A', 113))
stablo.umetni(('B', 89))
stablo.umetni(('C', 126))
...

# ispis
stablo.ispis(0)

# ----------------------------------

"""
Ispis treba biti u obliku

korijen
    desno podstablo (svi elementi veći od korijena)
    lijevo podtstablo (svi elementi manji od korijena)

Na primjer,
(A, 5)
    (C, 9)
        (H, 12)
        (G, 8)
    (B, 1)
        (D, 3)
            (F, 4)
            (E, 2)
        None
"""


# def umetni(self, value):  # <-- DOVRŠITI OVU METODU
#     if self.podatak is None:
#         self.podatak = Node(value)
#     else:
#         self.__umetni(value, self.podatak)


def __umetni(self, value, node):
    if value.__getitem__(1) < node.tuple.__getitem__(1):
        if node.left is not None:
            self.__umetni(value, node.left)
        else:
            node.left = Node(value)
    else:
        if node.right is not None:
            self.__umetni(value, node.right)
        else:
            node.right = Node(value)
