from mlx.mlx import Mlx
from typing import Any


class MyMlx:
    mlx = Mlx()
    mlx_ptr = mlx.mlx_init()
    _, screen_width_temp, screen_height = mlx.mlx_get_screen_size(mlx_ptr)
    screen_width: int = int(screen_width_temp * 0.7)
    screen_height = int(screen_height * 0.8)
    win_ptr = mlx.mlx_new_window(
        mlx_ptr, screen_width, screen_height, "A-Maze-ing"
    )

    @classmethod
    def put_string(cls, text: str, x: int, y: int, color: int) -> None:
        cls.mlx.mlx_string_put(cls.mlx_ptr, cls.win_ptr, x, y, color, text)

    @classmethod
    def put_image_to_window(cls, img_ptr: Any, x: int, y: int) -> None:
        cls.mlx.mlx_put_image_to_window(
            cls.mlx_ptr, cls.win_ptr, img_ptr, x, y
        )

    @classmethod
    def clear_window(cls) -> None:
        cls.mlx.mlx_clear_window(cls.mlx_ptr, cls.win_ptr)

    @classmethod
    def new_image(cls, width: int, height: int) -> Any:
        return cls.mlx.mlx_new_image(cls.mlx_ptr, width, height)

    @classmethod
    def get_data_addr(cls, img_ptr: Any) -> Any:
        return cls.mlx.mlx_get_data_addr(img_ptr)

    @classmethod
    def loop(cls) -> None:
        cls.mlx.mlx_loop(cls.mlx_ptr)

    @classmethod
    def loop_hook(cls, callback: Any, data: Any) -> None:
        cls.mlx.mlx_loop_hook(cls.mlx_ptr, callback, data)

    @classmethod
    def loop_exit(cls) -> None:
        cls.mlx.mlx_loop_exit(cls.mlx_ptr)

    @classmethod
    def key_hook(cls, callback: Any, data: Any) -> None:
        cls.mlx.mlx_key_hook(cls.win_ptr, callback, data)

    @classmethod
    def xpm_file_to_image(cls, filename: str) -> tuple[Any, int, int]:
        return cls.mlx.mlx_xpm_file_to_image(cls.mlx_ptr, filename)

    @classmethod
    def png_file_to_image(cls, filename: str) -> tuple[Any, int, int]:
        return cls.mlx.mlx_png_file_to_image(cls.mlx_ptr, filename)
