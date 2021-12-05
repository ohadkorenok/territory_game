import unittest
from board import Board
from cell import Cell
from random import randint


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(dimensions=18)

    def test_board_has_cells_instances(self):
        for row_arr in self.board.cells:
            for col in row_arr:
                self.assertIsInstance(col, Cell)

    def test_board_has_different_colors(self):
        counter = {'r': 0, 'g': 0, 'y': 0, 'b': 0}
        for row_arr in self.board.cells:
            for col in row_arr:
                counter[col.color] += 1
        [self.assertGreater(val, 0) for (key, val) in counter.items()]

    def test_board_has_ok_indexes(self):
        for row, row_arr in enumerate(self.board.cells):
            for col, cell in enumerate(row_arr):
                self.assertEqual(row, cell.row)
                self.assertEqual(col, cell.column)

    def test_counter_integrity(self):
        for i in range(0, 21):
            color = self.board.colors[randint(0, len(self.board.colors) - 1)]
            self.board.move(color)
            self.assertEqual(self.board.territory.counter, len(self.board.territory.cells))

    def test_small_board(self):
        self.board = Board(dimensions=2)
        colors_to_iterate = self.board.colors
        colors_to_iterate.append(colors_to_iterate[0])
        for color in colors_to_iterate:
            self.board.move(color)
        self.assertTrue(self.board.check_end_game())

    def test_success_in_100_automatic_35_move_games(self):
        success = []
        for i in range(0, 100):
            print(f"Game number {i} have started")
            for j in range(0, 35):
                color = self.board.colors[randint(0, len(self.board.colors) - 1)]
                self.board.move(color)
            if self.board.check_end_game():
                success.append(i)
            self.board = Board(dimensions=18)
        self.assertGreater(len(success), 1)
        print(success)
#