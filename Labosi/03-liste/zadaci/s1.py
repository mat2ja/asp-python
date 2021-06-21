class Node:
    def __init__(self, data):
        self._next = None
        self._data = data


class LinkedList:
    def __init__(self):
        self.head = None

    # dodavanje na kraj
    def add_to_start(self, elem):
        if not isinstance(elem, Node):
            new_node = Node(elem)
        else:
            new_node = elem

        new_node._next = self.head
        self.head = new_node

    def add(self, elem):
        if not isinstance(elem, Node):
            new_node = Node(elem)
        else:
            new_node = elem

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last._next is not None:
            last = last._next
        last._next = new_node

    def delete(self, elem):
        current = self.head

        if current and current._data == elem:
            self.head = current._next
            return

        prev = None
        while current and current._data != elem:
            prev = current
            current = current._next

        if current is None:
            return

        prev._next = current._next

    def last(self):
        current = self.head
        if not current:
            return None
        while current._next:
            current = current._next
        return current

    def print_list(self):
        if self.head is None:
            return "List is empty"

        e = self.head
        while e is not None:
            print(e._data)
            e = e._next


class Stog:
    def __init__(self):
        self._llist = LinkedList()

    def push(self, elem):
        self._llist.add(elem)

    def pop(self):
        last_node = self._llist.last()
        if not last_node:
            return "Stog je prazan"
        self._llist.delete(last_node._data)
        return last_node._data

    def print_stog(self):
        self._llist.print_list()


S = Stog()
S.push(7)
S.push(17)
S.push(27)
S.push(37)
S.push(47)
S.pop()

S.print_stog()
