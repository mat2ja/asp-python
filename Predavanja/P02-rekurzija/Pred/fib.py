import functools
#from time import clock
import time
#import sys
# sys.setrecursionlimit()


# koristi se dekorator ili lambda funkcija za automatski keš po algoritmu LRU
@functools.lru_cache(None)
def fib_lru(n):
    if n < 2:
        return n
    return fib_lru(n-1) + fib_lru(n-2)


# memo funkcija koja posprema izračunate vrijednosti u riječnik dictionary u listi parametara
def fib_memo(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib_memo(n-1, computed) + fib_memo(n-2, computed)
    return computed[n]


# slično rješenje sa riječnikom lokalno
def fib_local(n):
    computed = {0: 0, 1: 1}

    def fib_inner(n):
        if n not in computed:
            computed[n] = fib_inner(n-1) + fib_inner(n-2)
        return computed[n]
    return fib_inner(n)


# slično rješenje sa riječnikom lokalno sa ugrađenim exception handling
def fib_local_exc(n):
    computed = {0: 0, 1: 1}

    def fib_inner_x(n):
        try:
            computed[n]
        except KeyError:
            computed[n] = fib_inner_x(n-1) + fib_inner_x(n-2)
        return computed[n]

    return fib_inner_x(n)


# iterativno računanje
# O(n)
def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# BENCH ZA TESTIRANJE
def benchmark(n, *args):
    print("-" * 80)
    for func in args:
        print(func.__name__)
        start = time.time()
        try:
            ret = func(n)
            print("Result:", ret)
        except RuntimeError as e:
            print("Error:", e)
        print("Time:", "{:.8f}".format(time.time() - start))
        print()


# DRIVER KOD
benchmark(6, fib_iter, fib_memo, fib_local, fib_local_exc, fib_lru)
