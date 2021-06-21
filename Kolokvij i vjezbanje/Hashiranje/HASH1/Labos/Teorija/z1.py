'''
1. Neka je zadan niz ključeva 14, 27, 72, 18, 20, 31, 19, 15, 25, 92, hash funkcija h(k) = k mod 5 i veličina tabele 5 (s indeksima 0..4), gdje se kolizije rješavaju ulančavanjem u jednostruko-vezanu listu (linearno pretraživanje) u koju se novi elementi dodaju na kraj
liste i u kojoj se elementi pretražuju po redu, počevši od onog koji je dodan prvi.

a) Koliko ključeva će biti ispitano da bi našli vrijednost ključa 19 ako su prethodno
    svi ovi ključevi dodani po redu (s lijeva na desno)?___7__ (Ovdje pretpostavite da
    se za ključeve koji nisu u koliziji vrijednost ključa ne ispituje).

b) Ako je svaki ključ dvoznamenkasti broj i hash funkcija je definirana kao:
    return len(str(k))
    kolika će biti vremenska složenost pretraživanja? _____________ (Funkcija str(x)
    vraća broj x u obliku stringa).
'''

kljucevi = [14, 27, 72, 18, 20, 31, 19, 15, 25, 92]
#           4    2   2   3   0   1   4   0   0   2


def hashiraj(broj):
    return broj % 5
