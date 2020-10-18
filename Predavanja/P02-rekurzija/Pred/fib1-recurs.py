import time

# eksponencijalna
def fib1_recurs(n):
    """ funkcija vraća n-ti Fibonacci broj"""
    # osnovni slučaj

    if n <= 1:
        return n
    else:
        # rekurzivni poziv
        return fib1_recurs(n - 2) + fib1_recurs(n - 1)


if __name__ == '__main__':
    start = time.perf_counter()
    print(fib1_recurs(30))
    end = time.perf_counter()
    print("Time:", "{:.8f}".format(end - start))
    print()
