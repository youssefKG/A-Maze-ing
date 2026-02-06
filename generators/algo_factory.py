from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator
from maze.maze_state import MazeState
from renderer.images.cellImg import CellsImage
from solver.bfs_solver import BfsSolver
from solver.solver import Solver


class AlgoFactory:
    generator_name = "default"

    @classmethod
    def create(cls, name: str | None = None) -> MazeGeneratorAlgo:
        if name:
            cls.generator_name = name
        algo_generator = MazeGeneratorAlgo()
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
        return solver
