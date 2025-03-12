import unittest

from app.objects.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init(self):
        self.assertIsInstance(self.board, Board)

    def test_attr(self):
        self.assertEqual(self.board.row, [1, 2, 3])
