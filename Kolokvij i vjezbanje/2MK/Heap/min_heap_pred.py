# KLASA BINARNA HRPA (GOMILA) IMPLEMENTIRANA POMOĆU POLJA
# IMPLEMENTACIJA MIN GOMILE
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # Preslagivanje gomile prema gore
    def rearrangeUp(self, i):
        # usporeduj s parentom i pomici gore dokglegod je manji od parenta
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i //
                              2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    # Ubacivanje u gomilu
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.rearrangeUp(self.currentSize)

    # Preslagivanje gomile prema dolje
    def rearrangeDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    # dohvačanje Min vrijednosti gomile
    def getMin(self):
        return self.heapList[1]

    # određivanje indeksa najmanjeg djeteta
    def minChild(self, i):
        # u ovoj impementaciji je lijevo dijete i*2 a desno i*2+1, pa ako nema desnog, lijevo je najmanje
        if i*2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    # brisanje MIN vrijednosti
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.rearrangeDown(1)
        return retval

    # izgradnja gomile
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.rearrangeDown(i)
            i -= 1

    def __str__(self):
        return f"{self.heapList[1:]}"


BGom = BinHeap()
# BGom.buildHeap([9, 5, 6, 2, 3])
BGom.buildHeap([40, 60, 10, 20, 50, 30])
print(BGom)
# print("Ispis Min elementa")
# print(BGom.getMin())

# print("Brisanje Min elemenata")
# print(BGom.delMin())
# print(BGom.delMin())

# print(BGom.delMin())
# print(BGom.delMin())
# print(BGom.delMin())

print("Ubacivanje novih elemenata")
BGom.insert(12)
BGom.insert(7)
BGom.insert(15)

# print("Ispis Min elementa")
# print(BGom.getMin())
