
from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator

class AlgoFactory:
    def __init__(self, mlx, mlx_ptr, win_ptr) -> None:
        self.mlx = mlx
        self.mlx_ptr = mlx_ptr
        self.win_ptr = win_ptr
    def create(self, name):
        if name == "wilson":
                return WilsonMazeGenerator(self.mlx, self.mlx_ptr, self.win_ptr)
        elif name == "dfs":
                return DfsMazeGenerator(self.mlx, self.mlx_ptr, self.win_ptr)
        return MazeGeneratorAlgo(self.mlx, self.mlx_ptr, self.win_ptr)
