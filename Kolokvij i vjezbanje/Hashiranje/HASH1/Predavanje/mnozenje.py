import math
# Hash funkcije - Metoda množenja
# A ≈ (sqrt (5) -1)/2 = 0.6180339887….
A = (math.sqrt(5)-1)/2
HashTableSize = 10000
HashTableSize = int(input("Upiši veličinu tabele : "))
print("Konstanta A:", A)
#h(k) = floor(10000*(123456*0.6180339887…mod 1))


print("Hash za polje ključeva")
lkey = [123456, 234567, 233455, 345678, 333455,
        578989, 578990, 578991, 578992, 578993, 578994]
# lkey = [200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255,
#         260, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600]
for k in range(len(lkey)):
    key = lkey[k]
    # HASH FUNKCIJA
    hk = int(HashTableSize*(key*A % 1))
    print("Ključ je:", key, " Adresa je: ", hk)
