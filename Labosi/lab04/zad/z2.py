class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def napravi_binarno_stablo(values):
    i = 0
    while i < len(values):
        for value in values:
            root = Node(value)
        i += 1
