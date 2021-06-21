'''

Dovršite klasu Lista koja implementira jednostruko-vezanu listu na sljedeći način:

    Dodajte metodu "tekstualno" koja ispisuje listu kako je pokazano ispod.
    Dodajte metodu "obrisi" koja brise zadani element kako je pokazano ispod. Ta metoda
    treba brisati samo elemente na prvoj razini, ne u podlistama.
    Dodajte metodu "nadji" koja pronalazi element kako je pokazano ispod. Ova metoda
    treba tražiti elemente i u podlistama.

'''


class Element:
    def __init__(self, x):
        self.podatak = x
        self.iduci = None


class Lista:
    def __init__(self):
        self.prvi = None
        self.zadnji = None
        self.trenutni = None
        self.broj_elemenata = 0

    def resetiraj(self):
        self.trenutni = self.prvi

    def iduci(self):
        if self.trenutni is None:
            self.resetiraj()
            return None
        x = self.trenutni
        self.trenutni = x.iduci
        return x

    def dodaj(self, element):
        x = Element(element)
        if self.zadnji:
            self.zadnji.iduci = x
            self.zadnji = x
        else:
            self.prvi = x
            self.zadnji = x
            self.trenutni = self.prvi
        self.broj_elemenata += 1

    # *** ovu metodu trebaju napisati studenti
    # [5 bodova]
    def nadji(self, fn):
        curr = self.prvi
        while curr:
            if fn(curr):
                return curr.podatak
            elif isinstance(curr.podatak, Lista):
                postoji = curr.podatak.nadji(fn)
                if postoji:
                    return postoji
            curr = curr.iduci
        return None

    # *** ovu metodu trebaju napisati studenti
    # [5 bodova]
    def obrisi(self, element):
        prev = None
        curr = self.prvi

        while curr:
            if curr.podatak == element:
                if prev:
                    prev.iduci = curr.iduci
                else:
                    if self.prvi.iduci is None:
                        self.zadnji = curr.iduci
                    self.prvi = curr.iduci

            prev = curr
            curr = curr.iduci

    # *** ovu metodu trebaju napisati studenti
    # [5 bodova]

    def tekstualno(self):
        output = ""
        curr = self.prvi
        output += "<"

        while curr is not None:
            if isinstance(curr.podatak, Lista):
                output += curr.podatak.tekstualno()
            else:
                output += str(curr.podatak)
            if curr.iduci:
                output += "; "
            curr = curr.iduci
        output += ">"

        return output


x = Lista()
x.dodaj((1, 2))
print(x.tekstualno())  # ispisuje <(1, 2)>
x.obrisi((1, 2))
print(x.tekstualno())  # ispisuje <>
x.dodaj((1, 3))
print(x.tekstualno())  # ispisuje <(1, 3)>
x.dodaj((1, 4))
print(x.tekstualno())  # ispisuje <(1, 3); (1, 4)>
x.obrisi((1, 3))
print(x.tekstualno())  # ispisuje <(1, 4)>
x.obrisi((1, 4))
print(x.tekstualno())  # ispisuje <>

y = Lista()
y.dodaj('y1')
y.dodaj('y2')

z = Lista()
z.dodaj('z1')
z.dodaj('z2')
z.dodaj('z3')

y.dodaj(z)  # lista y sadrzi listu z kao element

x.dodaj(1)
x.dodaj(2)
x.dodaj(y)  # lista x sadrzi listu y kao element
x.dodaj(3)
x.dodaj(y)  # lista x sadrzi listu y kao element

# ispisuje <1; 2; <y1; y2; <z1; z2; z3>>; 3; <y1; y2; <z1; z2; z3>>>
print(x.tekstualno())

# '''
# Funkcija "nadji" prima lambda-izraz kao parametar (na primjer, lambda izraz
# lambda x: x * 2 vraća kvadrat broja)
# '''

# x je tipa Element
r = x.nadji(lambda x: x.podatak == 'z3')
print(r)  # ispisuje z3
r = x.nadji(lambda x: x.podatak == 'abc')
print(r)  # ispisuje None
