

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.rearrangeDown(i)
            i -= 1

    def insert(self, k):
        self.heapList.append(k)
        self.size += 1
        self.rearrangeUp(self.size)

    def rearrangeUp(self, i):
        # while has parent
        while i // 2 > 0:
            parentIdx = i // 2
            if self.heapList[i] < self.heapList[parentIdx]:
                self.heapList[parentIdx], self.heapList[i] = self.heapList[i], self.heapList[parentIdx]
            i //= 2

    def rearrangeDown(self, i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def getMin(self):
        return self.heapList[1]

    # određivanje indeksa najmanjeg djeteta
    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    # brisanje MIN vrijednosti
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size - 1
        self.heapList.pop()
        self.rearrangeDown(1)
        return retval


BGom = BinHeap()
BGom.buildHeap([9, 5, 6, 2, 3])
print("Ispis Min elementa")
print(BGom.getMin())

print("Brisanje Min elemenata")
print(BGom.delMin())
print(BGom.delMin())
print(BGom.delMin())
print(BGom.delMin())
print(BGom.delMin())

print("Ubacivanje novih elemenata")
BGom.insert(12)
BGom.insert(7)
BGom.insert(15)

print("Ispis Min elementa")
print(BGom.getMin())
