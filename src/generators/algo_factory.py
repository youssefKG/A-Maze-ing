from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator
from maze.maze_state import MazeState
from renderer.images.cellImg import CellsImage
from solver.bfs_solver import BfsSolver
from solver.solver import Solver

class AlgoFactory:
    vertical_cells = 15
    horizontal_cells = 15
    entry_cell = (2, 13)
    exit_cell = (5, 3)
    cells_img = CellsImage(vertical_cells, horizontal_cells)
    cells_grid = []
    
    @classmethod
    def create(cls, name: str | None=None) -> MazeGeneratorAlgo:
        maze_state = MazeState()
        (maze_state
         .set_vertical_cells(cls.vertical_cells)
         .set_horizontal_cells(cls.horizontal_cells)
         .set_cells_grid()
         .set_exit_cell(cls.exit_cell).
         set_exit_cell(cls.exit_cell)
         )
        algo_generator = MazeGeneratorAlgo()
        if name == "wilson":
            algo_generator = WilsonMazeGenerator()
        elif name == "dfs":
            algo_generator = DfsMazeGenerator()
        return (
            algo_generator
            .set_cells_img(cls.cells_img)
            .set_vertical_cells(cls.vertical_cells)
            .set_horizontal_cells(cls.horizontal_cells)
            .set_cells_grid(cls.cells_grid)
            .set_exit_cell(cls.exit_cell)
            .set_entry_cell(cls.entry_cell)
            )

    @classmethod
    def create_solver(cls, name: str):
        solver = Solver()
        if name == "bfs":
            solver = BfsSolver()
        return (
                solver
                .set_vertical_cells(cls.vertical_cells)
                .set_horizontal_cells(cls.horizontal_cells)
                .set_cells_grid(cls.cells_grid)
                .set_cells_img(cls.cells_img)
                .set_entry_cell(cls.entry_cell)
                .set_exit_cell(cls.exit_cell)
                )
