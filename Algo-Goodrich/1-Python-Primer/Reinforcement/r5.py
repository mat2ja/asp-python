# Give a single command that computes the sum from Exercise R-1.4, rely-
# ing on Python’s comprehension syntax and the built-in sum function.

def sumSqrs(n):
    return sum([i**2 for i in range(n, 0, -1)])


print(sumSqrs(4))
