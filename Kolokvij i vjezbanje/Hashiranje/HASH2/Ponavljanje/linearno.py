class HashTabelaLinProbe:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * self.capacity
        self.count = 0

    def __str__(self):
        return str(self.slots)

    def __contains__(self, item):
        return self.search(item) != -1

    def __len__(self):
        return self.count

    def hash_function(self, key):
        # return hash(key) % self.capacity
        return 3*key % self.capacity

    def find_slot(self, key):
        slot = self.hash_function(key)
        while self.slots[slot] is not None and self.slots[slot] != key:
            slot = (slot + 1) % self.capacity
            # slot += 1
            # if slot == self.capacity:
            #     slot = 0
        return slot

    def insert(self, key):
        slot = self.find_slot(key)
        if self.slots[slot] != key:
            self.slots[slot] = key
            self.count += 1


m = HashTabelaLinProbe(11)
keys = [2341, 4234, 2839, 430, 22, 397, 3920, 4567, 2833, 44]
n = len(keys)
for i in keys:
    m.insert(i)
print(m)
