import random
import math

random.seed(a=23489765, version=2)

lkey = [123456, 234567, 233455, 345678, 333455,
        578989, 578990, 578991, 578992, 578993, 578994]
lkey = [200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255,
        260, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600]

lkey = [random.randint(0, 1000) for i in range(25)]


N = 50
# N = int(input("Upiši veličinu tabele N: "))

p = 59  # prim broj
# p = int(input("Upiši prim broj p koji mora biti veći od veličine tabele N : "))

A = (math.sqrt(5)-1)/2

print("\nPoboljšana hash funkcija")
# h(k) = ((a*k + b) mod p) mod N

a = random.randint(1, p-1)
b = random.randint(0, p-1)


H = [None for i in range(N)]

for key in lkey:
    hk = ((a*key + b) % p) % N
    # hk = int(N*(key*A % 1)) # mnozenje

    print("Ključ je:", key, " Adresa je: ", hk)

    kolizija = 0
    if H[hk]:
        kolizija += 1

    H[hk] = key
    if kolizija > 0:
        print("\tBroj kolizija:", kolizija)
