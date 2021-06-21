# Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function.


def sumOddSqrs(n):
    return sum([k**2 for k in range(n, 0, -1) if k % 2 != 0])


print(sumOddSqrs(30))
