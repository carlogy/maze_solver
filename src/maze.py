from os import urandom
import time
import random

from cell import Cell

class Maze:
    def __init__(
                    self,
                    x1,
                    y1,
                    num_rows,
                    num_cols,
                    cell_size_x,
                    cell_size_y,
                    win,
                    seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            self.seed = random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        self.cells = []
        for i in range(self.num_cols):
            column = [Cell(self.win) for i in range(self.num_rows)]
            self.cells.append(column)
        else:
            for i in range(len(self.cells)):
                for j in range(len(self.cells[i])):
                    self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[i][j].draw(x1,y1,x2,y2)
        self._animate()

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        i = len(self.cells) - 1
        j = len(self.cells[i]) - 1
        self.cells[i][j].has_bottom_wall = False
        self._draw_cell(i,j)

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            options = []

            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                    options.append(("below", i, j + 1))

            if j > 0 and not self.cells[i][j - 1].visited:
                    options.append(("above", i, j - 1))

            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                    options.append(("right", i + 1, j))

            if i > 0 and not self.cells[i -1][j].visited:
                    options.append(("left", i - 1, j))

            if len(options) == 0:
                return

            next = random.randrange(len(options))
            next_cell = options[next]
            column = next_cell[1]
            row = next_cell[2]

            match next_cell[0]:
                case "below":
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[next_cell[1]][next_cell[2]].has_top_wall = False
                    self._break_walls_r(i=next_cell[1], j=next_cell[2])
                case "above":
                    self.cells[i][j].has_top_wall = False
                    self.cells[next_cell[1]][next_cell[2]].has_bottom_wall = False
                    self._break_walls_r(i=next_cell[1], j=next_cell[2])
                case "right":
                    self.cells[i][j].has_right_wall = False
                    self.cells[next_cell[1]][next_cell[2]].has_left_wall = False
                    self._break_walls_r(i=next_cell[1], j=next_cell[2])
                case "left":
                    self.cells[i][j].has_left_wall = False
                    self.cells[next_cell[1]][next_cell[2]].has_rigth_wall = False
                    self._break_walls_r(i=next_cell[1], j=next_cell[2])
                case _:
                    raise IndexError("Invalid random index chosen for next cell to visit")


    def _reset_cells_visited(self):
        for column in self.cells:
            for cell in column:
                cell.visited = False


    def _animate(self):
        self.win.redraw()
        time.sleep(0.02)

    def solve(self):
        solved = self._solve_r(i=0,j=0)
        return solved

    def _solve_r(self, i, j):
        self._animate()
        self.cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        if j < self.num_rows - 1 and not self.cells[i][j + 1].visited and not self.cells[i][j +1].has_bottom_wall:
            self.cells[i][j].draw_move(to_cell=self.cells[i][j + 1])
            self._solve_r(i=i, j=j + 1)
        elif j < self.num_rows - 1 and self.cells[i][j + 1].visited or not self.cells[i][j +1].has_bottom_wall:
            self.cells[i][j].draw_move(to_cell=self.cells[i][j + 1], undo=True)

        if j > 0 and not self.cells[i][j - 1].visited:
            self.cells[i][j].draw_move(to_cell=self.cells[i][j - 1])
            self._solve_r(i=i, j=j - 1)
        elif j > 0 and self.cells[i][j - 1].visited or self.cells[i][j - 1].has_bottom_wall:
            self.cells[i][j].draw_move(to_cell=self.cells[i][j - 1], undo=True)

        if i < self.num_cols - 1 and not self.cells[i + 1][j].visited and not self.cells[i + 1][j].has_left_wall:
            self.cells[i][j].draw_move(to_cell=self.cells[i + 1][j])
            self._solve_r(i=i + 1, j=j)
        elif i < self.num_cols - 1 and self.cells[i + 1][j].visited or self.cells[i + 1][j].has_left_wall:
            self.cells[i][j].draw_move(to_cell=self.cells[i + 1][j], undo=True)

        if i > 0 and not self.cells[i -1][j].visited and not self.cells[i - 1][j].has_right_wall:
            self.cells[i][j].draw_move(to_cell=self.cells[i - 1][j])
            self._solve_r(i=i -1, j=j)
        elif i > 0 and self.cells[i - 1][j].visited and self.cells[i - 1][j].has_right_wall:
            self.cells[i][j].draw_move(to_cell=self.cells[i - 1][j], undo= True)

        return False
