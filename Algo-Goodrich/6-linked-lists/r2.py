# Describe a good algorithm for concatenating two singly linked lists L and
# M, given only references to the first node of each list, into a single list L′
# that contains all the nodes of L followed by all the nodes of M.

from linked_list import MyLinkedList
# from r1 import LinkedList


def concatenate_lists(head_one, head_two):
    new_list = MyLinkedList()

    if head_one is not None:
        node_one = head_one
        while node_one:
            new_list.append(node_one.data)
            node_one = node_one.next

    if head_two is not None:
        node_two = head_two
        while node_two:
            new_list.append(node_two.data)
            node_two = node_two.next

    return new_list


llist1 = MyLinkedList()
for i in range(1, 6):
    llist1.append(i)

llist2 = MyLinkedList()
for i in range(10, 15):
    llist2.append(i)

concatedList = concatenate_lists(llist1.head, llist2.head)
concatedList.printList()
