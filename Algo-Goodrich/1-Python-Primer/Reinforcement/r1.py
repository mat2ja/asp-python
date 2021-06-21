# Write a short Python function, is
# multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def isMultiple(n, m):
    return True if n % m == 0 else False


a = isMultiple(10, 3)
b = isMultiple(10, 5)
print(a, b)
