from SLL import LinkedList


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.llist = LinkedList()

    # dodaje na kraj
    def enqueue(self, value):
        self.llist.append(value)
        self._updateEnds()

    # miče s početka
    def dequeue(self):
        if not self.head:
            return "Nothing to dequeue"
        removed = self.llist.head
        self.llist.removeNode(removed)
        self._updateEnds()
        return removed.data

    def display(self):
        self.llist.display()

    def size(self):
        return self.llist.size()

    def first(self):
        if not self.head:
            return "Queue is empty"
        return self.head.data

    def isEmpty(self):
        return True if not self.head else False

    def _updateEnds(self):
        self.head = self.llist.head
        self.tail = self.llist.tail


q = LinkedQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.head.data)
print(q.tail.data)
q.display()
print("Dequed:", q.dequeue())
print("Dequed:", q.dequeue())
print("First:", q.first())
q.display()
print("Dequed:", q.dequeue())
print("Dequed:", q.dequeue())
print("Dequed:", q.dequeue())
print("Dequed:", q.dequeue())
q.display()
q.enqueue(25)
q.display()
