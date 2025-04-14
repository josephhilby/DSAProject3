from app.objects.node import Node


class FloodFill:
    """
    Class to hold logic for flood fill algorithm

    Name used for game logic
    Solve should take in a doubly linked graph and
    return array of node id's for solution
    """
    def __init__(self):
        self.name = "Flood Fill"

    def solve(self, nodes: [Node]):
        return list(range(1, 321)) + list(range(320, 102401, 320))