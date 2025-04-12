import unittest

from app.objects.maze import Maze


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Maze()

    def test_init(self):
        self.assertIsInstance(self.board, Maze)
