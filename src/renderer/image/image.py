from mlx.mlx import Mlx
from Exceptions.ImageException import ImageException
from maze.cell import Cell
import os


class CellImage:
    def __init__(self, mlx: Mlx, mlx_ptr, cell: Cell ) -> None:
        self.mlx = mlx
        self.mlx_ptr =  mlx_ptr
        self.cell = cell
        self.ptr = self.mlx.mlx_new_image(self.mlx_ptr, self.cell.width, self.cell.height)
        (self.data, self.bpp, self.sl, self.format) = self.mlx.mlx_get_data_addr(self.ptr)

        for offset in range(0, self.sl * self.cell.width, 4):
            self.data[offset:offset+4] = (0xFFFF0000).to_bytes(4, 'little')

