class Node:
    def __init__(self, id: int):
        self.id = id
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def add_right(self, node):
        self.right = node
        node.left = self

    def add_left(self, node):
        self.left = node
        node.right = self

    def add_up(self, node):
        self.up = node
        node.down = self

    def add_down(self, node):
        self.down = node
        node.left = self