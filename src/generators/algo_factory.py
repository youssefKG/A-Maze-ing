from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator
from renderer.images.cellImg import CellsImage
from solver.bfs_solver import BfsSolver

class AlgoFactory:
    vertical_cells = 20
    horizontal_cells = 20
    entry_cell = 12
    exit_cell = 42
    cells_img = CellsImage(vertical_cells, horizontal_cells)
    
    @classmethod
    def create(cls, name: str | None=None) -> MazeGeneratorAlgo:
        algo_generator = MazeGeneratorAlgo()
        if name == "wilson":
            algo_generator = WilsonMazeGenerator()
        elif name == "dfs":
            algo_generator = DfsMazeGenerator()
        elif name == "dfs":
            algo_generator = DfsMazeGenerator()
        return (
            algo_generator.set_cells_img(cls.cells_img)
            .set_vertical_cells(cls.vertical_cells)
            .set_horizontal_cells(cls.horizontal_cells)
        )

    @classmethod
    def create_solver(cls, name: str) -> None:
        if name == "bfs":
            return (
                    BfsSolver()
                    .set_cells_img(cls.cells_img)
                    .set_vertical_cells(cls.vertical_cells)
                    .set_entry_cell(cls.entry_cell)
                    .set_entry_cell(cls.exit_cell)
                    )
