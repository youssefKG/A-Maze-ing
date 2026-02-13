"""Top-level renderer that wires together state, images, and controls.

This module prepares the maze state, initializes the cell image buffer
and control panel, and ultimately starts the MLX loop.
"""

from maze.maze_state import MazeState
from my_mlx.my_mlx import MyMlx
from controll_pannel.controll_pannel import ControllPannel
from renderer.images.cellImg import CellsImage
from parser.Parser import Parser
from mazegen.MazeGenerator import MazeGenerator


class Renderer:
    """Configure the maze rendering pipeline and start the main loop."""

    def __init__(self, maze_gen: MazeGenerator, parser: Parser) -> None:
        """Create a renderer bound to a maze generator and parser.

        The parser provides maze dimensions, entry/exit positions,
        randomness configuration, and output options.
        """
        self.maze_state = MazeState()
        self.maze_gen: MazeGenerator = maze_gen
        (
            self.maze_state.set_vertical_cells(parser.height)
            .set_horizontal_cells(parser.width)
            .set_cells_grid()
            .set_entry_cell(parser.entry)
            .set_exit_cell(parser.exit)
            .set_is_perfect(parser.perfect)
            .set_seed(parser.seed)
            .set_output_file(parser.output_file)
        )
        if not (
            self.maze_state.vertical_cells > 5
            and self.maze_state.horizontal_cells > 7
        ):
            print(
                "Cannot draw 42 in center in maze with width ",
                self.maze_state.vertical_cells,
                " and height ",
                self.maze_state.horizontal_cells,
            )
        self.cells_img = CellsImage()
        self.cells_img.set_cells(
            self.maze_state.vertical_cells, self.maze_state.horizontal_cells
        ).set_cell_height().set_cell_width()
        self.controll_pannel = ControllPannel(self.maze_gen)

    def render(self) -> None:
        """Enter the MLX event loop to display and animate the maze."""
        MyMlx.loop()
