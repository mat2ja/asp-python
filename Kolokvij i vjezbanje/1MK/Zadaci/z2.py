class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Lista:
    def __init__(self, lista=None):
        self.head = None
        self.tail = None

        if lista is not None:
            for elem in lista:
                self.append(elem)

    def prepend(self, data):
        node = Node(data)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data)

        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node

    def previousNode(self, ref_node):
        current = self.head
        while current and current.next != ref_node:
            current = current.next
        return current

    def remove(self, value, start_node=None):
        if self.head is None:
            return

        if start_node is None:
            prev = None
            current = self.head
        else:
            current = start_node
            prev = self.previousNode(current)

        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print(f"\tNode with value {value} was not found")
            return
        elif prev is None:
            self.head = self.head.next
        else:
            prev.next = current.next

    def size(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def display(self):
        if not self.head:
            print("List is empty")
        current = self.head
        while current:
            print(current.data, end=", ")
            current = current.next
        print()



def izdvoji(lista):
    if not lista.head:
        return

    nova_lista = Lista([])
    curr = lista.head
    while curr:
        data = curr.data
        if data % 2 == 0:
            lista.remove(data, curr)
            nova_lista.append(data)
        curr = curr.next
    return nova_lista


def ispis(lista):
    head = lista.head
    if not head:
        print("List is empty")

    current = head
    while current:
        print(current.data, end=", ")
        current = current.next
    print()


L = Lista([8, 7, 6, 5, 4, 3, 2, 1])
ispis(izdvoji(L))  # ispis mora biti ovakav: 8, 6, 4, 2
ispis(L)  # ispis mora biti ovakav: 7, 5, 3, 1
