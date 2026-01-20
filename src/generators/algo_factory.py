from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator

class AlgoFactory:
    def create(self, name):
        if name == "wilson":
                return WilsonMazeGenerator()
        elif name == "dfs":
                return DfsMazeGenerator()
        return MazeGeneratorAlgo()
