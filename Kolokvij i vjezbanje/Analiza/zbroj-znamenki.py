# Napisati funkciju koja računa zbroj znamenki zadanog prirodnog broja N. Kolika je složenost funkcije?
# Testirati rješenje tako da napišete driver kod koji poziva funkciju zbrojiZnamanke() uz zadani broj.
# Npr.za broj 3456 treba se rezultat 18.

def zbroji_znamenke(broj):
    suma = 0
    while broj > 0:
        suma += broj % 10
        broj //= 10
    return suma


def zbroji_znamenke2(broj):
    suma = 0
    while broj:
        (broj, ostatak) = divmod(broj, 10)
        suma += ostatak
    return suma


def zbroji_znamenke3(broj):
    return broj if broj < 10 else broj % 10 + zbroji_znamenke(broj // 10)


def zbroji_znamenke4(broj):
    suma = 0
    for char in str(broj):
        suma += int(char)
    return suma


print(zbroji_znamenke(3456))  # 18
print(zbroji_znamenke2(3456))  # 18
print(zbroji_znamenke3(3456))  # 18
print(zbroji_znamenke4(3456))  # 18
