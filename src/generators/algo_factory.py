from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator
from renderer.images.cellImg import CellsImage

class AlgoFactory:
    vertical_cells = 16
    horizontal_cells = 16
    cells_img = CellsImage(vertical_cells, horizontal_cells)
    
    @classmethod
    def create(cls, name: str):
        print("hello")
        algo_generator = None
        if name == "wilson":
            algo_generator = WilsonMazeGenerator()
        elif name == "dfs":
            print("dfs")
            algo_generator = DfsMazeGenerator()
        if algo_generator is not None:
            return (
                algo_generator.set_cells_img(cls.cells_img)
                .set_vertical_cells(cls.vertical_cells)
                .set_horizontal_cells(cls.horizontal_cells)
            )
        return algo_generator
