import time

# O(n)
def fib2_recurs(n):
    """ funkcija vraća Fibonacci brojeve, F(n) i F(n-1)"""

    # osnovni slučaj
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fib2_recurs(n - 1)
        return (a+b, a)


if __name__ == '__main__':
    start = time.perf_counter()
    print(fib2_recurs(5))
    end = time.perf_counter()
    print("Time:", "{:.8f}".format(end - start))
    print()
