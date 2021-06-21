class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def removeNode(self, node):
        prev = self.previousNode(node)
        if prev is None:
            self.head = self.head.next
        else:
            prev.next = node.next
        if node.next is None:
            self.tail = prev

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

        if current.next is None:
            self.append(value)
        elif current.data == prev_value:
            node.next = current.next
            current.next = node

    def size(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def sizeRecursive(self, node):
        if not node:
            return 0
        return 1 + self.sizeRecursive(node.next)


    def display(self):
        if not self.head:
            print("List is empty")
        print("Printing list", end=": ")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def clear(self):
        self.head = None
        self.tail = None

    def countOccurences(self, value):
        count = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

    def countOccurencesRecursive(self, node, value):
        if not node:
            return 0
        elif node.data != value:
            return self.countOccurencesRecursive(node.next, value)
        else:
            return 1 + self.countOccurencesRecursive(node.next, value)

    def removeDuplicates(self):
        current_1 = self.head

        while current_1:
            data = current_1.data
            current_2 = current_1.next
            while current_2:
                if current_2.data == data:
                    self.removeNode(current_2)
                current_2 = current_2.next
            current_1 = current_1.next

    def firstN(self, N=3):
        values = []
        current = self.head
        i = 0
        while current and i < N:
            values.append(current.data)
            current = current.next
            i += 1

        if len(values) == 0:
            return "List is empty"

        return tuple(values)

    def lastN(self, N=3):
        values = []
        current = self.head
        list_size = self.size()

        while current and list_size > N:
            current = current.next
            list_size -= 1

        while current:
            values.append(current.data)
            current = current.next

        if len(values) == 0:
            return "List is empty"

        return tuple(values)

    def swapNodes(self, value_1, value_2):
        if value_1 == value_2:
            return

        prev_1 = None
        current_1 = self.head
        while current_1 and current_1.data != value_1:
            prev_1 = current_1
            current_1 = current_1.next

        prev_2 = None
        current_2 = self.head
        while current_2 and current_2.data != value_2:
            prev_2 = current_2
            current_2 = current_2.next

        # node value isnt found as we iterated over entire list
        if not current_1 or not current_2:
            return

        if prev_1:
            prev_1.next = current_2
            if current_1.next is None:
                self.tail = current_2
        else:
            self.head = current_2

        if prev_2:
            prev_2.next = current_1
            if current_2.next is None:
                self.tail = current_1
        else:
            self.head = current_1

        current_1.next, current_2.next = current_2.next, current_1.next
