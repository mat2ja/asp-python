# A complete working Python program to demonstrate all
# insertion methods of linked list

# Node class
class Node:

    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertBefore(self, next_node, new_data):
        if next_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)

        node = self.head
        while node:
            if node.next == next_node:
                node.next = new_node
                new_node.next = next_node
                return
            else:
                node = node.next

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    def swapNodes(self, x, y):

        # Nothing to do if x and y are same
        if x == y:
            return

        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return

        # If x is not head of linked list
        if prevX is not None:
            prevX.next = currY
        else:  # make y the new head
            self.head = currY

        # If y is not head of linked list
        if prevY is not None:
            prevY.next = currX
        else:  # make x the new head
            self.head = currX

        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()

    llist.append(6)  # na kraj

    llist.push(7)  # na pocetak
    llist.push(1)
    llist.append(4)
    llist.printList()

    llist.insertAfter(llist.head.next, 8)

    print('Created linked list is:')
    llist.printList()

    print('Created linked list is:')
    llist.insertBefore(llist.head.next.next.next, 100)
    llist.printList()

