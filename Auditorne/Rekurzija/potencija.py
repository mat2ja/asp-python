# O(n)
def power(x, n):
    """Računa vrijednost x**n za integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


if __name__ == '__main__':
    x = 15
    n = 4
    rez = power(x, n)
    print(rez)
