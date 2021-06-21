# Describe a recursive algorithm that counts the number of nodes in a singly
# linked list.

from linked_list import MyLinkedList


def countNodes(head):
    counter = 0
    if head is not None:
        node = head
        while node:
            counter += 1
            node = node.next
    return counter


def countNodesRecursive(node):
    if node is None:
        return 0
    return 1 + countNodes(node.next)


llist = MyLinkedList()
for i in range(1, 2):
    llist.append(i)
llist.printList()
print("Node count:", countNodes(llist.head))
print("Node count (Recursive):", countNodesRecursive(llist.head))
