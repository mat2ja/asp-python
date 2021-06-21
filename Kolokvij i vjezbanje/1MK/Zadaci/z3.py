class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Lista:
    def __init__(self, lista=None):
        self.head = None
        self.tail = None

        if lista is not None:
            for elem in lista:
                self.append(elem)

    def prepend(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, data):
        node = Node(data)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def display(self):
        output = []
        current = self.head
        while current:
            output.append(current.data)
            current = current.next
        print(output)

    def size(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def remove(self, value, start_node=None):
        if not self.head:
            return

        if start_node is None:
            current = self.head
        else:
            current = start_node

        while current and current.data != value:
            current = current.next

        if current.prev is None:
            self.removeFirst()
        elif current.next is None:
            self.removeLast()
        else:
            nxt = current.next
            prev = current.prev
            nxt.prev = prev
            prev.next = nxt

    def removeNode(self, node):
        if node.prev is None and node.next is None:
            self.head = self.tail = None
        elif node.prev is None:
            nxt = node.next
            self.head = nxt
            nxt.prev = None
        elif node.next is None:
            prev = node.prev
            self.tail = prev
            prev.next = None
        else:
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev

    def removeFirst(self):
        if self.head is None:
            return
        self.head = self.head.next

    def removeLast(self):
        if self.tail is None:
            return

        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next

        if prev is None:
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev


def izdvoji(lista):
    if not lista.head:
        return

    nova_lista = Lista([])
    curr = lista.head
    i = 1
    while curr:
        data = curr.data
        if i % 2 == 1:
            lista.removeNode(curr)
            nova_lista.append(data)
        i += 1
        curr = curr.next
    return nova_lista


def ispis(lista):
    tail = lista.tail
    if not tail:
        print("List is empty")

    current = tail
    while current:
        print(current.data, end=", ")
        current = current.prev
    print()


L = Lista(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
ispis(izdvoji(L))  # ispis mora biti obratnim redoslijedom: g, e, c, a
ispis(L)  # ispis mora biti obratnim redoslijedom: h, f, d, b
# Složenost ostvarenja je: _?_
