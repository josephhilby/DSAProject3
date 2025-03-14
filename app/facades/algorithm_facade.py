from app.algorithms.flood_fill import FloodFill
from app.algorithms.wall_follow import WallFollow


class AlgorithmFacade:
    def __init__(self):
        self.flood_fill = FloodFill()
        self.wall_follow = WallFollow()

    def names(self):
        return [self.flood_fill.name, self.wall_follow.name]
