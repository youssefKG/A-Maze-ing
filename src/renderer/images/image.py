from mlx.mlx import Mlx

class Image:
    def __init__(self, mlx: Mlx, mlx_ptr, width=1200, height=1200) -> None:
        self.mlx = mlx
        self.width = width
        self.height = height
        self.mlx_ptr =  mlx_ptr
        self.ptr = self.mlx.mlx_new_image(self.mlx_ptr, self.width, self.height)
        (self.data, self.bpp, self.sl, self.format) = \
                self.mlx.mlx_get_data_addr(self.ptr)

    def put_pixel(self, x, y, color):
        offset = (y * self.sl) + (x * 4) 
        self.data[offset: offset + 4] = (color).to_bytes(4, 'little')
