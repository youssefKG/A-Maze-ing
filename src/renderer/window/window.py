from generators.mazeGenerator import MazeGenerator
from mlx.mlx.mlx import Mlx
from maze.cell import * 


class Window:
    def __init__(self, mlx: Mlx, mlx_ptr, screen_params) -> None: 
        self.mlx = mlx
        self.width, self.height, self.title = screen_params
        self.mlx_ptr = mlx_ptr
        self.ptr = self.mlx.mlx_new_window(self.mlx_ptr, self.width, self.height, self.title)
        self.maze_generator = MazeGenerator(self.mlx, self.mlx_ptr, self.ptr, (self.width, self.height))
        self.mlx.mlx_key_hook(self.ptr, self.mykey, [1, 2])
        self.maze_generator.generate("dfs")

    def mykey(self, keynum, _):
        if keynum == 65307:
            self.mlx.mlx_loop_exit(self.mlx_ptr)
