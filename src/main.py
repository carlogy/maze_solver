from graphics import Line, Point, Window
from cell import Cell

def main():
    win = Window(800, 600)
    point1 = Point(100, 100)
    point2 = Point(100, 200)
    line1 = Line(point1, point2)
    win.draw_line(line1)
    point3 = Point(400, 400)
    point4 = Point(500, 400)
    line2 = Line(point3, point4)
    win.draw_line(line2, "green")
    cell1 = Cell(True,True,True,True, 10, 20, 15, 25, win)
    cell1.draw()
    cell2 = Cell(True, False, True, False, 30, 40, 50, 60, win)
    cell2.draw()
    cell3 = Cell(False, False, True, True, 550, 560, 560, 570, win)
    cell3.draw()
    win.wait_for_close()

main()
