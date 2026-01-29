from abc import ABC
from maze.cell import Cell
from my_mlx.my_mlx import MyMlx

class Solver(ABC):
    def __init__(self):
        pass

    def set_horizontal_cells(self, horizontal_cells):
        self.horizontal_cells = horizontal_cells
        return self

    def set_vertical_cells(self, vertical_cells):
        self.vertical_cells = vertical_cells
        return self

    def set_cells_img(self, cells_img):
        self.cells_img = cells_img
        return self

    def find_path(self):
        print("hello")

    def set_cells_grid(self, cells_grid: list[list[Cell]]):
        self.cells_grid = cells_grid
        return self

    def set_entry_cell(self, entry_cell: tuple):
        (x, y) = entry_cell
        self.entry_cell = self.cells_grid[y][x]
        return self

    def set_exit_cell(self, exit_cell: tuple):
        (x, y) = exit_cell
        self.exit_cell = self.cells_grid[y][x]
        print(self.exit_cell.x, self.exit_cell.y)
        return self

    def put_cells_img_to_window(self) -> None:
        x = int((MyMlx.screen_width * 0.8) / 2 - self.cells_img.width / 2)
        y = int(MyMlx.screen_height / 2 - self.cells_img.height / 2)
        MyMlx.put_image_to_window(self.cells_img.ptr, x, 60)
