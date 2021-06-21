SIZE = 10


def hash_f(num):
    # skaliraj vrij na 0-9
    return num % (SIZE-1)


def address_calculation(arr):

    lists = [[] for i in range(SIZE)]

    for val in arr:
        address = hash_f(val)
        lists[address].append(val)

    print_hashtable(lists)


def print_hashtable(lists):

    for i in range(SIZE):
        print(f"Lista s ADRESOM {i}", end=": ")

        print("KLJUČEVI", end=" ")
        print(" ".join([str(x) for x in lists[i]]))


arr = [29, 23, 14, 5, 15, 10, 3, 18, 1, 16, 19, 36, 46]

print("Ulazno polje: " + " ".join([str(x) for x in arr]))

address_calculation(arr)
