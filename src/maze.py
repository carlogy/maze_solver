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
        j = len(self.cells[i]) -1
        self.cells[i][j].has_bottom_wall = False
        self._draw_cell(i,j)

    def break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        loop = True
        while loop:
            options = []
            cell_below = self.cells[i][j + 1]
            cell_right = self.cells[i + 1][j]
            cell_left = self.cells[i - 1][j]
            cell_above = self.cells[i][j - 1]
            if not cell_left.visited:
                options.append((i, j + 1))
            if not cell_right.visited:
                options.append((i + 1, j))
            if not cell_below.visited:
               options.append((i, j + 1))
            if not cell_above.visited:
               options.append((i, j + 1))
            if (
                cell_left.visited == True and
                cell_right.visited == True and
                cell_above.visited == True and
                cell_below.visited == True):
                    return
            direction = random.randrange(0,len(options))
            if options[direction][0] == i:
                if j < options[direction][1]:
                    self.cells[i][options[direction][1]].has_bottom_wall = False
                    self.break_walls_r(options[direction][0], options[direction][1])
                if j > options[direction][1]:
                    self.cells[i][options[direction][1]].has_top_wall = False
                    self.break_walls_r(options[direction][0], options[direction][1])
                elif options[direction][0] > i:
                    self.cells[options[direction][0]][j].has_right_wall = False
                    self.break_walls_r(options[direction][0], options[direction][1])
                elif options[direction][0] < i:
                   self.cells[options[direction][0]][j].has_left_wall = False
                   self.break_walls_r(options[direction][0], options[direction][1])







    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
