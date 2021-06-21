from random import randint


class Table():
    def __init__(self, size):
        self.size = size
        self.table = [None for i in range(size)]
        self.ukupno_kolizija = 0

    def dodaj(self, k):
        if self.je_puna():
            print("Tablica je puna")
            return

        i = 0
        limit = 50
        kolizija = 0
        slot = self.hash_func_kvadratno(k, i)

        while self.table[slot] is not None and i < limit:
            kolizija += 1
            i = (i+1) % self.size
            slot = self.hash_func_kvadratno(k, i)

        if i == limit:
            print(f"Ključ {k} nije dodan")
        else:
            self.ukupno_kolizija += kolizija
            self.table[slot] = k
            print(f"Ključ {k} dodan na slot {slot}", end=" ")
            print(f"\tKolizije: {kolizija}")

    def pronadji(self, k):
        i = 0
        slot = self.hash_func_kvadratno(k, i)
        limit = 50
        found = False

        if self.table[slot] == k:
            found = True
        else:
            while i < limit and not found:
                i += 1
                slot = self.hash_func_kvadratno(k, i)
                if self.table[slot] == k:
                    found = True

        if found:
            print(f"Ključ {k} nađen na slotu {slot}")
            return slot
        else:
            print(f"Ključ {k} nije pronađen")
            return -1

    def hash_func_kvadratno(self, k, i):
        return (k + 11 + i*2) % self.size

    def display(self):
        print(f"\nHASH TABLE:")
        for slot, key in enumerate(self.table):
            key = key or ""
            print(f"Slot {slot}: {key}")

    def je_puna(self):
        for key in self.table:
            if key is None:
                return False
        return True

    def __len__(self):
        return self.size


n = 17
# keys = [randint(1, 50) for i in range(14)]
keys = [38, 40, 52, 26, 14, 22, 7, 19, 35, 2]

print(keys)
HashTable = Table(n)

[HashTable.dodaj(key) for key in keys]
HashTable.display()

print(f"\nUkupno kolizija: {HashTable.ukupno_kolizija}")

print("\nTRAŽENJE")
HashTable.pronadji(40)
HashTable.pronadji(2)
HashTable.pronadji(250)
