'''
a) Napiši funkciju def double_hash(polje_Ključ, hash_table, n, m) koja realizira postupak dvostrukog isprobavanja(h(k, i) = (h1(k) + ih2(k) % m). Ulaz u funkciju su int polje ključeva, int polje hash tabele, , n – veličina hash tabele, m – veličina hash tabele koja mora biti prost broj(m <= n).

Napomena: Funkcija treba izvršiti izračunavanje adrese za svaki ključ prema hash funkcijama koje glase h1(k) = 13k % m i h2(k) = 17 + k % m1 (veličina m1 je za 1 manja od m) i svaki puta ispitati da li je izračunata adresa u koliziji(provjeriti da li je u hash tabeli vrijednost na izračunatoj adresi jednaka 0). 
Ako nije u koliziji upisuje se vrijednost ključa u hash tabelu na izračunatu adresu(indeks polja), a ako je u koliziji ide se računati nova adresa za novu vrijednost indeksa i koja se povećala za 1.

Napomena: koristite pomoćnu varijablu kolizija koja je jednaka 0 ako nema kolizije ili 1 ako ima kolizije. Na kraju ispisati tabelu ključeva i hash tabelu.

Napisati test program za zadanu tabelu ključeva: KEY = [28, 17, 9, 22, 45, 12, 78, 58, 38, 68, 201], veličina tabele je n = 19. 
Odredite broj m(djelitelj po modulu u hash funkciji) takav da bude prvi manji broj od veličine tablice koji je prim broj).

b) Realizirajte funkciju def search_key(hash_table, n, m, key) koja će pronaći zadani ključ(key) u tablici i ispisati njegovu vrijednost i indeks tablice u kojoj se nalazi te ispisati koliko ispitivanja je napravljeno da se nađe traženi ključ(broj ispitivanja i=0 do m-1). Ako ključ nije pronađen vratiti vrijednost - 1 i ispisati da ključ nije pronađen.Voditi računa u implementaciji funkcije za pretraživanje da li je možda traženi ključ bio brisan(pogledajte zadatak c).

c) Realizirajte funkciju def delete_key(hash_table, n, m, delkey) gdje je delkey ključ koji želimo izbrisati. Napomena za brisanje ključa zbog rješavanja kolizija na toj poziciji u tablici ne smije se samo obrisati ključ nego se mora ostaviti flag(zastavica) da je tu bio neki podatak. Zato nakon brisanja ključa na to mjesto upisati broj - 999999.

d) U drajver kodu testirati sve implementacije na sljedeći način.

    1) Umetnuti zadani niz u hash tabelu i ispisati broj kolizija za svako umetanje ispisati broj kolizija i ukupan broj kolizija. Ispisati cijelu hash tabelu.

    2) Pronaći neki ključ i ispisati ga prema zadatku b). Ključ sami birate.

    3) Obrisati dva ključa(po izboru).

    4) Pronaći neki ključ po izboru i jedan od obrisanih ključeva. Ispisati sve prema zadatku b).

    5) Ispisati ponovno cijelu hash tabelu.
'''

from random import randint


def double_hash(polje_Ključeva, hash_table, n, m):

    ukupno_kolizija = 0
    for key in polje_Ključeva:
        i = 0
        kolizija = 0

        if is_full(hash_table):
            print(f"Tablica je puna. Ključ {key} nije spremljen")
            continue

        slot = hash(key, m, i)
        # print(f"-> Pokušaj spremanja ključa {key} na slot {slot}")

        while hash_table[slot] != 0:

            if hash_table[slot] != 0:
                kolizija += 1
                ukupno_kolizija += 1

            i += 1
            slot = hash(key, m, i)

            # print(f"-> Pokušaj spremanja ključa {key} na slot {slot}")

        hash_table[slot] = key
        print(f"Ključ {key} spremljen na slot {slot}")

        print(f"\tKolizije: {kolizija}") if kolizija > 0 else None

    print("\nUkupno kolizija:", ukupno_kolizija)


def is_full(hash_table):
    for key in hash_table:
        if key is 0:
            return False
    return True


def search_key(hash_table, n, m, key):
    limit = 50
    i = 0

    slot = hash(key, m, i)

    found = True if hash_table[slot] == key else False
    found_izbrisani = False
    while not found and not found_izbrisani and i < limit:
        i += 1
        slot = hash(key, m, i)

        if hash_table[slot] == key:
            found = True
        elif hash_table[slot] == -999999:
            found_izbrisani = True

    if found:
        print(f"Ključ {key} nađen na slotu {slot}")
        return True
    elif found_izbrisani:
        print(f"Ključ {key} na slotu {slot} je možda izbrisan")
        return False
    else:
        print(f"Ključ {key} nije nađen")
        return False


def delete_key(hash_table, n, m, delkey):
    found = search_key(hash_table, n, m, delkey)
    if not found:
        return

    i = 0

    slot = hash(delkey, m, i)

    while hash_table[slot] != delkey:
        i += 1
        slot = hash(delkey, m, i)

    if hash_table[slot] == delkey:
        hash_table[slot] = -999999
        print(f"Izbrisali ste ključ {delkey}")


def display_hash_table(hash_table):
    for slot in range(len(hash_table)):
        value = hash_table[slot]
        key = value if value != 0 else ""
        print(f"Slot {slot}:", key)


def hash(k, m, i):
    return (h1(k, m) + i*h2(k, m)) % m


def h1(k, m):
    return (13 * k) % m


def h2(k, m):
    m1 = m-1
    return 17 + k % m1


def is_prime(num):
    isPrime = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            isPrime = True

    return isPrime


n = 19
m = n-1
while not is_prime(m):
    m -= 1

keys = [28, 17, 9, 22, 45, 12, 78, 58, 38, 68, 201]
# keys = [randint(1, 300) for i in range(16)]
keys = [66, 167, 83, 82, 18, 47, 161, 122,
        100, 280, 219, 252, 181, 156, 61, 243]

print(f"\n{keys}\n")

HashTable = [0 for i in range(n)]

double_hash(keys, HashTable, n, m)

print("\nISPIS HASH TABELE:")
display_hash_table(HashTable)

print("\nTRAŽENJE KLJUČEVA:")
# search_key(HashTable, n, m, 9)
# search_key(HashTable, n, m, 201)
# search_key(HashTable, n, m, 17)
# search_key(HashTable, n, m, 45)
# search_key(HashTable, n, m, 3242)
# search_key(HashTable, n, m, 1)

search_key(HashTable, n, m, 66)
search_key(HashTable, n, m, 161)
search_key(HashTable, n, m, 122)
search_key(HashTable, n, m, 219)
search_key(HashTable, n, m, 86)
search_key(HashTable, n, m, 12)

print("\nBRISANJE KLJUČEVA:")
delete_key(HashTable, n, m, 122)
delete_key(HashTable, n, m, 18)
delete_key(HashTable, n, m, 1225)

print("\nISPIS HASH TABELE:")
display_hash_table(HashTable)

print("\nTRAŽENJE IZBRISANIH:")
search_key(HashTable, n, m, 122)
