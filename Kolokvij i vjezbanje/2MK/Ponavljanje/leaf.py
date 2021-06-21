'''
Napisati funkciju programa koja će prebrojiti čvorove binarnog stabla koji su listovi. Čvor je list ako su oba djeteta(lijevo i desno) jednaka NULL. Odgovoriti koja je vremenska složenost u O-notaciji.

Algoritam:

Definicija funkcije:

getLeafCount(node)

1) ako je čvor NULL tada vrati 0.
2) u protivnom ako su i lijevo i desno dijete čvora jednaki NULL vrati 1.
3) u protivnom rekurzivno prebroji listove stabla prema formuli

Leaf count of a tree=Leaf count of left subtree + Leaf count of right subtree
'''

from binarytree import Node


def prebroji_listove(root):
    if root is None:
        return 0
    if not root.left and not root.right:
        return 1
    return prebroji_listove(root.left) + prebroji_listove(root.right)

def suma_listova(root):
    if root is None:
        return 0
    if not root.left and not root.right:
        return root.value
    return suma_listova(root.left) + suma_listova(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(9)
root.right.left = Node(6)
root.right.left.right = Node(8)
root.right.left.left = Node(18)
print(root)
print(f"Broj listova je {prebroji_listove(root)}")
print(f"Suma listova je {suma_listova(root)}")
