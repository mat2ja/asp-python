class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class LinkedQueue:
    """FIFO queue implementcija korištenjem SLL."""

    # -------------------------- ignježđena klasa  _Node class --------------------------
    class _Node:
        """Nejavna klasa za kreiranje jednog povezanog čvor."""
        __slots__ = '_element', '_next'         # korištenje memorije

        def __init__(self, element, next):      # inicijalizacija čvora
            self._element = element               # referenca na podatak
            self._next = next                     # referenca na next čvor

    # ------------------------------- queue methods -------------------------------
    def __init__(self):
        """Kreiranje praznog reda."""
        self._head = None
        self._tail = None
        self._size = 0                          # broj elemenata u redu

    def __len__(self):
        """Vraća broj elemenata u redu."""
        return self._size

    def __iter__(self):
        node = self._head
        while node:
            yield node
            node = node._next

    def is_empty(self):
        """Vraća True ako je red prazan."""
        return self._size == 0

    def first(self):
        """Vraća  (ali ne skidae)element na frontu reda.

        Raise Empty exception ako je prazan
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element              # front povezan s glavom liste

    def dequeue(self):
        """Skida i vraća element iz reda (FIFO).

        Raise Empty exception ako je prazan.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                     # spec. slučaj praznog reda
            self._tail = None                     # maknuta glava je bila rep
        return answer

    def enqueue(self, e):
        """Dodavanje elementa na kraj reda."""
        newest = self._Node(e, None)            # node će biti novi tail node
        if self.is_empty():
            self._head = newest                   # spec. slučaj: prethodni je prazan
        else:
            self._tail._next = newest
        self._tail = newest                     # obnova  reference na čvor tail
        self._size += 1


if __name__ == "__main__":
    ''' formiramo red'''
    red = LinkedQueue()
    red.enqueue("F")
    red.enqueue("B")
    red.enqueue("D")
    print(red.dequeue())
    print("Ispiši red:")
    for k in red:
        print(k._element)
