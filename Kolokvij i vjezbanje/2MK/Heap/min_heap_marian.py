class MinHeap():
    def __init__(self):
        self.heapList = [0]

    def build_heap(self, init_list=[]):
        if init_list:
            for element in init_list:
                self.heapList.append(element)
        last_parent_index = (len(self.heapList)-1)//2
        while last_parent_index:
            self.__bubble_down(last_parent_index)
            last_parent_index -= 1

    def __bubble_down(self, inx):
        while inx*2 <= len(self.heapList)-1:
            min_child_index = self.__min_child(inx)
            if self.heapList[inx] > self.heapList[min_child_index]:
                self.__swap(inx, min_child_index)
            inx = min_child_index

    def __min_child(self, inx):
        if inx*2+1 > len(self.heapList)-1:
            return inx*2
        else:
            if self.heapList[inx*2] < self.heapList[inx*2+1]:
                return inx*2
            else:
                return inx*2+1

    def __swap(self, inx1, inx2):
        self.heapList[inx1], self.heapList[inx2] = self.heapList[inx2], self.heapList[inx1]

    def __str__(self):
        return "{}".format(self.heapList[1:])

    def insert(self, data):
        self.heapList.append(data)
        self.build_heap()


min_heap = MinHeap()
min_heap.build_heap([40, 60, 10, 20, 50, 30])
print(min_heap)
