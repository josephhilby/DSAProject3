from app.objects.node import Node
import random

class Graph:
    def __init__(self):
        self.lineSize: int = 320
        self.start: int = 0
        self.end: int = (320 * 320) - 1
        self.nodes: list[Node] = []

    def generate_maze(self):
        # initialize nodes with walls. may need an extra 2 here
        # odd from 1 to end. inclusive
        for num in range(self.start, self.end + 1):
            self.nodes.append(Node(num))

        # setting entry & exit points of the maze
        # enter on the left, exit on the right
        self.nodes[self.start].walls["left"] = False
        self.nodes[self.end].walls["right"] = False

        # initialize disjointed-set (union-find) structure
        parent = {node.id: node.id for node in self.nodes}

        # 'find' and 'union' functions for union-find structure
        # 'find' function to find the root of a node
        def find(node_id):
            if parent[node_id] != node_id:
                parent[node_id] = find(parent[node_id])
            return parent[node_id]

        # unionizing two disjoint sets based on their roots
        def unionization(node1_id, node2_id):
            root1 = find(node1_id)
            root2 = find(node2_id)
            if root1 != root2:
                # merging smaller root into larger
                if root1 < root2:
                    parent[root2] = root1
                else:
                    parent[root1] = root2

        # edge list between adjacent cells
        edges = []
        for node in self.nodes:
            # add edges to the right and down neighbors
            # right neighbor
            if (node.id + 1) % self.lineSize != 0:
                edges.append((node.id, node.id + 1))
            # bottom neighbor
            if node.id + self.lineSize < len(self.nodes):
                edges.append((node.id, node.id + self.lineSize))
        # shuffle the edges to randomize the maze generation
        random.shuffle(edges)

        # lookup. id --> node object
        node_map = {node.id: node for node in self.nodes}
        # building the maze
        for node1_id, node2_id in edges:
            node1 = node_map[node1_id]
            node2 = node_map[node2_id]

            # Check if the nodes are already connected
            if find(node1_id) != find(node2_id):
                # Connect the nodes and remove the wall between them
                unionization(node1_id, node2_id)

                # determning which walls to remove
                if node1.id + 1 == node2.id:  # right
                    node1.walls["right"] = False
                    node2.walls["left"] = False
                elif node1.id + self.lineSize == node2.id:  # below
                    node1.walls["bottom"] = False
                    node2.walls["top"] = False
                elif node2.id + 1 == node1.id:  # left
                    node2.walls["right"] = False
                    node1.walls["left"] = False
                elif node2.id + self.lineSize == node1.id:  # above
                    node2.walls["bottom"] = False
                    node1.walls["top"] = False
                else:  # don't know if i need this
                    raise ValueError("Invalid edge connection between nodes")