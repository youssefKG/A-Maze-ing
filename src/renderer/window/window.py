from mlx.mlx.mlx import Mlx
from renderer.images.cellImg import CellsImage
from maze.cell import * 
import random


class Window:
    def __init__(self, mlx: Mlx, mlx_ptr, width: int, height: int, title: str) -> None: 
        self.mlx = mlx
        self.width = width
        self.height = height
        self.title = title
        self.mlx_ptr = mlx_ptr
        self.is_end = False
        print(self.mlx.mlx_get_screen_size(self.mlx_ptr))
        self.ptr = self.mlx.mlx_new_window(
                self.mlx_ptr, self.width, self.height, self.title
                )
        cellRow = 50
        cellCol = 50
        self.mlx.mlx_key_hook(self.ptr, self.mykey, [1, 2])
        self.cellsImg  = CellsImage(self.mlx, self.mlx_ptr, int(900),
                             int(900), 50, 50)
        self.frames = 0
        self.i = 0
        self.j = 0
        self.cellsData = []
        for y in range(cellRow):
            cells_row = []
            for x in range(cellCol):
                north = random.choice([True, False])
                south = random.choice([True, False])
                west = random.choice([True, False])
                east = random.choice([True, False])
                cells_row.append(Cell(north, west, south, east))
            self.cellsData.append(cells_row)
        self.mlx.mlx_loop_hook(self.mlx_ptr, self.render_animation, None)
    def mykey(self, keynum, data):
        if keynum == 65307:
            self.mlx.mlx_loop_exit(self.mlx_ptr)

    def render_animation(self, _):
        self.frames += 1
        if self.frames % 6 != 0:
            return 
        elif  self.j == 50 and self.i < 50:
            self.i += 1
            self.j = 0
        elif self.j < 50 and self.i < 50:
            self.j += 1
        else:
            return
        self.cellsImg.draw_walls(self.j, self.i, self.cellsData[self.i][self.j])
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.ptr, self.cellsImg.ptr, 10, 10)


