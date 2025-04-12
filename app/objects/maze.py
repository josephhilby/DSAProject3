from app.objects.node import Node


class Maze:
    """
    Class representing a maze.
    """
    def __init__(self):
        self.start = None
        self.end = None
        self.board = [Node]

    def generate_maze(self):
        # this is a 4x4 maze that is a stub for generate_maze
        self.start = 1
        self.end = 15

        for num in range(0, 16):
            self.board.append(Node(num))

        self.board[0].add_right(self.board[1])

        self.board[1].add_right(self.board[2])

        self.board[2].add_right(self.board[3])
        self.board[2].add_down(self.board[6])

        self.board[4].add_down(self.board[8])

        self.board[5].add_down(self.board[9])

        self.board[6].add_down(self.board[10])
        self.board[6].add_right(self.board[7])

        self.board[7].add_down(self.board[11])

        self.board[8].add_down(self.board[12])

        self.board[9].add_down(self.board[13])

        self.board[10].add_down(self.board[14])

        self.board[11].add_down(self.board[15])

        self.board[12].add_right(self.board[13])

        self.board[13].add_right(self.board[14])
