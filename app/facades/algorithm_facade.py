from app.algorithms.flood_fill import FloodFill
from app.algorithms.wall_follow import WallFollow


class AlgorithmFacade:
    def __init__(self):
        self.flood_fill = FloodFill()
        self.wall_follow = WallFollow()

    def names(self):
        return [self.flood_fill.name, self.wall_follow.name]

    def solve(self, nodes, algorithm):
        match algorithm:
            case self.flood_fill.name:
                return self.flood_fill.solve(nodes)
            case self.wall_follow.name:
                return self.wall_follow.solve(nodes)
            case _:
                raise ValueError(f'Unknown algorithm, {algorithm}')
