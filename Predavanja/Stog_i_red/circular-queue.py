# Klasa cirkularni red
class CircularQueue:

  # konstruktor klase
  # zadaje se maksimalna veličina reda

  def __init__(self, maxSize):
    self.queue = list()
    # korisnik unosi maxSize
    self.maxSize = maxSize
    # prazan red head i tail su jednaki 0
    self.head = 0
    self.tail = 0

  # dodavanje elementa u red
  def enqueue(self, data):
    # ako je pun
    if self.size() == (self.maxSize - 1):
      return("Red je pun!")
    else:
      # dodaj element u red
      self.queue.append(data)
      # povečaj tail pokazivać
      # djelenje modulo s maxSize
      self.tail = (self.tail+1) % self.maxSize
      return True

  # skidanje elementa iz reda
  def dequeue(self):
    # ako je prazan
    if self.size() == 0:
       return("Red je prazan!")
    else:
      # dohvati podatak
      data = self.queue[self.head]
      # povečaj pokazivanja glave
      self.head = (self.head+1) % self.maxSize
      return data

  # traženje veličine reda
  def size(self):
    # ako indeks repa veći od indeksa glave
    if self.tail >= self.head:
      qSize = self.tail - self.head
    # u protivnom
    else:
      qSize = self.maxSize - (self.head - self.tail)
    # vraća veličinu reda
    return qSize


# driver program
if __name__ == "__main__":

    # unesi veličinu reda 9
    size = input("Unesi veličinu cirkularnog reda: ")
    # instanciranje praznog reda veličine size
    q = CircularQueue(int(size))

    # dodavanje i skidanje za cirkularni red
    print(" Dodavanje u red")
    print(q.enqueue(10))
    print(q.enqueue(20))
    print(q.enqueue(30))
    print(q.enqueue(40))
    print(q.enqueue(50))
    print(q.enqueue('Jabuka'))
    print(q.enqueue(70))
    print(q.enqueue(80))
    print(q.enqueue(90))
    print("ispiši pokazivanje head i tail kad je red pun ")
    print(q.head, q.tail)
    print("Ispiši veličinu reda:")
    print(q.size())
    print(" Skidanje s reda")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("ispiši pokazivanje head i tail kad je red prazan ")
    print(q.head, q.tail)
    print("Ispiši veličinu reda:")
    print(q.size())
