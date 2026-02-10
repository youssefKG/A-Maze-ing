from abc import ABC
from maze.maze_state import MazeState
from my_mlx.my_mlx import MyMlx
from renderer.images.cellImg import CellsImage


class Solver(ABC):
    def __init__(self) -> None:
        self.is_finished: bool = False
        self.frames: int = 0
        self.is_running: bool = False
        self.maze_state = MazeState()
        self.cells_img = CellsImage()
        self.is_path_shown: bool = False

    def set_horizontal_cells(self, horizontal_cells: int) -> object:
        self.horizontal_cells = horizontal_cells
        return self

    def set_vertical_cells(self, vertical_cells: int) -> object:
        self.vertical_cells = vertical_cells
        return self

    def generate(self) -> None:
        pass

    def draw_path(self) -> None:
        pass

    def hide_path(self) -> None:
        pass

    def toggle_path(self) -> None:
        pass

    def redraw_maze(self) -> None:
        pass

    def put_cells_img_to_window(self) -> None:
        x = int(MyMlx.screen_width / 2 - self.cells_img.width / 2)
        y = int(MyMlx.screen_height / 2 - self.cells_img.height / 2)
        MyMlx.put_image_to_window(self.cells_img.ptr, x, y + 20)
