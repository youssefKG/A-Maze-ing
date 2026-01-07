from mlx.mlx import Mlx
from Exceptions.ImageException import ImageException
from maze.cell import Cell

import os

class Image:
    def __init__(self, mlx_ptr, width, height):
        self.mlx_ptr = mlx_ptr
        self.mlx = Mlx()
        self.mlx_ptr = mlx_ptr
        self.path = \
                os.path.abspath(
                        os.path.join(
                            os.path.dirname(__file__),
                            "../../assets/samuria.xpm")
                        )
        self.img_ptr = None

    def resize_image(self):
        print("hello")
        (orig_img, orig_width, orig_height) = \
                self.mlx.mlx_xpm_file_to_image(self.mlx_ptr, self.path)
        if orig_img is not None:
            raise ImageException(f"Cannot load image from path {self.path}")
        (img_addr, bit_per_pixel, size_line, format) = self.mlx.mlx_get_data_addr(orig_img)
        print(bit_per_pixel, size_line, format)



class CellImage:
    def __init_e(self, mlx: Mlx, mlx_ptr, cell: Cell ) -> None:
        self.mlx = mlx
        self.mlx_ptr =  mlx_ptr
        self.cell = cell
        self.ptr = self.mlx.mlx_new_image(self.mlx_ptr, self.cell.width, self.cell.height)
        (self.data, self.bpp,  self.sl, self.format) = self.mlx.mlx_get_data_addr(self.ptr)
