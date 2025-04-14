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

    def solve(self, nodes: list[Node]):
        self.dim=320
        start = 0
        end =(self.dim*self.dim)-1
        visited = set()
        prev = {start: None} #keeps track of the previous nodes
        queue = [start] #queue for BFS
        while queue:
            current_num = queue.pop(0)
            if current_num in visited:
                continue
            current_node = nodes[current_num]
            visited.add(current_num)
            if current_num == end:
                break
            row = current_num // self.dim #get current row
            col = current_num % self.dim #get current column

            #these are the possible movements
            directions = [("top",-self.dim,row>0),("bottom",self.dim,row<self.dim-1),("left",-1,col>0),("right",1,col<self.dim-1)]
            #try all the movement directions
            for wall,offset,valid in directions:
                if not current_node.walls[wall] and valid: #in bounds and no wall
                    neighbor_id = current_num + offset
                    if neighbor_id not in visited: #if neighbor hasnt been visited...
                        queue.append(neighbor_id)#...add it to the queue
                        prev[neighbor_id] = current_num
        
        #i dont know if there will be mazes with no solution but i put the edge case check in just in case
        if end not in prev:
            return []
        #this part reconstructs the path using the prev dictionary  
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = prev.get(current)
        #reverse the path to get it in the correct order since we went from end to start
        path.reverse()
        
        return path
