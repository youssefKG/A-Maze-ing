from sys import argv
from maze.maze_state import MazeState
from my_mlx.my_mlx import MyMlx
from controll_pannel.controll_pannel import ControllPannel
from renderer.images.cellImg import CellsImage
from parser.Parser import Parser


class Renderer:
    def __init__(self) -> None:
        parser = Parser(argv)
        parser.parse()
        self.maze_state = MazeState()
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
            self.maze_state.vertical_cells > 5 and self.maze_state.horizontal_cells > 7
        ):
            print(
                "Cannot 42 in center in maze with width ",
                self.maze_state.vertical_cells,
                " and height ",
                self.maze_state.horizontal_cells,
            )
        self.cells_img = CellsImage()
        self.cells_img.set_cells(
            self.maze_state.vertical_cells, self.maze_state.horizontal_cells
        ).set_cell_height().set_cell_width()
        self.controll_pannel = ControllPannel()

    def render(self) -> None:
        MyMlx.loop()
