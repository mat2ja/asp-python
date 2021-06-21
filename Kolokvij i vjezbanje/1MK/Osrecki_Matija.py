# Matija Osrečki

class Element:
    def __init__(self, x):
        self.podatak = x
        self.iduci = None


class Lista:
    def __init__(self):
        self.prvi = None
        self.zadnji = None
        self.trenutni = None

    def dodaj(self, element):
        x = Element(element)
        if self.zadnji:
            self.zadnji.iduci = x
            self.zadnji = x
        else:
            self.prvi = x
            self.zadnji = x
            self.trenutni = self.prvi

    def iduci(self):
        if self.trenutni is None:
            self.resetiraj()
            return None
        x = self.trenutni
        self.trenutni = x.iduci
        return x

    def resetiraj(self):
        self.trenutni = self.prvi

    def tekstualno(self):
        if not self.prvi:
            return ""

        output = ""
        curr = self.prvi
        output += "<"
        while curr:
            if isinstance(curr.podatak, Lista):
                output += curr.podatak.tekstualno()
            else:
                output += str(curr.podatak)
                
            if curr.iduci is not None:
                output += "; "
            curr = curr.iduci
        output += ">"

        return output


x = Lista()

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
