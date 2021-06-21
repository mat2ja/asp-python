# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def isEven(k):
    if k == 1:
        return False
    elif k == 0:
        return True
    else:
        return isEven(k-2)


a = isEven(14)
b = isEven(11)
c = isEven(0)
d = isEven(1)
print(a, b, c, d)
