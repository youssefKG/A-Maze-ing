"""Abstract base class for maze generation algorithms.

Concrete generators inherit from :class:`MazeGeneratorAlgo` and reuse
its grid drawing, wall manipulation, and helper utilities while
providing their own generation strategy.
"""

from abc import ABC
from typing import Any
from maze.cell import Cell
from my_mlx.my_mlx import MyMlx
from random import choice
from maze.maze_state import MazeState
from renderer.images.cellImg import CellsImage
from renderer.themes import Theme


class MazeGeneratorAlgo(ABC):
    """Shared functionality for animated maze generation algorithms."""

    def __init__(self) -> None:
        """Initialize shared maze generator state objects."""
        self.current_cell = None
        self.frames = 0
        self.is_finished = False
        self.maze_state = MazeState()
        self.is_running = False

    def generate(self) -> None:
        """Prepare the maze grid for generation and initial drawing."""
        self.is_running = True
        vertical_cells = self.maze_state.vertical_cells
        horizontal_cells = self.maze_state.horizontal_cells
        i = 0
        while i < self.maze_state.vertical_cells:
            j = 0
            while j < horizontal_cells:
                self.cells_img.draw_cell(
                    self.maze_state.cells_grid[i][j], Theme.background
                )
                j += 1
            i += 1
        if vertical_cells > 6 and horizontal_cells > 8:
            self.draw_42()
        self.put_cells_img_to_window()

    def put_cells_img_to_window(self) -> None:
        """Blit the cell image buffer to the window, centered on screen."""
        x = int((MyMlx.screen_width) / 2 - self.cells_img.width / 2)
        y = int(MyMlx.screen_height / 2 - self.cells_img.height / 2)
        MyMlx.put_image_to_window(self.cells_img.ptr, x, y + 20)

    def remove_wall(self, current_cell: Cell, next_cell: Cell) -> None:
        """Remove the wall between two neighboring cells and redraw it."""
        if next_cell:
            x = current_cell.x - next_cell.x
            y = current_cell.y - next_cell.y
            if y == 1:
                current_cell.north = False
                next_cell.south = False
            if y == -1:
                current_cell.south = False
                next_cell.north = False
            if x == 1:
                current_cell.west = False
                next_cell.east = False
            if x == -1:
                current_cell.east = False
                next_cell.west = False
        self.cells_img.draw_wall_between_two_cell(
            current_cell, next_cell, Theme.background
        )

    def check_neighbors(self) -> Any:
        """Return a random unvisited neighbor of the current cell.

        Returns ``None`` when no suitable neighbor exists.
        """
        if self.current_cell:
            x = self.current_cell.x
            y = self.current_cell.y
            neighbors = []
            if y - 1 >= 0:
                north = self.maze_state.cells_grid[y - 1][x]
                if not north.is_visited:
                    neighbors.append(north)
            if y + 1 < self.maze_state.vertical_cells:
                south = self.maze_state.cells_grid[y + 1][x]
                if not south.is_visited:
                    neighbors.append(south)
            if x + 1 < self.maze_state.horizontal_cells:
                east = self.maze_state.cells_grid[y][x + 1]
                if not east.is_visited:
                    neighbors.append(east)
            if x - 1 >= 0:
                west = self.maze_state.cells_grid[y][x - 1]
                if not west.is_visited:
                    neighbors.append(west)
            if len(neighbors) != 0:
                return choice(neighbors)
        return None

    def redraw_maze(self) -> None:
        """Redraw the whole maze using the current theme settings."""
        for row_cells in self.maze_state.cells_grid:
            for cell in row_cells:
                if cell.is_42_cell:
                    self.cells_img.draw_cell(cell, Theme.cell_42)
                else:
                    self.cells_img.draw_cell(cell, Theme.background)
        if self.is_finished:
            self.draw_entry_exit_cells()
        self.put_cells_img_to_window()

    def draw_42(self) -> None:
        """Draw a “42” pattern in the maze for decoration."""
        y = int(((self.maze_state.vertical_cells) / 2) - 2)
        x = int(((self.maze_state.horizontal_cells) / 2) - 3)
        cells_grid = self.maze_state.cells_grid

        # drw 4
        for i in range(y, y + 3):
            self.draw_cell_42(cells_grid[i][x])
        for i in range(x + 1, x + 3):
            self.draw_cell_42(cells_grid[y + 2][i])
        for i in range(y + 3, y + 5):
            self.draw_cell_42(cells_grid[i][x + 2])

        # Draw 2
        for i in range(x + 4, x + 7):
            self.draw_cell_42(cells_grid[y][i])
        for i in range(y + 1, y + 3):
            self.draw_cell_42(cells_grid[i][x + 6])
        for i in range(x + 4, x + 7):
            self.draw_cell_42(cells_grid[y + 2][i])
        for i in range(y + 3, y + 5):
            self.draw_cell_42(cells_grid[i][x + 4])
        for i in range(y + 3, y + 5):
            self.draw_cell_42(cells_grid[i][x + 4])
        for i in range(x + 4, x + 7):
            self.draw_cell_42(cells_grid[y + 4][i])

    def draw_cell_42(self, cell: Cell) -> None:
        """Mark a cell as part of the 42 logo and draw it."""
        cell.is_visited = True
        cell.is_42_cell = True
        self.cells_img.draw_cell(cell, Theme.cell_42)

    def run(self) -> None:
        """Mark the generator as running."""
        self.is_running = True

    def stop(self) -> None:
        """Mark the generator as stopped."""
        self.is_running = False

    def set_cells_img(self, cells_img: CellsImage) -> Any:
        """Attach the cell image buffer and return ``self`` for chaining."""
        self.cells_img = cells_img
        return self

    def count_cell_walls(self, cell: Cell) -> int:
        """Count how many walls around a cell are still present."""
        count = 0
        if cell.north:
            count += 1
        if cell.south:
            count += 1
        if cell.east:
            count += 1
        if cell.west:
            count += 1
        return count

    def break_wall(self, cell: Cell) -> None:
        """Break a random valid wall around a cell in imperfect mazes."""

        vertical_cells = self.maze_state.vertical_cells
        horizontal_cells = self.maze_state.horizontal_cells
        walls = self.get_valid_walls(cell)
        target_wall = choice(walls)
        x, y = (cell.x, cell.y)
        next_cell = cell

        match target_wall:
            case "north" if y - 1 >= 0:
                next_cell = self.maze_state.cells_grid[y - 1][x]
            case "south" if y + 1 < vertical_cells:
                next_cell = self.maze_state.cells_grid[y + 1][x]
            case "east" if x + 1 < horizontal_cells:
                next_cell = self.maze_state.cells_grid[y][x + 1]
            case "west" if x - 1 >= 0:
                next_cell = self.maze_state.cells_grid[y][x - 1]
        if next_cell is not cell and not next_cell.is_42_cell:
            self.remove_wall(cell, next_cell)
            self.cells_img.draw_wall_between_two_cell(
                cell,
                next_cell,
                Theme.background,
            )

    def get_valid_walls(self, cell: Cell) -> list[str]:
        """Return a list of wall directions that can be removed safely."""
        valid_walls = []
        height = self.maze_state.vertical_cells
        width = self.maze_state.horizontal_cells
        if cell.north:
            if cell.y != 0:
                valid_walls.append("north")
        if cell.east:
            if cell.x != width - 1:
                valid_walls.append("east")
        if cell.south:
            if cell.y != height - 1:
                valid_walls.append("south")
        if cell.west:
            if cell.x != 0:
                valid_walls.append("west")
        return valid_walls

    def break_wall_in_imperfect(self) -> None:
        """Introduce a single extra opening to make the maze imperfect."""
        if self.maze_state.is_perfect:
            return
        for y in range(self.maze_state.vertical_cells):
            for x in range(self.maze_state.horizontal_cells):
                cell = self.maze_state.cells_grid[y][x]
                if not cell.is_42_cell:
                    count_walls = self.count_cell_walls(cell)
                    if count_walls == 3:
                        self.break_wall(cell)
                        self.cells_img.clear_image()
                        self.redraw_maze()
                        return

    def draw_entry_exit_cells(self) -> None:
        """Highlight the entry and exit cells using the theme colors."""
        entry_cell = self.maze_state.get_entry_cell()
        exit_cell = self.maze_state.get_exit_cell()
        self.cells_img.draw_cell(entry_cell, Theme.entry_cell)
        self.cells_img.draw_cell(exit_cell, Theme.exit_cell)
        self.put_cells_img_to_window()
