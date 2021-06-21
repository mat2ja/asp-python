# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

from binarytree import Node


class BinaryTree:
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

    # will sort it

    def insert_node(self, value, node='root'):

        if node == 'root':
            node = self.root

        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self.insert_node(value, node.left)
        elif value > node.value:
            node.right = self.insert_node(value, node.right)

        return node

    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left
        return current

    def max_value_node(self, node):
        current = node

        while current.right is not None:
            current = current.right
        return current

    def delete_node(self, value, node='root'):
        if node == 'root':
            node = self.root

        if node is None:
            return node

        if value < node.value:
            node.left = self.delete_node(value, node.left)
        elif value > node.value:
            node.right = self.delete_node(value, node.right)
        else:
            if node.left is None:
                temp = node.right
                node.right = None
                return temp
            if node.right is None:
                temp = node.left
                node = None
                return temp

            # Node with 2 children
            # find the smallest of right, replace root and delete
            temp = self.min_value_node(node.right)
            node.value = temp.value
            node.right = self.delete_node(temp.value, node.right)

        return node


tree = BinaryTree(4)

tree.insert_node(6)
tree.insert_node(2)
tree.insert_node(1)
tree.insert_node(5)
tree.insert_node(10)
tree.insert_node(8)
tree.insert_node(3)
tree.insert_node(12)

print(tree.root)


# tree.print_tree('preorder') # 4 2 1 3 6 5 10 8 12
# tree.print_tree('inorder')  # 1 2 3 4 5 6 8 10 12
tree.print_tree('postorder')  # 1 3 2 5 8 12 10 6 4


'''
    __4__
   /     \
  2       6__
 / \     /   \
1   3   5     10
             /  \
            8    12

'''
tree.delete_node(3)
print("\n\nDeleted 3:", tree.root)
tree.delete_node(6)
print("Deleted 6:", tree.root)
