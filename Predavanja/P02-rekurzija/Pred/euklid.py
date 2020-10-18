def nzm(a, b):
    if b == 0:
        return a
    return nzm(b, a % b)


if __name__ == "__main__":
    print(nzm(428988, 8))
