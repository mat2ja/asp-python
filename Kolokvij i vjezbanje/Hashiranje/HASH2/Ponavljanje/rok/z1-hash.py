'''
Napisati funkciju za hashiranje stringova omena. Zadana he tablica imena veličine n = 11, Str_Ime = [„Lana“, „Leo“, „Marija“, „Mario“, „Lino“, „Marko“, „Ana“, „Martina“, „Ljubica“, „Katarina“, „Marta“].

Napisati funkciju def String_Hash(String m) gdje je m veličina Hash tabele.  Napisati test program u kojem se testira funkcija koja vraća Hash adresu(varijabla value) na koju u tabelu Hash_Ime treba upisati pripadni ključ. Ispisati broj kolizija. Komentari da li je ova hash funkcija dobra i objasniti ako jest odnosno ako nije zašto?

Hash funkcija glasu: value = (string[i] + 7 * value) % m, m = 11
'''

# hash funckija nije dobra jer nema nikakve metode pokusaja spremanja vrijednosti na neki drugi slot ukoliko je slot dobiven hashiranjem vec zauzet. Trebalo bi to rijesili ulancavanjem ili nekim od linearnog, kvadratnog ili dvostrikog isprobavanja


n = 11
HashTable = [None for i in range(n)]
imena = ["Lana", "Leo", "Marija", "Mario", "Lino", "Marko",
         "Ana", "Martina", "Ljubica", "Katarina", "Marta"]


def string_hash(string, m):
    value = 0
    for i in range(len(string)):
        value = (ord(string[i]) + 7 * value) % m

    return value


kolizija = 0
for ime in imena:
    slot = string_hash(ime, n)
    if HashTable[slot] != None:
        kolizija += 1
        print(f"Došlo je do kolizije na slotu {slot}")
    else:
        HashTable[slot] = ime
        print(f"{ime} spremljeno na slot {slot}")

print(f"\nUkupno kolizija {kolizija}")

print("\nHASH TABLICA")
for index, ime in enumerate(HashTable):
    ime = ime if ime is not None else ""
    print(f"{index}: {ime}")



