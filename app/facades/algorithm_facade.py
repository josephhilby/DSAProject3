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

    def plot(self, nodes, algorithm, line_size, top, left):
        result = self.solve(nodes, algorithm)
        coords, visited_count = result
        cell_size = line_size // 320
        path = []
        for node_id in coords:
            row = (node_id) // 320
            col = (node_id) % 320
            x = left + col * cell_size + cell_size // 2
            y = top + row * cell_size + cell_size // 2
            path.append((x, y))
        return path, visited_count

