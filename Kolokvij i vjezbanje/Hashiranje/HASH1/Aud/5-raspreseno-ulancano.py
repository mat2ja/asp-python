SIZE = 110


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

    def hashiraj(self, string):
        suma = 0
        for i in range(len(string)):
            # suma += ord(string[i])
            suma += ord(string[i]) * i+1
        return suma % self.size

    def prikazi(self):
        for k in range(self.size):
            print(f"ADRESA {k}:", end=" ")
            curr = self.table[k].head
            while curr:
                print(curr.value, end=" -> ")
                curr = curr.next
            print("")


T = HashTable()

a = "Toni Dominik Antonio Mate Josip Anto Ivan Ivan Branimir Franjo Danijel Klara Matija Igor Filip Tin Emanuel Sven Mihael Kristijan Kristina Ante Enis Maksimilijan Antonio Josip Ozren Mateo Franjo Lovro Krešimir Oton Marko Jerko Josip Juraj Franjo Ruža Marina Franjo Krešimir Elvis Jakov Filip Bruno Andy Dominik Stjepan Mateo Domagoj Stjepan Vedrana Franjo Patrik Ivan Tomislav Nikola Dominik Armando Marko Paul"
imena = a.split()
imena = set(imena)
for e in imena:
    T.dodaj(e)


T.prikazi()

print("\nBroj kolizija:", T.kolizije)

print(T.stored)
print(len(imena))
# elemCount = len(imena)
# prazni = 0
# for lista in T.table:
#     if lista.head is None:
#         prazni += 1
# print(f"U tablici of {elemCount} elemenata je {prazni} praznih celija")
