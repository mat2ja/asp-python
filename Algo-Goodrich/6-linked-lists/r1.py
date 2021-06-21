# Give an algorithm for finding the second-to-last node in a singly linked
# list in which the last node is indicated by a next reference of None.

from linked_list import MyLinkedList


def findSecondToLast(head):
    if head is None or head.next is None:
        return "No 2nd last element found"

    node = head
    next_node = node.next
    while next_node.next is not None:
        node = node.next
        next_node = node.next
    return node.data


ll = MyLinkedList()
for i in range(1, 10):
    ll.append(i)
ll.printList()
print("Second to last is:", findSecondToLast(ll.head))
