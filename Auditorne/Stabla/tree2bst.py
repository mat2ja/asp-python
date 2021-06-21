# Program za konverziju BS u BST
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
# Čvor binarnog stabla
from binarytree import Node


class Node:

    # Konstruktor za kreiranje novog čvor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Helper function to store the inroder traversal of a tree
def storeInorder(root, inorder):

    # Osnovni slucaj
    if root is None:
        return

    # Prvo pospremimo lijevo podstablo
    storeInorder(root.left, inorder)

    # dodajemo podatak za root
    inorder.append(root.data)

    # Konačno pospremimo desno podstablo
    storeInorder(root.right, inorder)

# A helper funtion to count nodes in a binary tree


def countNodes(root):
    if root is None:
        return 0

    return countNodes(root.left) + countNodes(root.right) + 1

# Helper function that copies contents of sorted array
# to Binary tree


def arrayToBST(arr, root):

    # Osnovni slučaj
    if root is None:
        return

    # Prvo obnovimo lijevo podstablo
    arrayToBST(arr, root.left)

    # obnovim podatak za root i brišemo ga iz polja
    root.data = arr[0]
    arr.pop(0)

    # Konačno obnovimo desno podstablo
    arrayToBST(arr, root.right)

# Ova funkcija konvertira BS u BST


def binaryTreeToBST(root):

    # BOsnovni slučaj: Stablo je prazno
    if root is None:
        return

    # Prebrojimo broj čvorova u Ninatrnom stablu
    # kako bi znali veličinu pomočnog polja koje moramo kreirati
    n = countNodes(root)

    # Kreiramo temp polje i pospremimo u inorder obilazak
    # stabla
    arr = []
    storeInorder(root, arr)

    # Sortiramo polje
    arr.sort()

    # kopiramo polje elemnata nazad u binarno stablo
    arrayToBST(arr, root)

    # Inorder ispis


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data)
    printInorder(root.right)


def printPreorder(root):

    if root:

        # printamo roditelja
        print(root.data),

        # prvo rekurzivno idemo na lijevo dijete
        printPreorder(root.left)

        # Konačno rekrzivno idemo na desno dijete
        printPreorder(root.right)


def printPostorder(root):

    if root:
        # prvo rekurzivno idemo na lijevo dijete
        printPreorder(root.left)

        # Konačno rekrzivno idemo na desno dijete
        printPreorder(root.right)

        # printamo roditelja
        print(root.data),


count_leaf = 0


def ispisListova(root):
    global count_leaf
    if root.left == None and root.right == None:

        count_leaf = count_leaf + 1
        print(root.data)
    else:
        if root.left != None:
            ispisListova(root.left)
        if root.right != None:
            ispisListova(root.right)

# dodano - rekurzivni minimum i maximum


def minValue(root):
    if (root.left is None):
        return root.data

    if (root.left is not None):
        return minValue(root.left)


def maxValue(root):
    if (root.right is None):
        return root.data

    if (root.right is not None):

        return maxValue(root.right)


def get_tree_height(root):
    if root is None:
        return -1

    else:
        return (max(get_tree_height(root.left), get_tree_height(root.right)) + 1)


# Driver program za testiranje funkcije
if __name__ == "__main__":

    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    print("Inorder ispis binarnog stabla")
    printInorder(root)
    print("Poziv funkcije za konverziju:")
    # Konverzija BS u BST
    binaryTreeToBST(root)

    print("Inorder obilazak konvertiranog BST")
    print("Vidimo da je Inorder obilazak BST sortirani niz za razliku od obilaska BS ")
    printInorder(root)

    print("visina")
    print(get_tree_height(root))

    print("Inorder ispis binarnog stabla")
    printInorder(root)

    print("Preorder ispis binarnog stabla")
    printPreorder(root)

    print("Postorder ispis binarnog stabla")
    printPostorder(root)
