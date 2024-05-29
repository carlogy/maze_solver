import unittest

from maze import Maze
from graphics import Window



class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        win = Window(100, 100)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_added_padding_x(self):
        num_cols = 10
        num_rows = 10
        win = Window(200, 200)
        m1 = Maze(
                    x1=20,
                    y1=20,
                    num_rows=num_rows,
                    num_cols=num_cols,
                    cell_size_x=10,
                    cell_size_y=10,
                    win=win
        )
        self.assertEqual(
            m1.cells[0][0]._x1,
            m1.x1
        )
    def test_maze_added_padding_y(self):
        num_cols = 10
        num_rows = 10
        win = Window(200, 200)
        m1 = Maze(
                    x1=20,
                    y1=20,
                    num_rows=num_rows,
                    num_cols=num_cols,
                    cell_size_x=10,
                    cell_size_y=10,
                    win=win
        )
        self.assertEqual(
            m1.cells[0][0]._y1,
            m1.y1
        )

    def test_exit_entrance(self):
        num_cols = 10
        num_rows = 10
        win = Window(200, 200)
        m1 = Maze(
                    x1=20,
                    y1=20,
                    num_rows=num_rows,
                    num_cols=num_cols,
                    cell_size_x=10,
                    cell_size_y=10,
                    win=win
        )
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1.cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1.cells[-1][-1].has_bottom_wall,
            False
        )





if __name__ == "__main__":
    unittest.main()
