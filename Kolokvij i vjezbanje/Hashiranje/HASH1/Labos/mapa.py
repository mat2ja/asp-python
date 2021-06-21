# 4. Implementirajte jednostavnu hash-tabelu klasom Mapa kod koje ključ može biti samo
# string i koja se upotrebljava na sljedeći način:

SIZE = 10


class NepostojeciKljuc():
    pass


class Mapa():
    def __init__(self):
        self.lista = [[] for i in range(SIZE)]

    def postavi(self, k, v):
        h = self.hashiraj(k)
        self.lista[h].append(v)

    def kljuc(self, k):
        h = self.hashiraj(k)
        if not self.postoji(k):
            raise Exception("Nepostojeći ključ")

        return " ".join([str(v) for v in self.lista[h]])

    def postoji(self, k):
        h = self.hashiraj(k)
        return len(self.lista[h]) >= 1

    def hashiraj(self, s):
        h = 7
        for c in s:
            h = h*31 + ord(c)
        return h % SIZE

    def __str__(self):
        printed = ""
        for l in self.lista:
            printed += " ".join([str(v) for v in l]) if len(l) >= 1 else "-"
            printed += "\n"
        return printed[:-1]


m = Mapa()

m.postavi("a", 10)
m.postavi("a", 20)
m.postavi("c", 36)
m.postavi("d", 4)
m.postavi("g", 203)

print(m.kljuc("a"))
# print(m.kljuc("b"))
print(m.kljuc("d"))

print("Mapa:")
print(m)

print(m.kljuc("g"))
print(m.postoji("a"))
print(m.postoji("test"))
