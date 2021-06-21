"""
Promijenite jedan red u funkciji main tako da funkcija f 
pronađe element 10 i vrati njegov indeks.
-------------

"""


def f(p, donji, gornji, e):
    if gornji >= donji:
        srednji = (gornji + donji) // 2
        if p[srednji] == e:
            return srednji
        elif p[srednji] > e:
            return f(p, donji, srednji - 1, e)
        else:
            return f(p, srednji + 1, gornji, e)

    else:
        return -1


def main(niz):
    result = f(sorted(niz), 0, len(niz)-1, 10)
    print(result)


main([7, 2, 4, 10, 1, 18, 3, 8, 15, 3])
