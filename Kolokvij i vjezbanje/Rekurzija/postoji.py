# 4. Napišite funkciju postoji koja pronalazi zadani element u listi koja može sadržavati druge
# liste i vraća True ako taj element postoji, u suprotnom vraća False.

def postoji(trazeni, lista):
    if not lista:
        return False

    for elem in lista:
        if elem == trazeni:
            return True
        if isinstance(elem, list) and postoji(trazeni, elem):
            return True
    return False


A = ['a', [['b', 'c'], 'd', ['e']], 'f']
print(postoji('a', A))
print(postoji('c', A))
print(postoji('d', A))
print(postoji('e', A))
print(postoji('w', A))
