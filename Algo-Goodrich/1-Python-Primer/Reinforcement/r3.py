# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

import random


# def minmax(data):
#     data.sort() # in-place
#     return (data[0], data[-1])


def minmax(data):
    sortedData = sorted(data)  # return new list
    return (sortedData[0], sortedData[-1])


def randomData(size=10):
    data = []
    for i in range(size):
        data.append(random.randint(0, 100))
    return data


a = randomData()
b = randomData()

print(a)
print(b)

print(minmax(a))
print(minmax(b))
