from mlx.mlx.mlx import Mlx

class MyMlx:
    mlx = Mlx()
    mlx_ptr = mlx.mlx_init()
    _, screen_width, screen_height = mlx.mlx_get_screen_size(mlx_ptr)
    win_ptr = mlx.mlx_new_window(mlx_ptr, screen_width, screen_height, "A-Maze-ing")

    @classmethod
    def put_string(cls, text: str, x: int, y: int, color: str) -> None:
        cls.mlx.mlx_string_put(cls.mlx_ptr, cls.win_ptr, x, y, text, color)

    @classmethod
    def put_image_to_window(cls, img_ptr, x: int, y: int):
        cls.mlx.mlx_put_image_to_window(cls.mlx_ptr, cls.win_ptr, img_ptr, x, y)

    @classmethod
    def clear_window(cls):
        cls.mlx.mlx_clear_window(cls.mlx_ptr, cls.win_ptr)

    @classmethod
    def new_image(cls, width: int, height: int):
        return cls.mlx.mlx_new_image(cls.mlx_ptr, width, height)

    @classmethod
    def get_data_addr(cls, img_ptr):
        return cls.mlx.mlx_get_data_addr(img_ptr)

    @classmethod
    def loop(cls):
        cls.mlx.mlx_loop(cls.mlx_ptr)

    @classmethod
    def loop_hook(cls, callback, data):
        cls.mlx.mlx_loop_hook(cls.mlx_ptr, callback, data)

    @classmethod
    def loop_exit(cls):

        cls.mlx.mlx_loop_exit(cls.mlx_ptr)

    @classmethod
    def key_hook(cls, callback, data):
        cls.mlx.mlx_key_hook(cls.win_ptr, callback, data)
