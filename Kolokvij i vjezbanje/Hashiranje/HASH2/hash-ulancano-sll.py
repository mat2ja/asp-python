SIZE = 8


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

    def dodaj(self, elem):
        if self.jePuna():
            print("Tablica je puna")
            return

        h = self.hashiraj(elem)
        print(f"Dodajem {elem} na poz {h}")
        self.table[h].insert(elem)
        self.stored += 1

    def jePuna(self):
        if self.stored == self.size:
            return True
        return False

    def hashiraj(self, element):
        return element % self.size

    def prikazi(self):
        for slot in range(self.size):
            print(f"Key {slot}:", end=" ")
            print(f"\tValues:", end=" ")

            curr = self.table[slot].head
            while curr:
                print(curr.value, end=" -> ")
                curr = curr.next
            print("")

    def pronadji(self, k):
        h = self.hashiraj(k)
        found = False

        curr = self.table[h].head
        while curr and not found:
            if curr.value == k:
                found = True
            else:
                curr = curr.next

        if found:
            print(f"Key {k} found at slot {h}")
            return h
        else:
            print(f"Key {k} not found")


T = HashTable()
T.dodaj(30)
T.dodaj(24)
T.dodaj(4)
T.dodaj(10)
T.dodaj(11)
T.dodaj(54)
T.dodaj(500)
T.dodaj(65)
T.dodaj(9)
T.dodaj(88)
T.dodaj(62)


T.prikazi()

T.pronadji(500)
T.pronadji(502)
