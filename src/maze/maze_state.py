from typing import Self
from maze.cell import Cell


class MazeState:
    _instance = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_vertical_cells(self, vertical_cells: int) -> Self:
        self.vertical_cells = vertical_cells
        return self

    def set_horizontal_cells(self, horizontal_cells: int) -> Self:
        self.horizontal_cells = horizontal_cells
        return self

    def set_cells_grid(self) -> Self:
        self.cells_grid = []
        for y in range(self.vertical_cells):
            row = []
            for x in range(self.horizontal_cells):
                row.append(Cell(x, y))
            self.cells_grid.append(row)
        return self

    def set_entry_cell(self, entry_cell: tuple[int, int]) -> Self:
        x, y = entry_cell
        self.entry_cell = self.cells_grid[y][x]
        return self

    def set_exit_cell(self, exit_cell: tuple[int, int]) -> Self:
        x, y = exit_cell
        self.exit_cell = self.cells_grid[y][x]
        return self
