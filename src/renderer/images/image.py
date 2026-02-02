from mlx.mlx import Mlx
from my_mlx.my_mlx import MyMlx

class Image:
    def __init__(self, width=1200, height=1200) -> None:
        self.width = width
        self.height = height 
        self.ptr = MyMlx.new_image(self.width, self.height)
        (self.data, self.bpp, self.sl, self.format) = \
                MyMlx.get_data_addr(self.ptr)

    def put_pixel(self, x, y, color):
        offset = (y * self.sl) + (x * 4)
        self.data[offset: offset + 4] = (color).to_bytes(4, 'little')
