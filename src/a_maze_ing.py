from mlx.mlx import Mlx
from renderer import renderer
from renderer.image.image import Image
from renderer.renderer import Renderer

class Amazeing:
    def __init__(self) -> None:
        self.mlx = Mlx()
        self.mlx_ptr = self.mlx.mlx_init()
        self.renderer = Renderer(self.mlx, self.mlx_ptr)

def main():
    amazeing = Amazeing()
    amazeing.renderer.render()

main()
#     m = Mlx()
#     mlx_ptr = m.mlx_init()
#     win_ptr = m.mlx_new_window(mlx_ptr, window_height, widow_width, "hello world")
#     m.mlx_clear_window(mlx_ptr, win_ptr)
#     m.mlx_hook(win_ptr, 33, 0, gere_close, None)
#     img = Image(mlx_ptr, 800, 800)qsew
#     m.mlx_put_image_to_window(mlx_ptr, win_ptr, img.image_ptr, 0, 0)
#
# m = Mlx()
# mlx_ptr = m.mlx_init()
# win_ptr = m.mlx_new_window(mlx_ptr, 500, 500, "win title")
# m.mlx_clear_window(mlx_ptr, win_ptr)
# m.mlx_string_put(mlx_ptr, win_ptr, 20, 20, 255, "Hello PyMlx!")
# (ret, w, h) = m.mlx_get_screen_size(mlx_ptr)
# print(f"Got screen size: {w} x {h} .")
#
# stuff = [1, 2]
# m.mlx_mouse_hook(win_ptr, mymouse, None)
# m.mlx_key_hook(win_ptr, mykey, stuff)
#
# m.mlx_loop(mlx_ptr)
