from node import MyNode as Node


class MyLinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def insertAfter(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertBefore(self, next_node, data):
        if next_node is None:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        node = self.head
        while node:
            if node.next == next_node:
                node.next = new_node
                new_node.next = next_node
                return
            else:
                node = node.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # def findSecondToLast(self):
    #     if self.head is None or self.head.next is None:
    #         return "No 2nd last element found"

    #     node = self.head
    #     next_node = node.next
    #     while next_node.next is not None:
    #         node = node.next
    #         next_node = node.next
    #     return node.data

    # def countNodes(self):
    #     counter = 0
    #     if self.head is not None:
    #         node = self.head
    #         while node:
    #             counter += 1
    #             node = node.next
    #     return counter

    def swapNodes(self, x, y):
        if x == y:
            return

        prevX = None
        currentX = self.head
        while currentX:
            if currentX.data == x:
                break
            else:
                prevX = currentX
                currentX = currentX.next

        prevY = None
        currentY = self.head
        while currentY:
            if currentY.data == y:
                break
            else:
                prevY = currentY
                currentY = currentY.next

        if not currentY or not currentY:
            return

        if prevX:
            prevX.next = currentY
        else:
            self.head = currentY

        if prevY:
            prevY.next = currentX
        else:
            self.head = currentX

        currentX.next, currentY.next = currentY.next, currentX.next
