from app.objects.node import Node


class Maze:
    """
    Class representing a maze

    An array of nodes, position in array will dictate placement in maze
        row = node.id / 320
        col = node.id % 320

    Hardcoded a line size of 320, total size 320x320
    Walls (edges) are held as a dict of bools in Node objects
    """
    def __init__(self):
        self.lineSize: int = 320
        self.start: int = 0
        self.end: int = (320*320) - 1
        self.nodes: [] = []

    def generate_maze(self):
        for num in range(self.start + 1, self.end + 2):
            self.nodes.append(Node(num))

        self.nodes[self.start].walls["left"] = False
        self.nodes[self.end].walls["right"] = False

        # create program that selects two random nodes in 'nodes'
        # then checks to see if they are in the same disjointed-set (union-find)
        # connects (smaller to larger) them only if they were in diff sets
        # removes wall based on location (e.g. 1 <- 2, 1 remove right wall, 2 remove left wall;
        # 1 <- 321, 1 remove bottom wall, 321 remove top wall)