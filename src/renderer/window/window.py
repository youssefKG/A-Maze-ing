from generators.mazeGenerator import MazeGenerator
from mlx.mlx.mlx import Mlx
from renderer.images import cellImg
from renderer.images.cellImg import CellsImage
from maze.cell import * 


class Window:
    def __init__(self, mlx: Mlx, mlx_ptr, width: int, height: int, title: str) -> None: 
        self.mlx = mlx
        self.width = width
        self.height = height
        self.title = title
        self.mlx_ptr = mlx_ptr
        self.ptr = self.mlx.mlx_new_window(
                self.mlx_ptr, self.width, self.height, self.title
                )
        self.mlx.mlx_key_hook(self.ptr, self.mykey, [1, 2])
        self.maze_generator = MazeGenerator(self.mlx, self.mlx_ptr, self.ptr,
                                       900, 900)
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.ptr,
                                         self.maze_generator.cells_img.ptr, 0, 0)

    def mykey(self, keynum, data):
        if keynum == 65307:
            self.mlx.mlx_loop_exit(self.mlx_ptr)
