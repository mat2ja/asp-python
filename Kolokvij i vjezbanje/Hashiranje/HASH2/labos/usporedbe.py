def hash_funcs(k, n=10):
    hashA = k**2 % n
    hashB = k**3 % n
    hashC = (11 * k**2) % n
    hashD = (12 * k) % n
    return (hashA, hashB, hashC, hashD)


HT = [None for i in range(10)]
HT1 = HT[:]
HT2 = HT[:]
HT3 = HT[:]
HT4 = HT[:]


for k in range(10):
    hashA, hashB, hashC, hashD = hash_funcs(k)
    HT1[hashA] = k
    HT2[hashB] = k
    HT3[hashC] = k
    HT4[hashD] = k


print(HT1)
print(HT2)
print(HT3)
print(HT4)

# najbolja je pod b)
