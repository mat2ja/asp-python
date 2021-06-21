class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stog:
    def __init__(self):
        self.head = None

    def stavi(self, value):
        node = SNode(value)
        if self.head:
            node.next = self.head
        self.head = node

    def uzmi(self):
        if self.isEmpty():
            return None
        popped = self.head
        self.head = self.head.next
        return popped.data

    def isEmpty(self):
        return True if not self.head else False


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Red:
    def __init__(self):
        self.head = None
        self.tail = None

    def stavi(self, value):
        node = Node(value)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def uzmi(self):
        if not self.head:
            return "Nothing to deqeue"

        removed = self.head
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

        if self.isEmpty():
            self.tail = None
        return removed.data

    def printQueue(self):
        if not self.head:
            print("Queue is empty")
            return

        print("Printing queue", end=": ")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def isEmpty(self):
        return True if not self.head else False

    # def promijeni(self, elem):
    #     prev = None
    #     curr = self.head
    #     while curr:
    #         if curr.data == elem:
    #             break
    #         prev = curr
    #         curr = curr.next

    #     # if element not found
    #     if curr is None:
    #         return

    #     # if found is at head
    #     if prev is None and curr.next is None:
    #         prev_value = 0
    #         next_value = 0
    #     elif prev is None:
    #         prev_value = 0
    #         next_value = curr.next.data
    #     # if found is at tail
    #     elif curr.next is None:
    #         next_value = 0
    #         prev_value = prev.data
    #     else:
    #         prev_value = prev.data
    #         next_value = curr.next.data

    #     # curr.data = prev_value + next_value
    #     curr.data = next_value - prev_value

    def promijeni(self, elem):
        curr = self.head
        while curr:
            if curr.data == elem:
                break
            curr = curr.next

        # if element not found
        if curr is None:
            return

        # if found is at head
        if curr.prev is None and curr.next is None:
            prev_value = 0
            next_value = 0
        elif curr.prev is None:
            prev_value = 0
            next_value = curr.next.data
        # if found is at tail
        elif curr.next is None:
            next_value = 0
            prev_value = curr.prev.data
        else:
            prev_value = curr.prev.data
            next_value = curr.next.data

        # curr.data = prev_value + next_value
        curr.data = next_value - prev_value


def ispis(struktura):

    head = struktura.head

    if not head:
        return "Prazno je"

    if isinstance(struktura, Stog):
        curr = head
        print("<--", end=" ")
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    elif isinstance(struktura, Red):
        tail = struktura.tail
        curr = tail
        while curr:
            print(curr.data, end=" ")
            curr = curr.prev
        print("-->", end=" ")
        print()


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S = Stog()
R = Red()
for element in L:
    R.stavi(element)

S.stavi(4)
S.stavi(5)
S.stavi(6)
S.stavi(23)
S.stavi(14)
S.stavi(9)

ispis(S)  # ispis mora biti ovakav: <-- 9 14 23 6 5 4
ispis(R)  # ispis mora biti ovakav: 10 9 8 7 6 5 4 3 2 1 -->

R.promijeni(S.uzmi())
R.promijeni(S.uzmi())
R.promijeni(S.uzmi())
R.promijeni(S.uzmi())
R.promijeni(S.uzmi())

R.uzmi()
R.uzmi()
R.uzmi()

ispis(S)  # ispis mora biti ovakav: <-- 4
ispis(R)  # ispis mora biti ovakav: 10 2 8 7


# Koja je složenost metode promijeni()?
