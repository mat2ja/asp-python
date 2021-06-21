# Describe in detail how to swap two nodes x and y (and not just their contents) in a singly linked list L given references only to x and y. Repeat
# this exercise for the case when L is a doubly linked list. Which algorithm takes more time?


from linked_list import MyLinkedList


def swapNodes(head, x, y):
    if x == y:
        return

    prevX = None
    currentX = head
    while currentX:
        if currentX.data == x:
            break
        else:
            prevX = currentX
            currentX = currentX.next

    prevY = None
    currentY = head
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
        head = currentY

    if prevY:
        prevY.next = currentX
    else:
        head = currentX

    currentX.next, currentY.next = currentY.next, currentX.next

    return head


llist = MyLinkedList()
for i in range(1, 5):
    llist.append(i)
llist.printList()

# llist.swapNodes( 1, 3)
swapNodes(llist.head, 1, 3)
print("Poslje zamjene")
llist.printList()
# ne radi za zamjenu prvog elementa ako je iznad klase, jer nemrem promjenit head value 😭
