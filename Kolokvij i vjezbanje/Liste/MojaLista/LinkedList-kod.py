class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def _print_list(self):
        node = self.head
        if not node:
            print("[ Lista je prazna ]")
        else:
            while node:
                print(node.data)
                node = node.next

    def _add(self, data):
        self.length += 1
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def _delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.next
        else:
            prev.next = node.next

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.data == value:
                found = True
            else:
                prev = node
                node = node.next
        return node, prev, found

    def deleteNode(self, index):
        node, prev, i = self._find(index)
        if index == i:
            self._delete(prev, node)
        else:
            print(f"Node s indeksom {index} nije nađen")

    def deleteNodeByValue(self, value):
        node, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev, node)
        else:
            print(f"Node s vrijednošću {value} nije nađen")


ll = LinkedList()
for i in range(5):
    ll._add(i*2)
print("Lista je:")
ll._print_list()

print("Lista nakon brisanja elementa s indeksom 2:")
ll.deleteNode(2)
ll._print_list()

print("Lista nakon brisanja elementa 6:")
ll.deleteNodeByValue(6)
ll._print_list()

print('Lista nakon dodavanja elementa 15')
ll._add(15)
ll._print_list()

print("Lista nakon brisanja svega...")
for i in range(ll.length-1, -1, -1):
    ll.deleteNode(i)
ll._print_list()
