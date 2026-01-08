from mlx.mlx import Mlx
from Exceptions.ImageException import ImageException

class Image:
    def __init__(self, mlx: Mlx, mlx_ptr, width: int, height: int) -> None:
        self.mlx = mlx
        self.mlx_ptr =  mlx_ptr
        self.width = width
        self.height = height
        self.ptr = \
                self.mlx.mlx_new_image(
                        self.mlx_ptr,
                        self.width,
                        self.height
                        )
        (self.data, self.bpp, self.sl, self.format) = \
                self.mlx.mlx_get_data_addr(self.ptr)

    def put_pixel(self, x, y):
        offset = (y * self.sl) + (x * 4) 
        self.data[offset: offset + 4] = (0xFFFFFFFF).to_bytes(4, 'little')
