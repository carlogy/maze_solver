from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("maze_zolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        canvas = Canvas()
        canvas.pack()
        window_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_running = True

    def close(self):
        self.window_running = False
