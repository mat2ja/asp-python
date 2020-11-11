class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
            print(start.value)
            self.preorder_print(start.left)
            self.preorder_print(start.right)

    def inorder_print(self, start):
        '''Left->Root->Right'''
        if start:
            self.inorder_print(start.left)
            print(start.value)
            self.inorder_print(start.right)

    def postorder_print(self, start):
        '''Left->Right->Root'''
        if start:
            self.postorder_print(start.left)
            self.postorder_print(start.right)
            print(start.value)

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

    def min_value_node(node):
        current = node

        while current.left is not None:
            current = current.Left
        return current

    def max_value_node(node):
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


tree = BinaryTree(5)

tree.insert_node(6)
tree.insert_node(2)
tree.insert_node(1)
tree.insert_node(10)
tree.insert_node(8)
tree.insert_node(3)
tree.insert_node(12)

tree.delete_node(3)
tree.delete_node(6)

# tree.print_tree('preorder')
tree.print_tree('inorder')
# tree.print_tree('postorder')
