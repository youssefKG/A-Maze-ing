from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator
from maze.maze_state import MazeState
from renderer.images.cellImg import CellsImage
from solver.bfs_solver import BfsSolver
from solver.solver import Solver


class AlgoFactory:
    maze_state = MazeState()

    @classmethod
    def create(cls, name: str | None = None) -> MazeGeneratorAlgo:
        algo_generator = MazeGeneratorAlgo()
        cls.maze_state.set_cells_grid()
        if name == "wilson":
            algo_generator = WilsonMazeGenerator()
        elif name == "dfs":
            algo_generator = DfsMazeGenerator()
        return algo_generator.set_cells_img(CellsImage())

    @classmethod
    def create_solver(cls, name: str) -> Solver:
        solver = Solver()
        if name == "bfs":
            solver = BfsSolver()
        return solver.set_cells_img(CellsImage())
