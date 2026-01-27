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

    def set_entry_cell(self, entry_cell: int):
        self.entry_cell = entry_cell
        return self

    def set_exit_cell(self, exit_cell: int):
        self.exit_cell = exit_cell
        return self

    def find_path(self):
        print("hello")
        pass
