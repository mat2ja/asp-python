def hash_string(string, tablesize):
    sum = 0
    for s in string:
        sum += ord(s)

    return sum % tablesize


def add_string(string, hashtable):
    collisions = 0
    stop = False

    slot = hash_string(string, len(hashtable))
    print(f"{string} se hashira na slot: {slot}")

    while not stop:
        if hashtable[slot] is None:
            hashtable[slot] = string
            stop = True
        else:
            # uzima se kvadrat broja kolizija
            slot = (slot + collisions**2) % len(hashtable)
            print(f"Novi slot: {slot}")
            collisions += 1
        print(f"Kolizije: {collisions}")


lstring = ["Marko", "Ante", "Marija", "Petar", "Ivan",
           "Filip", "Ljubo", "Katja", "Marina", "Markov"]
l2string = ["stop", "tops", "pots", "spot"]


H = [None for i in range(20)]
# H = [None] * 20

for s in l2string:
    add_string(s, H)

print(f"Hash table:\n")
print(H)
