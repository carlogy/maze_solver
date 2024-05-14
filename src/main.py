from graphics import Line, Point, Window

def main():
    win = Window(800, 600)
    point1 = Point(100, 100)
    point2 = Point(100, 200)
    line1 = Line(point1, point2)
    win.draw_line(line1, "black")
    point3 = Point(400, 400)
    point4 = Point(500, 400)
    line2 = Line(point3, point4)
    win.draw_line(line2, "green")
    win.wait_for_close()

main()
