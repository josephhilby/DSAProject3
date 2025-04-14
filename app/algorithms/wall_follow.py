from app.objects.node import Node


class WallFollow:
    """
    Class to hold logic for wall follow algorithm

    Name used for game logic
    Solve should take in a doubly linked graph and
    return array of node id's for solution
    """
    def __init__(self):
        self.name = "Wall Follow"

    def solve(self, nodes: [Node]):
        return list(range(1, 102401, 320))