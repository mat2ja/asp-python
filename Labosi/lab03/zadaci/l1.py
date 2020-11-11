""" 1. Implementirajte cirkularnu (kružnu) jednostruko vezanu listu kod koje posljednji element
ima vezu s onim prvim. Neka vaša klasa ima metodu iduci koja slijedi veze među elementima
kružne liste i koja uvijek daje iduci element liste (to jest, nikad ne dolazi do kraja). """


class Node:
    def __init__(self, data):
        self._next = None
        self._data = data


class CircularList:
    def __init__(self):
        self.head = None

    def add(self, elem):
        if not isinstance(elem, Node):
            elem = Node(elem)

        if self.head is None:
            self.head = elem
        else:
            self.last()._next = elem
        elem._next = self.head
        return self

    def first(self):
        return self.head

    def last(self):
        last = self.head
        if last is None:
            return None

        while last._next != self.head:
            last = last._next
        return last

    def size(self):
        if not self.head:
            return 0
        size = 1
        e = self.head
        while e != self.last():
            size += 1
            e = e._next
        return size

    def print_list(self):
        e = self.head
        if not e:
            print("List is empty")
            return
        if e._next is None:
            print(e._data)
            return
        while e._next != self.head:
            print(e._data)
            e = e._next
        print(e._data)
        return

    def iduci(self, elem):
        if not elem or self.size() < 1:
            return "Element ne postoji"
        if elem._next is None:
            return "Element nema idući"
            return
        return elem._next._data

    def postoji_ciklus(self):
        if self.head is None:
            return "Ne postoji ciklus"
        return "Postoji ciklus"


A = Node(12)
B = Node(34)
clist = CircularList()
clist.add(A)
clist.add(B)
clist.add(99)
clist.add(178)
clist.add(Node(345))

clist.print_list()
print(f"Size is {clist.size()}")

print(clist.iduci(clist.first()))
print(clist.iduci(B))
print(clist.iduci(clist.last()))

print(clist.postoji_ciklus())
