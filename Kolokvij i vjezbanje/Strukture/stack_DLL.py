class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        if self.head:
            self.head.prev = node
            node.next = self.head
        self.head = node

    def pop(self):
        if self.isEmpty():
            return None
        elif self.head.next is None:
            popped = self.head.data
            self.head = None
            return popped
        else:
            popped = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return popped

    def isEmpty(self):
        return True if not self.head else False

    def printStack(self):
        if self.isEmpty():
            print("Stack is empty!")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def top(self):
        if self.isEmpty():
            return None
        return self.head.data

    def size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size


stog = Stack()
stog.push(1)
stog.push(2)
stog.push(3)
stog.push(4)
print("Popped:", stog.pop())
stog.printStack()
print(stog.top())
stog.pop()
stog.pop()
stog.pop()
print(stog.top())
