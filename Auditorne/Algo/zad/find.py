def find(S, item):
    """Vraća indeks j takav da je  S[j] == item, ili False ako takav element ne postoji."""
    for i in range(len(S)):
        if S[i] == item:
            return i
    return False


def find2(S, item):
    """Vraća indeks j takav da je  S[j] == item, ili False ako takav element ne postoji."""
    itemIndex = S.index(item) if item in S else False
    return itemIndex


def find3(S, item):
    """Vraća indeks j takav da je  S[j] == item, ili False ako takav element ne postoji."""
    itemIndex = S.index(item) if item in S else False
    try:
        return S.index(item)
    except ValueError:
        return False


if __name__ == '__main__':
    lst = [3, 5, 7, 8, 1, 2, 19, 8, 45, 7]
    print('find:', find(lst, 10))
    print('find2:', find2(lst, 10))
    print('find3:', find3(lst, 10))
