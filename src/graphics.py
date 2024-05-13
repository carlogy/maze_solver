from tkinter import Tk, BOTH, Canvas
from tkinter.constants import X

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("maze_zolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
        print("Closed window ...")

    def close(self):
        self.__window_running = False
