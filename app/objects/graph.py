from app.objects.node import Node

class Graph:
    def __init__(self):
        self.lineSize: int = 5  
        self.start: int = 0
        self.end: int = (5 * 5) - 1  
        self.nodes: list[Node] = []

    def generate_maze(self):
        for i in range(1, 26):  
            node = Node(i)
            self.nodes.append(node)
        
        self.nodes[0].walls["right"] = False  
        self.nodes[1].walls["right"] = False  
        self.nodes[2].walls["right"] = False  
        self.nodes[3].walls["right"] = False  
        self.nodes[4].walls["bottom"] = False 
        self.nodes[9].walls["bottom"] = False 
        self.nodes[14].walls["bottom"] = False 
        self.nodes[19].walls["bottom"] = False 
       
        self.nodes[self.start].walls["left"] = False
        self.nodes[self.end].walls["right"] = False