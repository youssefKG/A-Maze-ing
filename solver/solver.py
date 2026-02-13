"""Abstract base class for maze solvers.

Concrete solver implementations (such as BFS) inherit from
``Solver`` and implement the path-finding and drawing behavior.
"""

from abc import ABC
from maze.maze_state import MazeState
from my_mlx.my_mlx import MyMlx
from renderer.images.cellImg import CellsImage


class Solver(ABC):
    """Shared interface and state for maze solving algorithms."""

    def __init__(self) -> None:
        """Initialize common solver state and references."""
        self.is_finished: bool = False
        self.frames: int = 0
        self.is_running: bool = False
        self.maze_state = MazeState()
        self.cells_img = CellsImage()
        self.is_path_shown: bool = False

    def set_horizontal_cells(self, horizontal_cells: int) -> object:
        """Store the maze width and return ``self`` for chaining."""
        self.horizontal_cells = horizontal_cells
        return self

    def set_vertical_cells(self, vertical_cells: int) -> object:
        """Store the maze height and return ``self`` for chaining."""
        self.vertical_cells = vertical_cells
        return self

    def generate(self) -> None:
        """Start or schedule the solving process (to be overridden)."""
        pass

    def draw_path(self) -> None:
        """Draw the solution path on the maze (to be overridden)."""
        pass

    def hide_path(self) -> None:
        """Hide the solution path (to be overridden)."""
        pass

    def toggle_path(self) -> None:
        """Toggle visibility of the solution path (to be overridden)."""
        pass

    def redraw_maze(self) -> None:
        """Redraw the maze without the solver’s overlay (to be overridden)."""
        pass

    def put_cells_img_to_window(self) -> None:
        """Blit the cells image to the window, centered on screen."""
        x = int(MyMlx.screen_width / 2 - self.cells_img.width / 2)
        y = int(MyMlx.screen_height / 2 - self.cells_img.height / 2)
        MyMlx.put_image_to_window(self.cells_img.ptr, x, y + 20)
