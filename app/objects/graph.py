from app.objects.node import Node


class Graph:
    def __init__(self):
        self.lineSize: int = 320
        self.start: int = 0
        self.end: int = (320 * 320) - 1
        self.nodes: list[Node] = []

    def generate_maze(self):
        size = 320
        for i in range(size * size):
            self.nodes.append(Node(i))
        for col in range(size - 1):
            node_id = col
            self.nodes[node_id].walls["right"] = False
            self.nodes[node_id + 1].walls["left"] = False
        for row in range(size - 1):
            node_id = (row * size) + (size - 1)
            self.nodes[node_id].walls["bottom"] = False
            self.nodes[node_id + size].walls["top"] = False
        self.nodes[self.start].walls["left"] = False
        self.nodes[self.end].walls["right"] = False