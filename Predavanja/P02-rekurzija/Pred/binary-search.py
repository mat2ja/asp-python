import time

def binary_search(data, target, low, high, k):
    """
    Vraća True ako je nađen .
    Traženje od data[low] do data[high] uključno.
    """

    if low > high:
        return False                    # interval je prazan
    else:
        mid = (low + high) // 2
        k = k + 1
        print("Broj koraka:", k)
        if target == data[mid]:         # element je pronađen
            return True
        elif target < data[mid]:
            # rekurzija od left do middle
            return binary_search(data, target, low, mid - 1, k)
        else:
            # rekurzija do  right od middle
            return binary_search(data, target, mid + 1, high, k)


if __name__ == '__main__':
    S = [3, 9, 22, 99, 45, 1, 56, 33, 8, 67, 85, 32]
    S = sorted(S)
    print(S)
    a = len(S)
    k = 0
    start = time.perf_counter()
    # start = time.time()

    print(binary_search(S, 99, 0, a-1, k))
    
    end = time.perf_counter()
    print(end - start)
