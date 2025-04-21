from app.objects.node import Node


class WallFollow:
    """
    Class to hold logic for wall follow algorithm
    """
    def __init__(self):
        self.name: str = "Wall Follow"

    def solve(self, nodes: list[Node]):
        self.dim = 320
        start = 0
        end = (self.dim * self.dim) - 1
        #clockwise movement directions and their offsets
        directions = ["up", "right", "down", "left"]
        direction_vecs = {"up": -self.dim, "right": 1, "down": self.dim, "left": -1}
        walls = {"up":"top", "right":"right", "down":"bottom", "left":"left"}

        current = start
        current_direction = "right"
        #path that will be updated if nodes are in solution
        path = [current]
        #set of visited nodes
        visited = set()
        while current != end:
            current_node = nodes[current]
            visited.add(current)

            direction_index = directions.index(current_direction)
            #directions relative to current 
            right = directions[(direction_index + 1) % 4]
            forward = current_direction
            left = directions[(direction_index - 1) % 4]
            backward = directions[(direction_index + 2) % 4]
            moved = False
            for move_attempt in [right, forward, left, backward]:
                wall = walls[move_attempt]
                offset = direction_vecs[move_attempt]
                neighbor = current + offset
                #bounds check
                if 0 <= neighbor < len(nodes):
                    if wall in ["left", "right"]:
                        row1 = current//self.dim
                        row2 = neighbor//self.dim
                        if row1 != row2:
                            continue
                    #if theres no wall we can move    
                    if not current_node.walls[wall]:
                        current = neighbor
                        current_direction = move_attempt
                        #if we moved, add to path
                        path.append(current)
                        moved = True
                        break
            if not moved:
                break
        return path
