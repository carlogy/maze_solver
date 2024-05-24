
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
                    win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self.cells = []
        for i in range(self.num_cols):
            column = [Cell(self.win) for i in range(self.num_rows // self.cell_size_y)]
            self.cells.append(column)
        else:
            for i in range(len(self.cells)):
                for j in range(len(self.cells[i])):
                    self.cells[i][j]._draw_cell(i,j) #this was updated to call the draw_cell maze method on the specific cell in matrix.

    def _draw_cell(self, I, J):
        # This method should calculate the x/y position of the Cell based on i, j, the cell_size, and the x/y position of the Maze itself.
        # The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window.
        cell_x = self.x1 * (I * self.cell_size_x)
        cell_y = self.y1 * (J * self.cell_size_y)

        self._animate()
    def _animate(self):
        self.win.redraw()
