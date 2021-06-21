from random import randint


class Skup():
    def __init__(self):
        self.SIZE = 8
        self.table = [None for i in range(self.SIZE)]

    def jePuna(self):
        if None in self.table:
            return False
        return True

    def dodaj(self, element):

        if self.jePuna():
            print("Tablica je puna")
            return

        h = self.hashiraj(element)

        if self.table[h] == None:
            self.table[h] = element
            print(f"Dodan je {element} na poziciju {h}")

        else:
            print(f"Doslo je do kolizije na poziciji {h}")
            pos = h
            while self.table[pos] != None:
                pos += 1
                if pos >= self.SIZE:
                    pos = 0

            self.table[pos] = element
            print(f"Dodan je {element} na poziciju {pos}")

    def hashiraj(self, element):
        a = randint(1, 100)
        b = randint(0, 100)

        return (a*element + b) % self.SIZE

    def prikazi(self):
        print(self.table)

    def clan(self, element):
        h = self.hashiraj(element)
        naden = False

        if self.table[h] == element:
            naden = True
        else:
            poz = h
            while not naden:
                poz += 1
                if poz >= self.SIZE:
                    break
                if self.table[poz] == element:
                    naden = True

            poz = h
            while not naden:
                poz -= 1
                if poz < 0:
                    break
                if self.table[poz] == element:
                    naden = True

        return naden


T = Skup()
T.dodaj(2)
T.dodaj(4)
T.dodaj(12)
T.dodaj(11)
T.dodaj(15)
T.dodaj(9)
T.dodaj(18)
T.dodaj(49)
T.dodaj(6)
T.dodaj(69)

print(T.clan(2))
print(T.clan(4))
print(T.clan(12))
print(T.clan(11))
print(T.clan(15))
print(T.clan(9))
print(T.clan(18))
print(T.clan(49))
print(T.clan(6))
print(T.clan(69))

print(T.clan(79))
print(T.clan(98))
print(T.clan(99))


T.prikazi()
