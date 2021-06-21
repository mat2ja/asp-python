class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # def add(self, key, value):
    #     h = self.get_hash(key)
    #     self.arr[h] = value

    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        for idx, elem in enumerate(self.arr[h]):
            # check if same key and replace its value
            if len(elem) == 2 and elem[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        # if new key
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

    def __str__(self):
        printed = ""
        for c in self.arr:
            printed += f"{c}, "
        return printed


t = HashTable()
print(t.get_hash('march 6'))  # 9

t['march 6'] = 120
t['march 6'] = 78
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459

print(t)


# print(t['march 6'])
# print(t['march 1'])
# print("Not in table:", t['march 18'])
# print(t['dec 17'])

del t['march 6']
print(t)
