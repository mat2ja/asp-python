def search_key(hash_table, n, m, key):
    i = 0
    slot = hash(key, m, i)

    found = True if hash_table[slot] == key else False
    found_izbrisani = True if hash_table[slot] == -999999 else False

    if not found and not found_izbrisani:
        temp = slot
        slot += 1
        while slot < len(hash_table):
            if hash_table[slot] == key:
                found = True
                break
            elif hash_table[slot] == -999999:
                found_izbrisani = True
            slot += 1

        if not found or not found_izbrisani:
            slot = temp
            slot -= 1
            while slot >= 0:
                if hash_table[slot] == key:
                    found = True
                    break
                elif hash_table[slot] == -999999:
                    found_izbrisani = True
                    slot -= 1
