# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

from binarytree import Node


class BST():
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root)
        if traversal_type == 'inorder':
            return self.inorder_print(self.root)
        if traversal_type == 'postorder':
            return self.postorder_print(self.root)

    def preorder_print(self, start):
        '''Root->Left->Right'''
        if start:
            print(start.value, end=" ")
            self.preorder_print(start.left)
            self.preorder_print(start.right)

    def inorder_print(self, start):
        '''Left->Root->Right'''
        if start:
            self.inorder_print(start.left)
            print(start.value, end=" ")
            self.inorder_print(start.right)

    def postorder_print(self, start):
        '''Left->Right->Root'''
        if start:
            self.postorder_print(start.left)
            self.postorder_print(start.right)
            print(start.value, end=" ")

    def insert(self, value, node="root"):
        if node == "root":
            node = self.root

        if node is None:
            return Node(value)

        if value <= node.value:
            node.left = self.insert(value, node.left)
        elif value > node.value:
            node.right = self.insert(value, node.right)

        return node

    def first_child(self):
        if self.root.left:
            return self.root.value
        return

    def search_node(self, key, root):

        if root is None:
            return "Node not found"
        elif root.value == key:
            return root
            # return root.value

        if key < root.value:
            return self.search_node(key, root.left)
        else:
            return self.search_node(key, root.right)

    def min_node(self, root):
        curr = root

        while curr.left:
            curr = curr.left
        return curr

    def max_node(self, root):
        curr = root
        while curr.right:
            curr = curr.right
        return curr

    def delete_node(self, key, root):
        if not root:
            return root

        if key < root.value:
            root.left = self.delete_node(key, root.left)
        elif key > root.value:
            root.right = self.delete_node(key, root.right)
        else:
            if root.left is None:  # 1 or no children
                deleted_node = root.right
                root = None
                return deleted_node  # vrati izbrisani cvor
            elif root.right is None:
                deleted_node = root.left
                root = None
                return deleted_node

            # if has 2 children
            temp = self.min_node(root.right)
            root.value = temp.value
            root.right = self.delete_node(temp.value, root.right)

        return root


def postorder_print(root):
    if root:
        postorder_print(root.left)
        postorder_print(root.right)
        print(root.value, end=" ")


tree = BST(14)
tree.insert(8)
tree.insert(22)
tree.insert(4)
tree.insert(18)
tree.insert(11)
tree.insert(24)
tree.insert(14)
tree.insert(3)
tree.insert(5)
tree.insert(25)
tree.insert(10)
tree.insert(7)
print(tree.root)

tree2 = Node(15)
tree2.left = Node(10)
tree2.left.left = Node(5)
tree2.right = Node(20)
tree2.right.right = Node(30)

print("Novo")
print(tree2)
postorder_print(tree2)  # 5 10 30 20 15
print()

# print("Traženje 14", tree.search_node(14, tree.root))
# print("Traženje 34:", tree.search_node(34, tree.root))
# print("Min node:", tree.min_node(tree.root))
# print("Max node:", tree.max_node(tree.root))

# tree.delete_node(4, tree.root)
# print(tree.root)
