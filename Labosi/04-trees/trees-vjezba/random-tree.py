from binarytree import Node, tree, bst, heap, build

# Generate a random binary tree and return its root node
my_tree = tree(height=3, is_perfect=False)

# Generate a random BST and return its root node
my_bst = bst(height=3, is_perfect=True)

# Generate a random max heap and return its root node
my_heap = heap(height=3, is_max=True, is_perfect=False)

# Pretty-print the trees in stdout
print("BinaryTree:", my_tree)
print("\nBST:", my_bst)
print("Heap:", my_heap)

print("Preorder:", my_bst.preorder)
print("Inorder:", my_bst.inorder)
print("Postorder:", my_bst.postorder)
print("Levelorder:", my_bst.levelorder)  # print(list(my_bst))


values = [7, 3, 2, 6, 9, None, 1, 5, 8]
root = build(values)
print(root)
print(root.values)
