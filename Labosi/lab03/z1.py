# 1. Implementirajte cirkularnu(kružnu) jednostruko vezanu listu kod koje posljednji element
# ima vezu s onim prvim. Neka vaša klasa ima metodu iduci koja slijedi veze među elementima
# kružne liste i koja uvijek daje iduci element liste(to jest, nikad ne dolazi do kraja).

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None

    def iduci(self, element=None):
        if not element:
            return self.head.value
        return element.next.value

    def size(self):
        size = 0
        temp = self.head
        if temp:
            size = 1
        else:
            return 0
        while temp.next is not self.head:
            size += 1
            temp = temp.next
        return size

    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return new_node.value

        last = self.head
        while last.next is not self.head:
            last = last.next

        last.next = new_node
        new_node.next = self.head
        return new_node.value

    def printList(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return

        while temp.next is not self.head:
            print(temp.value)
            temp = temp.next
        print(temp.value)

    def postoji_ciklus(self):
        if self.head:
            return True
        return False

    def prva_tri(self):
        if self.size() <= 0:
            return (0,)
        elif self.size() <= 1:
            return (self.head.value,)
        elif self.size() <= 2:
            first = self.head
            second = first.next
            return (first.value, second.value)
        else:
            first = self.head
            second = first.next
            third = second.next
            return (first.value, second.value, third.value)


if __name__ == '__main__':
    llist = CircularList()

    print("Postoji ciklus:", llist.postoji_ciklus())

    print("Prva 3:", llist.prva_tri())
    llist.push(2)
    print("Prva 3:", llist.prva_tri())
    llist.push(3)
    print("Prva 3:", llist.prva_tri())
    llist.push(45)
    llist.push(6)
    print("Prva 3:", llist.prva_tri())

    print("Postoji ciklus:", llist.postoji_ciklus())

    print("Ispis liste:")
    llist.printList()

    print("Size:", llist.size())
    print("Prvi element:", llist.iduci())
    print("Drugi element:", llist.iduci(llist.head))
    print("Treci element:", llist.iduci(llist.head.next))
    print("Prvi element:", llist.iduci(llist.head.next.next.next))

    print(llist.prva_tri())
