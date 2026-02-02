from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator
from maze.maze_state import MazeState
from renderer.images.cellImg import CellsImage
from solver.bfs_solver import BfsSolver
from solver.solver import Solver

class AlgoFactory:
    horizontal_cells = 2
    vertical_cells = 2
    entry_cell = (0, 1)
    exit_cell = (0, 0)
    cells_img = CellsImage(vertical_cells, horizontal_cells)
    
    @classmethod
    def create(cls, name: str | None=None) -> MazeGeneratorAlgo:
        maze_state = MazeState()
        (maze_state
         .set_vertical_cells(cls.vertical_cells)
         .set_horizontal_cells(cls.horizontal_cells)
         .set_cells_grid()
         .set_entry_cell(cls.entry_cell).
         set_exit_cell(cls.exit_cell)
         )
        algo_generator = MazeGeneratorAlgo()
        if name == "wilson":
            algo_generator = WilsonMazeGenerator()
        elif name == "dfs":
            algo_generator = DfsMazeGenerator()
        return algo_generator.set_cells_img(cls.cells_img)

    @classmethod
    def create_solver(cls, name: str):
        solver = Solver()
        if name == "bfs":
            solver = BfsSolver()
        return solver.set_cells_img(cls.cells_img)
