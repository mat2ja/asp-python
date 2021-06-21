class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node

    def pop(self):
        if self.isEmpty():
            return None
        popped = self.head.data
        self.head = self.head.next
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


# stog = Stack()
# stog.push(1)
# stog.push(2)
# stog.push(3)
# stog.push(4)
# print("Popped:", stog.pop())
# stog.printStack()
