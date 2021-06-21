def double_hash(k, i, m, m1):
    return (h1(k, m) + i*h2(k, m1)) % m


def h1(k, m):
    return (k * 5) % m


def h2(k, m1):
    return 3 + (k % m1)


def dodaj(table, key, m, m1, ukupno_kolizija):
    i = 1
    limit = 30
    kolizija = 0
    slot = double_hash(key, i, m, m1)

    while table[slot] is not None:
        kolizija += 1
        limit -= 1
        if limit == 0:
            return
        i = (i + 1) % m
        slot = double_hash(key, i, m, m1)

    table[slot] = key
    print(f"{key} dodan na slot {slot}")

    if kolizija > 0:
        print(f"Za kljuc {key} -> {kolizija} kolizija")

    ukupno_kolizija += kolizija


m = 3
m1 = 7
arr = [15, 39, 77, 12, 48]

TABLE = [None for i in range(m)]

ukupno_kolizija = 0
for value in arr:
    dodaj(TABLE, value, m, m1, ukupno_kolizija)

print("\nTABLE")
for i, key in enumerate(TABLE):
    print(f"Slot {i}: {key}")
