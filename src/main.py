from graphics import Line, Point, Window
from cell import Cell
from maze import Maze

def main():
    win = Window(1000, 1000)
    m1 = Maze(
        x1=0,
        y1=0,
        num_rows=10,
        num_cols=10,
        cell_size_x=100,
        cell_size_y=100,
        win=win
    )

    m1._break_entrance_and_exit()
    m1._break_walls_r(0,0)


    m1.solve()

    win.wait_for_close()



main()
