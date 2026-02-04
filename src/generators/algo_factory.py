from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator
from maze.maze_state import MazeState
from parser.Parser import Parser
from renderer.images.cellImg import CellsImage
from solver.bfs_solver import BfsSolver
from solver.solver import Solver
from sys import argv


class AlgoFactory:
    horizontal_cells: int = 30
    vertical_cells: int = 30
    entry_cell: tuple[int, int] = (0, 19)
    exit_cell: tuple[int, int] = (0, 99)
    cells_img = CellsImage(vertical_cells, horizontal_cells)

    @classmethod
    def create(cls, name: str | None = None) -> MazeGeneratorAlgo:
        parser = Parser(argv[1])
        parser.parse()
        maze_state = MazeState()
        (
            maze_state.set_vertical_cells(100)
            .set_horizontal_cells(100)
            .set_cells_grid()
            .set_entry_cell(cls.entry_cell)
            .set_exit_cell(cls.entry_cell)
        )
        algo_generator = MazeGeneratorAlgo()
        if name == "wilson":
            algo_generator = WilsonMazeGenerator()
        elif name == "dfs":
            algo_generator = DfsMazeGenerator()
        return algo_generator.set_cells_img(cls.cells_img)

    @classmethod
    def create_solver(cls, name: str) -> Solver:
        solver = Solver()
        if name == "bfs":
            solver = BfsSolver()
        return solver.set_cells_img(cls.cells_img)
