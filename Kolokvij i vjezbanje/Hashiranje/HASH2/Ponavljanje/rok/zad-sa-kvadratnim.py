

def hashiraj(k, i, m):
    return (k + 7 + i**2) % m


def dodaj(table, k, m):
    i = 0
    slot = hashiraj(k, i, m)
    print(f"\tTry {k} on slot {slot}")

    while table[slot] is not None:
        i = (i+1) % m
        slot = hashiraj(k, i, m)
        print(f"Kolizija na slotu {slot}")
        print(f"\tTry {k} on slot {slot}")

    if table[slot] is None:
        table[slot] = key
        print(f"Key {key} added to slot {slot}")


def display_table(table):
    print("\nHash table:")
    for slot, key in enumerate(table):
        print(f"Slot {slot}: {key}")


arr = [6, 11, 22, 4, 29, 30, 45, 62, 78]
m = 9

HashTable = [None for i in range(m)]


for key in arr:
    dodaj(HashTable, key, m)

display_table(HashTable)


'''
0: 11
1: 29
2: 22
3: 4
4: 6
5: 39
6: 62
7: 45
8: 78
'''
