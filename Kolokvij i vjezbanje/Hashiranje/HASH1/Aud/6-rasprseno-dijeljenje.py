from random import randint, seed

seed(a=23489765, version=2)

SIZE = 110
p = 199  # prim broj, mora bit veci od tabele


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node


class HashTable():
    def __init__(self):
        self.size = SIZE
        self.table = [LinkedList() for i in range(self.size)]
        self.stored = 0
        self.kolizije = 0

    def dodaj(self, elem):
        if self.jePuna():
            print("Tablica je puna")
            return

        h = self.hashiraj(elem)

        if self.table[h].head is not None:
            self.kolizije += 1

        self.table[h].insert(elem)
        self.stored += 1

    def jePuna(self):
        if self.stored == self.size:
            return True
        return False

    def hashiraj(self, n):
        a = randint(0, p-1)
        b = randint(1, p-1)
        # return n % SIZE # 51 kol
        return ((a*n + b) % p) % SIZE  # 39 kol

    def prikazi(self):
        for k in range(self.size):
            print(f"ADRESA {k}:", end=" ")
            curr = self.table[k].head
            while curr:
                print(curr.value, end=" -> ")
                curr = curr.next
            print("")


T = HashTable()


arr = [randint(i, 100) for i in range(100)]

for n in arr:
    T.dodaj(n)

T.prikazi()
print("\nBroj kolizija:", T.kolizije)
