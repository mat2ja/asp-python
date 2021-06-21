class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:

    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)

        if self.is_empty():
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        node.prev = curr
        curr.next = node

    def prepend(self, value):
        node = Node(value)

        if self.is_empty():
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def is_empty(self):
        if not self.head:
            return True

    def display(self):
        if self.is_empty():
            print("List is empty")
            return

        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def size(self, node='default'):
        if node == 'default':
            node = self.head
        if not node:
            return 0
        return 1 + self.size(node.next)

    def find_node_by_value(self, value):
        if self.is_empty():
            print("List is empty")
            return

        curr = self.head
        while curr and curr.data != value:
            curr = curr.next

        if curr is None:
            print(f"{value} not found")
        else:
            return curr

    def remove_node(self, node):
        if not node:
            return
        if not node.prev and not node.next:
            self.head = None
        elif not node.prev:
            nxt = self.head.next
            self.head = nxt
            nxt.prev = None
        elif not node.next:
            prev = node.prev
            prev.next = None
        else:
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev

        node = None

    def remove_node_by_value(self, value):
        node_to_remove = self.find_node_by_value(value)
        if node_to_remove is None:
            return
        self.remove_node(node_to_remove)

    def remove_kth_node(self, k):
        if self.is_empty():
            return

        count = 1
        curr = self.head
        while curr:
            if count % k == 0:
                self.remove_node(curr)
            count += 1
            curr = curr.next


dllist = DLL()
for i in range(1, 6):
    dllist.append(i)
dllist.display()

dllist.prepend(99)
dllist.prepend(199)
dllist.prepend(299)
dllist.append(777)

dllist.display()
print("size:", dllist.size())

node99 = dllist.find_node_by_value(99)
node777 = dllist.find_node_by_value(777)
node778 = dllist.find_node_by_value(777)

dllist.display()
dllist.remove_node(node99)
dllist.display()
dllist.remove_node(node777)
dllist.display()
dllist.remove_node(node778)
dllist.display()

dllist.remove_node_by_value(299)
dllist.display()
dllist.remove_kth_node(3)
dllist.display()
