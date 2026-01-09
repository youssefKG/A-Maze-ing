from mlx.mlx.mlx import Mlx

from renderer.window.window import Window

class Renderer:
    def __init__(self, mlx: Mlx, mlx_ptr):
        self.mlx = mlx
        self.mlx_ptr = mlx_ptr
        _ ,self.width, self.height = self.mlx.mlx_get_screen_size(self.mlx_ptr)
        self.win = Window(self.mlx, self.mlx_ptr, self.width, self.height, "HELLO WORLD")

    def render(self):
        self.mlx.mlx_loop(self.mlx_ptr)
        self.mlx.mlx_clear_window(self.mlx_ptr, self.win.ptr)
