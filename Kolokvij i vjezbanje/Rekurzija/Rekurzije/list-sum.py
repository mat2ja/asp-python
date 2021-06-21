# Write a Python program of recursion list sum.


def sumiraj(lista):
    total = 0
    for elem in lista:
        if isinstance(elem, list):
            total += sumiraj(elem)
        else:
            total += elem
    return total


a = [1, 2, [3, 4], [5, 6]]
print(sumiraj(a))
