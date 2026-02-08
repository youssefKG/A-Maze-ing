from my_mlx.my_mlx import MyMlx


class Image:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.ptr = MyMlx.new_image(self.width + 10, self.height + 10)
        self.data, self.bpp, self.sl, self.format = MyMlx.get_data_addr(
            self.ptr
        )
        for i in range(0, len(self.data), 4):
            self.data[i:i + 4] = (0x0000000).to_bytes(4, "little")

    def put_pixel(self, x: int, y: int, color: int) -> None:
        offset = int((y * self.sl) + (x * (self.bpp / 8)))
        self.data[offset:offset + 4] = (color).to_bytes(4, "little")
