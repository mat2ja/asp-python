from binarytree import Node


def zizagtraversal(root):

    if not root:
        return

    curr_level = []
    next_level = []

    ltr = True  # left to right

    curr_level.append(root)

    while len(curr_level) > 0:
        popped = curr_level.pop()
        print(popped.value, end=" ")

        if ltr:
            if popped.left:
                next_level.append(popped.left)
            if popped.right:
                next_level.append(popped.right)
        else:
            if popped.right:
                next_level.append(popped.right)
            if popped.left:
                next_level.append(popped.left)

        if len(curr_level) == 0:
            ltr = not ltr
            curr_level, next_level = next_level, curr_level


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print(root)
print("Cikcak obilazak binarnog stabla je:")
zizagtraversal(root)
