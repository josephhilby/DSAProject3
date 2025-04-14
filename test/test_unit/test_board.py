import unittest

from app.objects.graph import Graph


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Graph()

    def test_init(self):
        self.assertIsInstance(self.board, Graph)
