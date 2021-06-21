# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sumSqrs(n):
    sum = 0
    while n > 0:
        sum += n**2
        n -= 1
    return sum


def sumSqrs2(n):
    sum = 0
    for i in range(n,0,-1):
        sum += i**2
    return sum

print(sumSqrs(4))
print(sumSqrs2(4))
