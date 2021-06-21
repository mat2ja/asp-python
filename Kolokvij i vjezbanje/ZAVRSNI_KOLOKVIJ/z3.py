'''

Dovršite klasu HashTablica kojom ćete implementirati jednostavnu hash-tablicu.

Metodu "hash" koja je već implementirana treba koristiti za spremanje i čitanje
ključeva i vrijednosti. Za rješavanje kolizija koristite tehniku ulančavanja
upotrebom klase Lista (jednostruko-vezana lista) iz prethodnog zadatka.

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


class HashTablica:
    def __init__(self):
        self.tablica = []
        for _ in range(31):
            # svaki element tablice je tipa Lista (iz prethodnog zadatka)
            self.tablica += [Lista()]

    def hash(self, s):
        h = 7
        for c in s:
            h = h * 31 + ord(c)  # ord(c) vraća ASCII kôd znaka c
        return h % 10  # % daje ostatak cjelobrojnog dijeljenja

    # [5 bodova]

    def postavi(self, k, v):
        '''
        Ovdje u jednostruko-vezanu listu dodati par (k, v); prije toga treba
        provjeriti postoji li već ključ k u toj listi i, ako postoji, obrisati ga.
        '''
        h = self.hash(k)
        # *** ovo ispod trebaju dovršiti studenti

        self.tablica[h].dodaj((k, v))

    # [5 bodova]

    def kljuc(self, k):
        '''
        Prvo u jednostruko-vezanoj listi naći ključ k i, ako postoji, vratiti
        par (k, v); ako ne postoji baciti iznimku sljedećim pozivom:
            raise Exception('Nepostojeći ključ')
        '''
        h = self.hash(k)
        # *** ovo ispod trebaju dovršiti studenti
        found = self.postoji(k)
        if not found:
            raise Exception('Nepostojeći ključ')

        lista = self.tablica[h]
        curr = lista.prvi
        while curr:
            if k in curr.podatak:
                return curr.podatak
            else:
                curr = curr.next

    # [5 bodova]

    def postoji(self, k):
        '''
        U jednostruko-vezanoj listi provjeriti postoji li element s ključem k.
        '''
        h = self.hash(k)
        # *** ovo ispod trebaju dovršiti studenti
        found = False

        curr = self.tablica[h].prvi
        while curr and not found:
            if k in curr.podatak:
                found = True
            else:
                curr = curr.iduci

        return found


m = HashTablica()

# postavi(k, v) postavlja vrijednost ključa k na vrijednost v
m.postavi('a', 10)
m.postavi('a', 20)

# # kljuc(k) vraća vrijednost ključa k
v = m.kljuc('a')
print('kljuc "a":', v)  # ispisuje kljuc "a": ('a', 20)

# m.postoji(k) vraća True ako ključ k postoji u mapi ili False ako ne postoji
print('postoji "a":', m.postoji('a'))  # ispisuje postoji "a": True
print('postoji "test":', m.postoji('test'))  # ispisuje postoji "test": False

# # čitanje ključa koji ne postoji, treba baciti iznimku
v = m.kljuc('b')  # iznimka!
print('v =', v)  # ne ispisuje se zbog prethodne iznimke
