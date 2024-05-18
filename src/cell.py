from graphics import Point, Window, Line

class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, x2, y1, y2, win):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        pointA = Point(self._x1, self._y1)
        pointB = Point(self._x1, self._y2)
        pointC = Point(self._x2, self._y2)
        pointD = Point(self._x2, self._y1)


        if self.has_left_wall:
            self._win.draw_line(Line(pointA, pointB))
        if self.has_right_wall:
            self._win.draw_line(Line(pointC, pointD))
        if self.has_top_wall:
            self._win.draw_line(Line(pointA, pointD))
        if self.has_bottom_wall:
            self._win.draw_line(Line(pointB, pointC))

    def draw_move(self, to_cell, undo=False):

        if undo:
            line_color = "gray"
        line_color = "red"

        mid_x_axis1 = (self._x1 + to_cell._x1) / 2
        mid_y_axis1 = (self._y1 + to_cell._y1) / 2
        mid_x_axis2 = (self._x2 + to_cell._x2) / 2
        mid_y_axis2 = (self._y2 + to_cell._y2) / 2
        pointA = Point(mid_x_axis1, mid_y_axis1)
        pointB = Point(mid_x_axis2, mid_y_axis2)

        self._win.draw_line(Line(pointA, pointB), line_color)
