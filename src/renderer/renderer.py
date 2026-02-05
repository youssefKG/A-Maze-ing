from maze.maze_state import MazeState
from my_mlx.my_mlx import MyMlx
from controll_pannel.controll_pannel import ControllPannel
from renderer.images.cellImg import CellsImage


class Renderer:
    def __init__(self) -> None:
        self.maze_state = MazeState()
        (
            self.maze_state.set_vertical_cells(10)
            .set_horizontal_cells(10)
            .set_cells_grid()
            .set_entry_cell((0, 0))
            .set_exit_cell((1, 9))
            .set_is_perfect(True)
        )
        self.cells_img = CellsImage()
        self.cells_img.set_cells(
            self.maze_state.vertical_cells, self.maze_state.horizontal_cells
        ).set_cell_height().set_cell_width()
        self.controll_pannel = ControllPannel()

    def render(self) -> None:
        MyMlx.loop()
