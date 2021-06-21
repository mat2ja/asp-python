

# Čvor binarnog stabla

class newNode:

    # Konstruktor novog čvora
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None

# Preoreder obilazak BST


def preorder(root):

    if (root != None):

        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

# Funkcija za kreiranje stabla


def constructTrees(start, end):

    list = []

    #  ako je start > end stablo je prazno
    if (start > end):

        list.append(None)
        return list

    # iteriranje kroz sve vrijednosti
    # od start do end radi izgradnje
    # lijevog i desnog podstabla rekurzivno
    for i in range(start, end + 1):

        #  rekurzivna izgradnja lijevog podstabla
        #print("lijevo", start, i-1)
        leftSubtree = constructTrees(start, i - 1)

        #  rekurzivna izgradnja desnog podstabla
        #print("desno", i+1, end)
        rightSubtree = constructTrees(i + 1, end)

        # prolazak kroz sva lijeva i desna
        # podstabla i povezivanje na  root

        for j in range(len(leftSubtree)):
            left = leftSubtree[j]
            for k in range(len(rightSubtree)):
                right = rightSubtree[k]
                node = newNode(i)   # vrijednost i postaje root
                node.left = left    # spoji lijevo podstablo
                node.right = right    # spoji desno podstablo
                list.append(node)    # dodaj to stablo u listu

    return list


# Napravi sva moguća BST
rezultat = constructTrees(1, 5)

# ispis preorder obilaska za sva izgrađena stabla
nBST = len(rezultat)
print("Preorder obilasci za svih {} izgrađenih BST su:".format(nBST))

for i in range(nBST):
    preorder(rezultat[i])
    print()
