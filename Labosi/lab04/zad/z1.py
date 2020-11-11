'''1. Napišite funkciju je_bsp koja vraća True ako je zadano stablo binarno stablo pretraživanja
ili False ako nije'''


def je_bsp(branch):
    if not (1 < len(branch) <= 3) or isinstance(branch[0], list):
        return False

    root = branch[0]
    if len(branch) >= 2:
        left = branch[1]
        if isinstance(left, list):
            if left[0] > root or not je_bsp(left):
                return False
        elif left > root:
            return False

    if len(branch) == 3:
        right = branch[2]
        if isinstance(right, list):
            if right[0] < root or not je_bsp(right):
                return False
        elif right < root:
            return False

    return True


print("\nSljedeci trebaju biti True:")
print(je_bsp([1, 0]))
print(je_bsp([1, 0, 3]))
print(je_bsp([5, [4, 2, 10], 13]))
print(je_bsp([10, 2, 12]))
print(je_bsp([20, [15, 8], 30]))
print(je_bsp([50, [44, 30, 48], [80, [66, 60, 67], 88]]))
print(je_bsp([20, [15, 8, 20], [30, 28, [32, 31, 33]]]))
print(je_bsp([20, [15, 8, [20, [10, 8, 35], 100]], [30, 28, [32, 31]]]))
print(je_bsp([20, [15, 8, [20, [10, 5], 100]], [30, 28, [32, 31, 33]]]))

print("\nSljedeci trebaju biti False:")
print(je_bsp([]))
print(je_bsp([1]))
print(je_bsp([1, 2, 3]))
print(je_bsp([[1, 2, 3], 0, 19]))
print(je_bsp([5, [4, 2, 10], 3]))
print(je_bsp([10, [4, 7, 6], 12]))
print(je_bsp([10, [4], 12]))
print(je_bsp([50, [44, 30, 48], [49, [66, 60, 67], 88]]))
print(je_bsp([20, [15, 8, [20, [10, 11, 35], 100]], [30, 28, [32, 31, 33]]]))
print(je_bsp([20, [15, 8, [20, [10, 12], 100]], [30, 28, [32, 31, 33]]]))
