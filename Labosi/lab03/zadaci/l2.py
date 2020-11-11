
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
        while last._next:
            last = last._next
        last._next = new_node

    def delete(self, elem):
        current = self.head

        if current is None:
            return

        if current and current._data == elem:
            self.head = current._next
            return

        prev = None
        while current._next and current._data != elem:
            prev = current
            current = current._next

        if current is None:
            return

        prev._next = current._next

    def print_list(self):
        if self.head is None:
            return "List is empty"

        e = self.head
        while e is not None:
            print(e._data)
            e = e._next


llist = LinkedList()
llist.add(Node(1))
llist.add(2)
llist.add(3)
llist.add(4)
llist.add(5)
print("Prvi print:")
llist.add_to_start(0)
llist.print_list()

llist.delete(-99)  # ne postoji
llist.delete(0)
llist.delete(4)
print("\nDrugi print:")
llist.print_list()
