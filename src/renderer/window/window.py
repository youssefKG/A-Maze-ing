from mlx.mlx.mlx import Mlx
from renderer.image.image import CellImage
from maze.cell import * 

class Window:
    def __init__(self, mlx: Mlx, mlx_ptr, width: int, height: int, title: str) -> None: 
        self.mlx = mlx
        self.widht = width
        self.height = height
        self.title = title
        self.mlx_ptr = mlx_ptr
        self.ptr = self.mlx.mlx_new_window(self.mlx_ptr, self.widht, self.height, self.title)
        cellWall = CellWalls(True, True, True, True)
        cell = Cell(20, 20, cellWall)
        cellImg = CellImage(self.mlx, self.mlx_ptr, cell)
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.ptr, cellImg.ptr, 10, 10)
        self.mlx.mlx_key_hook(self.ptr, self.mykey, [1, 2])
        self.mlx.mlx_hook(self.ptr, 30, 0, self.gere_close, None)

    def mykey(self, keynum, mystuff):
        print(f"Got key {keynum}, and got my stuff back:")
        print(mystuff)
        if keynum == 32:
            self.mlx.mlx_mouse_hook(self.ptr, None, None)
        if keynum == 65307:
            self.mlx.mlx_loop_exit(self.mlx_ptr)

    def gere_close(self, dummy):
        self.mlx.mlx_loop_exit(self.mlx_ptr)

    # Draw a diagonal line
