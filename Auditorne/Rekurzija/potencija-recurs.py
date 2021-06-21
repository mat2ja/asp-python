# O(logN)
def power(x, n):
    """Računa vrijednost x**n za integer n."""

    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)  # zaokružena vrijednost na integer
        result = partial * partial
        if n % 2 == 1:    # ako je neparan uključuje se posebni faktor x
            result *= x
        return result


if __name__ == '__main__':
    x = 12
    n = 7
    rez = power(x, n)
    print(rez)
