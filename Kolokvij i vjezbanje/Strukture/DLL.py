class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def insertAfter(self, prev_value, value):
        node = Node(value)

        if self.head is None:
            return

        current = self.head
        while current and current.data != prev_value:
            current = current.next

        if current is None:
            print(f"\tNode with value {prev_value} is not in the list")
            return

        if current.next is None and current.data == prev_value:
            self.append(value)
        elif current.data == prev_value:
            nxt = current.next
            current.next = node
            node.prev = current
            nxt.prev = node
            node.next = nxt

    def insertBefore(self, next_value, value):
        node = Node(value)

        if self.tail is None:
            return

        current = self.tail
        while current and current.data != next_value:
            current = current.prev

        if current is None:
            print(f"\tNode with value {next_value} is not in the list")
            return

        if current.prev is None and current.data == next_value:
            self.prepend(value)
        elif current.data == next_value:
            prev = current.prev
            prev.next = node
            node.prev = prev
            node.next = current
            current.prev = node

    def display(self):
        output = []
        current = self.head
        while current:
            output.append(current.data)
            current = current.next
        print(output)

    def displayReverse(self):
        output = []
        current = self.tail
        while current:
            output.append(current.data)
            current = current.prev
        print(output)

    def size(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def removeFirst(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = self.tail = None
        else:
            nxt = self.head.next
            nxt.prev = None
            self.head = nxt

    def removeLast(self):
        if not self.tail:
            return

        if not self.tail.prev:
            self.head = self.tail = None
        else:
            prev = self.tail.prev
            prev.next = None
            self.tail = prev

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

    def removeDuplicates(self):
        if not self.head:
            return

        current_1 = self.head
        while current_1:
            data = current_1.data
            current_2 = current_1.next
            while current_2:
                if current_2.data == data:
                    self.removeNode(current_2)
                current_2 = current_2.next
            current_1 = current_1.next

    def countOccurences(self, value):
        count = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

    def removeKthNode(self, k):
        if k > self.size() or self.head is None:
            return

        n = 1
        node = self.head
        while node:
            if n == k:
                self.removeNode(node)
                n = 1
            else:
                n += 1
            node = node.next

    def removeKthNodeReverse(self, k):
        if k > self.size() or self.tail is None:
            return

        n = 1
        node = self.tail
        while node:
            if n == k:
                self.removeNode(node)
                n = 1
            else:
                n += 1
            node = node.prev


dlist = DoubleLinkedList()
for i in range(5, 10):
    dlist.append(i)
for i in range(4, 0, -1):
    dlist.prepend(i)

print("Printing list")
dlist.display()
# dlist.displayReverse()
print("Size:", dlist.size())

dlist.insertAfter(9, 9999)
dlist.display()

dlist.remove(1)
dlist.remove(9999)
dlist.display()

dlist.prepend(2)
dlist.append(2)
dlist.append(2)
dlist.display()
print("Count of 2:", dlist.countOccurences(2))

dlist.removeDuplicates()
dlist.display()
print("Count of 2:", dlist.countOccurences(2))

dlist.removeKthNode(2)
dlist.display()
dlist.removeKthNodeReverse(2)
dlist.display()
