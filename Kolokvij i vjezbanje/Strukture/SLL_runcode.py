from SLL import LinkedList

llist = LinkedList()

llist.prepend(99)
for i in range(1, 4):
    llist.append(i)

llist.prepend(0)

llist.display()
print("Size:", llist.size())

llist.remove(1)
llist.remove(99)

print("After removing:")
llist.display()

llist.insertAfter(0, "Matija")
llist.insertAfter(0, 3)
llist.prepend(3)

print("After inserting:")
llist.display()

print("Count of Matija:", llist.countOccurences("Matija"))
print("Count of 1000:", llist.countOccurences(1000))
print("Count of 3:", llist.countOccurences(3))

print("Count recursive of 3:", llist.countOccurencesRecursive(llist.head, 3))
print("Count recursive of Jozo:",
      llist.countOccurencesRecursive(llist.head, "Jozo"))

llist.removeDuplicates()
print("After removing duplicates")
llist.display()
print("Count of 3:", llist.countOccurences(3))

# llist.removeFirst()
llist.removeFirst()
llist.removeLast()
print("After removing first and last")
llist.display()
print("Size:", llist.size())
print("Size Recursive:", llist.sizeRecursive(llist.head))

llist.append("Lucija")
llist.append("Marta")
llist.append("Marian")
llist.append("Marin")
llist.remove(2)
print("After adding more names")


print("First n:", llist.firstN(4))
print("Last n:", llist.lastN())

# print("After clearing")
# llist.clear()
# llist.display()

print("Printing list:")
llist.display()
llist.swapNodes("Lucija", "Marin")

print("After swaping:")
llist.display()

print("After inserting:")
llist.insertAfter("Lucija", "Roso")
llist.display()

llist.append("Matija")
llist.prepend("Matija")
llist.display()

llist.removeDuplicates()
llist.display()

llist.remove("Marta")
llist.removeNode(llist.head.next)
llist.display()
