'''
### Rekurzivno pretvori ugnježđenu listu u obični listu poredanih elemanta (poravnanje)

1. Inicijalizirajte varijablu na ugniježđeni popis.
2. Proslijedite popis kao argument rekurzivnoj funkciji za poravnanje popisa.
3. Ako je popis prazan, vratite ga u funkciju.
4. U suprotnom, funkcija se rekurzivno poziva s podlistama kao parametrima sve dok se cijela lista ne poravna.
5. Ispišite poravnau listu.
'''


def poravnaj(lista):
    if len(lista) == 0:
        return lista
    if isinstance(lista[0], list):
        return poravnaj(lista[0]) + poravnaj(lista[1:])
    return lista[:1] + poravnaj(lista[1:])


s1 = [[1, 2], [3, 4]]
s2 = [['x', 'y'], ['z', 'p'], ['m', ['a', 'b', 'c', ['d', 'e']]]]
print("Poravnana lista je: ", poravnaj(s1))
print("Poravnana lista je: ", poravnaj(s2))
