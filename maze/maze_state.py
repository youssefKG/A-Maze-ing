"""Global maze configuration and shared state.

This module exposes a singleton-like :class:`MazeState` used to share
maze dimensions, cell grid, entry/exit positions, and other options
between generators, solvers, and renderers.
"""

from maze.cell import Cell
from typing import Any


class MazeState:
    """Singleton container for maze dimensions and runtime state."""
    _instance = None

    def __new__(cls) -> Any:
        """Return the unique MazeState instance (singleton pattern)."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_vertical_cells(self, vertical_cells: int) -> Any:
        """Set the number of vertical cells and return ``self``."""
        self.vertical_cells = vertical_cells
        return self

    def set_horizontal_cells(self, horizontal_cells: int) -> Any:
        """Set the number of horizontal cells and return ``self``."""
        self.horizontal_cells = horizontal_cells
        return self

    def set_cells_grid(self) -> Any:
        """Allocate the 2D grid of Cell instances and return ``self``."""
        self.cells_grid = []
        for y in range(self.vertical_cells):
            row = []
            for x in range(self.horizontal_cells):
                row.append(Cell(x, y))
            self.cells_grid.append(row)
        return self

    def set_entry_cell(self, entry_cell: tuple[int, int]) -> Any:
        """Configure the maze entry cell by grid coordinates.

        Parameters
        ----------
        entry_cell:
            Tuple ``(x, y)`` selecting the entry position.
        """
        x, y = entry_cell
        self.entry_cell = self.cells_grid[y][x]
        return self

    def set_exit_cell(self, exit_cell: tuple[int, int]) -> Any:
        """Configure the maze exit cell by grid coordinates."""
        x, y = exit_cell
        self.exit_cell = self.cells_grid[y][x]
        return self

    def set_is_perfect(self, is_perfect: bool) -> Any:
        """Mark whether the maze should be perfect (no loops)."""
        self.is_perfect = is_perfect
        return self

    def set_seed(self, seed_value: int) -> Any:
        """Store the random seed associated with this maze."""
        self.seed = seed_value
        return self

    def get_entry_cell(self) -> Cell:
        """Return the current entry cell instance from the grid."""
        x = self.entry_cell.x
        y = self.entry_cell.y
        return self.cells_grid[y][x]

    def get_exit_cell(self) -> Cell:
        """Return the current exit cell instance from the grid."""
        x = self.exit_cell.x
        y = self.exit_cell.y
        return self.cells_grid[y][x]

    def set_output_file(self, filename: str) -> Any:
        """Set the filename used for saving maze output and return ``self``."""
        self.filename = filename
        return self
