class MaxHeap():
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def rearrangeDown(self, i):
        # while it has atleast 1 child
        while i*2 <= self.size:
            # find bigger child
            max_child = self.maxChild(i)
            # if its bigger than current (parent), swap
            if self.heapList[max_child] > self.heapList[i]:
                self.swap(i, max_child)
            # now current node is index of bigger child, we repeat for its children
            i = max_child

    def rearrangeUp(self, i):
        # while it has parent
        while i//2 > 0:
            if self.heapList[i] > self.heapList[i//2]:
                self.swap(i, i//2)
            i //= 2

    def maxChild(self, i):
        left = i*2
        right = i*2+1
        if right > self.size:
            return left
        else:
            if max(self.heapList[left], self.heapList[right]) == self.heapList[left]:
                return left
            else:
                return right

    def swap(self, a, b):
        self.heapList[a], self.heapList[b] = self.heapList[b], self.heapList[a]

    def build(self, arr):
        i = len(arr)//2
        self.size = len(arr)
        self.heapList = [0] + arr
        while i > 0:
            self.rearrangeDown(i)
            i -= 1

    def insert(self, value):
        self.heapList.append(value)
        self.size += 1
        self.rearrangeUp(self.size)

    def __str__(self):
        return f"{self.heapList[1:]}"


MH = MaxHeap()
MH.build([40, 60, 10, 20, 50, 30])
print(MH)

MH.insert(15)
MH.insert(90)
print(MH)
