from maze.cell import Cell
from typing import Any


class MazeState:
    _instance = None

    def __new__(cls) -> Any:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_vertical_cells(self, vertical_cells: int) -> Any:
        self.vertical_cells = vertical_cells
        return self

    def set_horizontal_cells(self, horizontal_cells: int) -> Any:
        self.horizontal_cells = horizontal_cells
        return self

    def set_cells_grid(self) -> Any:
        self.cells_grid = []
        for y in range(self.vertical_cells):
            row = []
            for x in range(self.horizontal_cells):
                row.append(Cell(x, y))
            self.cells_grid.append(row)
        return self

    def set_entry_cell(self, entry_cell: tuple[int, int]) -> Any:
        x, y = entry_cell
        self.entry_cell = self.cells_grid[y][x]
        return self

    def set_exit_cell(self, exit_cell: tuple[int, int]) -> Any:
        x, y = exit_cell
        self.exit_cell = self.cells_grid[y][x]
        return self

    def set_is_perfect(self, is_perfect: bool) -> Any:
        self.is_perfect = is_perfect
        return self

    def set_seed(self, seed_value: int) -> Any:
        self.seed = seed_value
        return self

    def get_entry_cell(self) -> Cell:
        x = self.entry_cell.x
        y = self.entry_cell.y
        return self.cells_grid[y][x]

    def get_exit_cell(self) -> Cell:
        x = self.exit_cell.x
        y = self.exit_cell.y
        return self.cells_grid[y][x]

    def set_output_file(self, filename: str) -> Any:
        self.filename = filename
        return self
