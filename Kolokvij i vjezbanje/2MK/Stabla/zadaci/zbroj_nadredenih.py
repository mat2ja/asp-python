# Zadano je binarno stablo koje sadrži n čvorova. Problem je pronaći zbroj svih nadređenih čvorova koji imaju podređeni čvor s vrijednošću x.

# Potrebno je napisati funkciju koja određuje tu sumu. Funkciju riješiti rekurzivno.

from binarytree import Node


# odjednom
def find_sum_of_parents_of_x(root, x, sum=0):

    if not root or not root.left or not root.right:
        return sum

    if root.left.value == x or root.right.value == x:
        sum += root.value
        sum = find_sum_of_parents_of_x(root.left, x, sum)
        sum = find_sum_of_parents_of_x(root.right, x, sum)
    return sum


# moja verzija di koristim imutable polje
def find_sum_of_parents_of_x2(root, x):
    sum = [0]
    return find_sum_of_parents_of_x_util(root, x, sum)


def find_sum_of_parents_of_x_util(root, x, sum_ptr):

    if not root or not root.left or not root.right:
        return

    if root.left.value == x or root.right.value == x:
        sum_ptr[0] = sum_ptr[0] + root.value
        find_sum_of_parents_of_x_util(root.left, x, sum_ptr)
        find_sum_of_parents_of_x_util(root.right, x, sum_ptr)
    return sum_ptr[0]


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(2)
root.right.left = Node(2)
root.right.right = Node(3)
print(root)

print(find_sum_of_parents_of_x(root, 2))
print(find_sum_of_parents_of_x2(root, 2))
