# definirana je klasa za generiranje čvora

# Čvor binarnog stabla
class Node:

    # Konstruktor za kreiranje novog čvor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Funkcija koja pronalazi sumu svih čvorova roditelja koji imaju
# čvor dijete s vrijednosti x.
# Umjesto pass napisati potrebni kod
def SumOfParentOfX(root, Sum, x):
    if root is None or root.right is None or root.left is None:
        return Sum

    if root.right.data == x or root.left.data == x:
        Sum += root.data
        Sum = SumOfParentOfX(root.left, Sum, x)
        Sum = SumOfParentOfX(root.right, Sum, x)
    return Sum


# pomočna funkcija koja poziva funkciju za određivanje sume
def SumOfParentOfXUtil(root, x):
    Sum = [0]
    SumOfParentOfX(root, Sum, x)

    # tražena suma roditeljskih čvorova
    return Sum[0]


# Driver kod
# Umjesto pass napisati potrebni kod
if __name__ == '__main__':

    # formiranje binarnog stabla i određivanje tražene sume
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(2)
    root.right.left = Node(2)
    root.right.right = Node(3)

    print(SumOfParentOfX(root, 0, 2))
