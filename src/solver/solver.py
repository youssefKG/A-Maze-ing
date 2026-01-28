from abc import ABC
from maze.cell import Cell

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

    def set_cells_grid(self, cells_grid: list[list[Cell]]):
        self.cells_grid = cells_grid
        return self

    def find_path(self):
        print("hello")
        pass

    def set_cells_grid(self, cells_grid: list[list[Cell]]) -> None:
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
