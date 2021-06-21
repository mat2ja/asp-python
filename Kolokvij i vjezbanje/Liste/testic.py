class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newdata):
        self.value = newdata

    def setNext(self, newpointer):
        self.pointer = newpointer


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()

    def _delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

    def _add(self, value):
        self.length += 1
        self.head = Node(value, self.head)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = 0
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def delete_node(self, index):
        node, prev, i = self._find(index)
        if index == i:
            self._delete(prev, node)
        else:
            print('Node s indeksom {} nije nadjen'.format(index))

    # moje
    def delete_node_by_value(self, value):
        prev = None
        curr = self.head

        if not curr:
            print("List is empty")
            return

        while curr and curr.value != value:
            prev = curr
            curr = curr.pointer

        if curr is None:
            print(f"{value} not found in the list")
            return
        elif prev is None:
            self.head = curr.pointer
        else:
            prev.pointer = curr.pointer
        curr = None

    # moje
    def insert_after(self, prev_value, node_value):
        new_node = Node(node_value)

        curr = self.head

        if not curr:
            print("List is empty")
            return

        while curr and curr.value != prev_value:
            curr = curr.pointer

        if curr is None:
            print(f"{prev_value} not found")
            return

        next_node = curr.pointer
        curr.pointer = new_node
        new_node.pointer = next_node

    def insert_before(self, next_value, node_value):
        new_node = Node(node_value)

        prev = None
        curr = self.head

        if not curr:
            print("List is empty")
            return

        while curr and curr.value != next_value:
            prev = curr
            curr = curr.pointer

        if curr is None:
            print(f"{next_value} not found")
            return

        if prev is None:
            new_node.pointer = self.head
            self.head = new_node
        else:
            prev.pointer = new_node
            new_node.pointer = curr

    # zbroji trenutni i prethodni
    def izmijeni_node_value(self, value):
        prev = None
        curr = self.head

        if not curr:
            print("List is empty")
            return

        while curr and curr.value != value:
            prev = curr
            curr = curr.pointer

        if curr is None:
            print(f"{value} not found")
            return

        if prev is None:
            prev_value = 0
        else:
            prev_value = prev.value

        if curr.pointer is None:
            next_value = 0
        else:
            next_value = curr.pointer.value

        curr.value = prev_value + next_value


ll = LinkedList()
for i in range(1, 5):
    ll._add(i)
print('Lista je:')
ll._printList()
print(ll.head.value)
ll.delete_node_by_value(5)
ll.delete_node_by_value(2)
ll._printList()
ll.insert_after(3, 90)
ll._printList()
ll.insert_before(90, 88)
ll._printList()
ll.izmijeni_node_value(88)
ll._printList()
