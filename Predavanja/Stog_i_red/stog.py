class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass


class LinkedStack:
  """LIFO Stog (Stack) implementacija korištenjem SLL."""

#-------------------------- ugnježđena klasa _Node class --------------------------
  class _Node:
    """Nejavna klasa za kreiranje jednog povezanog čvor."""
    __slots__ = '_element', '_next'         # korištenje memorije

    def __init__(self, element, next):      # inicijalizacija čvora
      self._element = element               # referenca na podatak
      self._next = next                     # referenca na next čvor

  #------------------------------- stack methods -------------------------------
  def __init__(self):
    """Kreiranje praznog stoga"""
    self._head = None                       # referenca na čvor galav
    self._size = 0                          # broj elemenata na stogu
  def __len__(self):
    """metoda vraća broj elemenata na stogu"""
    return self._size

  def __iter__(self):
    node = self._head
    while node:
      yield node
      node =node._next


  def is_empty(self):
    """Vraća True ako je stog prazan"""
    return self._size == 0

  def push(self, e):
    """Dodaje element e na vrh stoga."""
    self._head = self._Node(e, self._head)  # kreira i povezuje novi čvor
    self._size += 1

  def top(self):
    """Vraća (ali ga ne skida) element na vrhu stoga

    Raise Empty exception ako je stog prazan
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._head._element              # top of stack is at head of list

  def pop(self):
    """Skida element koji je na vrhu stoga( LIFO).

    Raise Empty exception ako je stog prazan.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    answer = self._head._element
    self._head = self._head._next           # premoščivanje glave na sljedećeg
    self._size -= 1
    return answer
  def len1(self):
    return len()
  
''' DRIVER - TESTIRANJE STOGA '''
if __name__ == "__main__":
  ''' formiramo stog korištenjem klase LinkedStack '''
  stack = LinkedStack()
  stack.push("A")
  stack.push("V")
  stack.push("B")
  stack.push("Z")
  print("Tko je na vrhu")
  print(stack.top())
  stack.push("V")
  print("Tko je na vrhu")  
  print(stack.top())
  print("skinuto s vrha")
  print(stack.pop())
  print("Tko je na vrhu") 
  print(stack.top())

  for k in stack:
   print(k._element, end = " ")
