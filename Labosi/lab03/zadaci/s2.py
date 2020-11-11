class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinked():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def size(self):
        len = 0
        if self.head and self.tail:
            current = self.head
            while current is not self.tail:
                current = current.next
                len += 1
        return len

    def print_list(self):
        if not (self.head and self.tail):
            return "List is empty"
        current = self.head
        while current is not self.tail.next:
            print(current.data)
            current = current.next


dllist = DoubleLinked()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(0)

dllist.print_list()
print("Size:", dllist.size())


class Stog:
    def __init__(self):
        self.dllist = DoubleLinked()

    def push(self, elem):
        self.dllist.append(elem)

    def pop(self):
        last_elem = self.dllist.tail
        pass
