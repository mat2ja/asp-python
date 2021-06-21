class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = Node(value)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if not self.head:
            return "Nothing to deqeue"

        removed = self.head
        self.head = self.head.next
        if self.isEmpty():
            self.tail = None
        return removed.data

    def printQueue(self):
        if not self.head:
            print("Queue is empty")
            return

        print("Printing queue", end=": ")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def first(self):
        if not self.head:
            return "Queue is empty"
        return self.head.data

    def isEmpty(self):
        return True if not self.head else False

    def size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size


q = LinkedQueue()
for i in range(1, 6):
    q.enqueue(i)
    pass
q.printQueue()
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())
q.enqueue(1000)
q.printQueue()
print(q.size())
print(q.first())
print(q.isEmpty())
