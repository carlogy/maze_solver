from graphics import Point, Window, Line

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.visited = False
        self._win = win

    def __repr__(self):
        return f"Left: {self.has_left_wall}\nTop: {self.has_top_wall}\nRight: {self.has_right_wall}\nBottom: {self.has_bottom_wall}\nVisited: {self.visited}"

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        pointA = Point(self._x1, self._y1)
        pointB = Point(self._x1, self._y2)
        pointC = Point(self._x2, self._y2)
        pointD = Point(self._x2, self._y1)

        if self.has_left_wall:
            self._win.draw_line(Line(pointA, pointB))
        if not self.has_left_wall:
            self._win.draw_line(Line(pointA, pointB), "white")
        if self.has_right_wall:
            self._win.draw_line(Line(pointC, pointD))
        if not self.has_right_wall:
            self._win.draw_line(Line(pointC, pointD), "white")
        if self.has_top_wall:
            self._win.draw_line(Line(pointA, pointD))
        if not self.has_top_wall:
            self._win.draw_line(Line(pointA, pointD), "white")
        if self.has_bottom_wall:
            self._win.draw_line(Line(pointB, pointC))
        if not self.has_bottom_wall:
            self._win.draw_line(Line(pointB, pointC), "white")

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
