from binarytree import Node


def longest_path_sum(root, maxDubina=-99999, maxSuma=0, dubina=-1, suma=0):
    if root is None:
        if dubina > maxDubina:
            maxDubina = dubina
            maxSuma = suma
        elif maxDubina == dubina and suma > maxSuma:
            maxSuma = suma
        return maxSuma

    dubina += 1
    suma += root.value

    sumaL = longest_path_sum(root.left, maxSuma, maxDubina, dubina, suma)
    sumaR = longest_path_sum(root.right, maxSuma, maxDubina, dubina, suma)
    suma = max(sumaL, sumaR)
    return suma


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(1)
root.right.left = Node(2)
root.right.right = Node(3)
root.left.right.left = Node(6)
root.right.right.left = Node(4)

print(root)

print(longest_path_sum(root))
