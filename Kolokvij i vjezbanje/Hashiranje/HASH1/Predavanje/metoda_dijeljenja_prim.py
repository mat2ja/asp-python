import random
random.seed(a=23489765, version=2)
# h(k) = k mod  m
 
m = 101  # prim broj
# Za tablicu veličine N = 102 stavljamo prvi manji broj koji je prim broj. npr. m = 101

m = int(input("Upiši veličinu tablice. Veličina tablice mora biti prim broj. : "))

print("Polje ključeva")
# MOŽETE ZADAVATI RAZLIČITA POLJA KLJUČEVA. MOGU SE GENERIRATI I RANDOM
#lkey = [123456, 234567,233455, 345678,333455,578989,578990,578991,578992,578993,578994]
#lkey = [200,205,210,215,220,225,230,235,240,245,250,255,260,550,555,560,565,570,575,580,585,590,595,600]
lkey = []
# POLJE KLJUČEVA MOŽE BITI RANDOM ILI U OPSEGU NPR. OD 200 DO 600 S KORAKOM 5
# UMJESTO OVIH KLJUČEVA MOŽETE KORISTITI GORE ZADANE LISTE

for j in range(200, 400, 15):
    # lkey.append(random.randint(200,600))
    lkey.append(j)
for k in range(len(lkey)):
    key = lkey[k]
    # HASH FUNKCIJA
    hk = key % m
    print("Ključ je:", key, " Adresa je: ", hk)

print("\nPoboljšana hash funkcija")
# h(k) = (a*k + b) mod m, a i b su random brojevi a > 1 i a < m, 0 < b < m
a = random.randint(1, m)
b = random.randint(0, m)
for k in range(len(lkey)):
    key = lkey[k]
    hk = (a*key + b) % m
    print("Ključ je:", key, " Adresa je: ", hk)
