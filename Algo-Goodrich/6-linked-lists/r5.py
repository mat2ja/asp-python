from circular_list import MyCircularLinkedList

# Implement a function that counts the number of nodes in a circularly
# linked list.


def countNodes(head):
    if head is None:
        return 0

    if head.next == head:
        return 1

    count = 1
    node = head
    while node.next != head:
        node = node.next
        count += 1

    return count


clist = MyCircularLinkedList()
for i in range(1, 3):
    clist.append(i)
clist.print_list()
print("Count:", countNodes(clist.head))
