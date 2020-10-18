def korijen(x):
    a = 1
    while abs(a ** 2 - x) > 0.001:
        a = (a + x / a) / 2
        return a


print('%.4f' % (korijen(4)))
