from abc import ABC
from maze.cell import Cell
from maze.maze_state import MazeState
from my_mlx.my_mlx import MyMlx

class Solver(ABC):
    def __init__(self):
        self.is_finished = False
        self.frames = 0
        self.is_running = False
        self.maze_state = MazeState()
        self.is_path_shown = False

    def set_horizontal_cells(self, horizontal_cells: int):
        self.horizontal_cells = horizontal_cells
        return self

    def set_vertical_cells(self, vertical_cells):
        self.vertical_cells = vertical_cells
        return self

    def set_cells_img(self, cells_img):
        self.cells_img = cells_img
        return self


    def generate(self):
        pass

    def  draw_path(self):
        pass

    def hide_path(self):
        pass

    def toggle_path(self):
        pass

    def put_cells_img_to_window(self) -> None:
        x = int((MyMlx.screen_width * 0.8) / 2 - self.cells_img.width / 2)
        y = int(MyMlx.screen_height / 2 - self.cells_img.height / 2)
        MyMlx.put_image_to_window(self.cells_img.ptr, x, y)
