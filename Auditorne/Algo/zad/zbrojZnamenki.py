import time


def zbrojZnamenki(N):
    res = 0
    for char in str(N):
        res += int(char)
    return res


def zbrojZnamenki2(N):
    res = 0
    while (N > 0):
        res += N % 10
        N //= 10
    return res


def zbrojZnamenki3(N):
    if N < 10:
        return N
    return (N % 10) + zbrojZnamenki(N//10)


if __name__ == '__main__':
    # start = time.time()
    print(zbrojZnamenki(3456))
    print(zbrojZnamenki2(3456))
    print(zbrojZnamenki3(3456))
    # print(time.time()-start)
