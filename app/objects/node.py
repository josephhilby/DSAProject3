class Node:
    """
    Class representing a cell, to be put in a graph

    Doubly Linked List Node, ID will dictate placement in maze by UI
        row = id // 320
        col = id % 320

    Walls (edges) are held as a dict of bools
    If visited in a given solution mark visited to True
    """
    def __init__(self, id: int):
        self.id: int = id
        self.next: Node | None = None
        self.prev: Node | None = None
        self.visited: bool = False
        self.walls: dict[str, bool] = {"top": True, "bottom": True, "left": True, "right": True}
