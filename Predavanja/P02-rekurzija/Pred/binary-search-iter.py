import time


def binary_search_iter(array, item):

    lo, hi = 0, len(array)

    while lo < hi:
        mid = (hi + lo)//2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            hi = mid
        else:
            lo = mid + 1
    return False


if __name__ == '__main__':
    import timeit
    s = [3, 4, 6, 8, 9, 10, 16, 22, 23, 25, 28, 30, 32, 67, 89, 99, 100]

    start = time.perf_counter()

    print("Nađen je na lokaciji: ", binary_search_iter(s, 99))
    print(s)

    end = time.perf_counter()
    print(end - start)
    #print(timeit.timeit("binary_search_iter(s,99)", setup="from __main__ import binary_search_iter"))
