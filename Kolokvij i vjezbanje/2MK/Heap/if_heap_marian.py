from binarytree import Node

# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


def check_if_max_heap(root):
    number_of_nodes = count_nodes(root)
    heap_property = has_heap_property(root)
    complete_tree_prop = is_complete_tree(root, 0, number_of_nodes)
    return heap_property and complete_tree_prop


def count_nodes(root):
    if root:
        return 1 + count_nodes(root.left) + count_nodes(root.right)
    return 0


def has_heap_property(root):
    if root.left is None and root.right is None:
        return True
    if root.right is None:
        return root.value >= root.left.value
    else:
        if root.left:
            if root.value > root.left.value and root.value > root.right.value:
                return has_heap_property(root.left) and has_heap_property(root.right)
            else:
                return False
        else:
            return False


def is_complete_tree(root, index, number_of_nodes):
    if root is None:
        return True
    if index >= number_of_nodes:
        return False
    return is_complete_tree(root.left, 2*index+1, number_of_nodes) and is_complete_tree(root.right, 2*index+2, number_of_nodes)



root1 = Node(6)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(1)
print(root1)
print("Is it max heap: ", check_if_max_heap(root1))

root2 = Node(6)
root2.left = Node(1)
root2.right = Node(3)
root2.left.right = Node(2)
print(root2)
print("Is it max heap: ", check_if_max_heap(root2))

root3 = Node(2)
root3.left = Node(6)
root3.right = Node(1)
root3.left.left = Node(1)
print(root3)
print("Is it max heap: ", check_if_max_heap(root3))

root4 = Node(8)
root4.left = Node(2)
root4.right = Node(5)
root4.left.right = Node(0)
root4.left.left = Node(1)
print(root4)
print("Is it max heap: ", check_if_max_heap(root4))


root5 = Node(8)
root5.left = Node(2)
# root5.right = Node(5)
root5.left.left = Node(4)
print(root5)
print("Has heap property: ", has_heap_property(root5))
