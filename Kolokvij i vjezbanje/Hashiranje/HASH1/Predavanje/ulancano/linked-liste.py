class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


SIZE = 10


class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head or new_node.data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.data < new_node.data:
                curr = curr.next

            new_node.next = curr.next
            curr.next = new_node


def hash_f(num):
    # skaliraj vrij na 0-9, metoda dijelenja
    return num % (SIZE-1)


def hash_f2(num, maximum):
    # skaliraj vrij na 0-9, metoda mnozenja
    return int((num * 1.0 / maximum) * (SIZE-1))


def address_calculation(arr):

    linked_lists = [LinkedList() for i in range(SIZE)]

    for val in arr:
        address = hash_f(val)
        linked_lists[address].insert(val)

    print_hashtable(linked_lists)


# hash table je sortirana
def address_calculation2(arr):

    linked_lists = [LinkedList() for i in range(SIZE)]

    for val in arr:
        address = hash_f2(val, max(arr))
        linked_lists[address].insert(val)

    print_hashtable(linked_lists)

    # Pridruži sortirane vrijednosti polju
    index = 0
    for i in range(SIZE):
        current = linked_lists[i].head

        while current:
            arr[index] = current.data
            index += 1
            current = current.next


def print_hashtable(linked_lists):

    for i in range(SIZE):
        curr = linked_lists[i].head
        print(f"Lista s ADRESOM {i}", end=": ")

        print("KLJUČEVI", end=" ")
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()


arr = [29, 23, 14, 5, 15, 10, 3, 18, 1, 16, 19, 36, 46]

print("Ulazno polje: " + " ".join([str(x) for x in arr]))

address_calculation(arr)

print("\n")

address_calculation2(arr)
# Ispis sortiranog polja
print("\nSortirano polje: " + " ".join([str(x) for x in arr]))
