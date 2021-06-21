# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sumOddSqrs(n):
    sum = 0
    for i in range(n, 0, -1):
        if i % 2 != 0:
            sum += i**2
    return sum


print(sumOddSqrs(30))
