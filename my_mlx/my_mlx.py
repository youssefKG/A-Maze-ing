"""Thin wrapper around the MLX bindings used by this project.

This module centralizes window creation and common drawing helpers so
the rest of the codebase can interact with MLX through a simple Python
API.
"""

from mlx.mlx import Mlx
from typing import Any


class MyMlx:
    """Convenience facade over the low-level MLX functions."""
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
        """Draw a string at the given window coordinates."""
        cls.mlx.mlx_string_put(cls.mlx_ptr, cls.win_ptr, x, y, color, text)

    @classmethod
    def put_image_to_window(cls, img_ptr: Any, x: int, y: int) -> None:
        """Blit an image to the window at the specified position."""
        cls.mlx.mlx_put_image_to_window(
            cls.mlx_ptr, cls.win_ptr, img_ptr, x, y
        )

    @classmethod
    def clear_window(cls) -> None:
        """Clear the entire window contents."""
        cls.mlx.mlx_clear_window(cls.mlx_ptr, cls.win_ptr)

    @classmethod
    def new_image(cls, width: int, height: int) -> Any:
        """Create a new off-screen image buffer."""
        return cls.mlx.mlx_new_image(cls.mlx_ptr, width, height)

    @classmethod
    def get_data_addr(cls, img_ptr: Any) -> Any:
        """Return the raw data address and metadata for an image."""
        return cls.mlx.mlx_get_data_addr(img_ptr)

    @classmethod
    def loop(cls) -> None:
        """Enter the main MLX event loop."""
        cls.mlx.mlx_loop(cls.mlx_ptr)

    @classmethod
    def loop_hook(cls, callback: Any, data: Any) -> None:
        """Register a callback to be called each loop iteration."""
        cls.mlx.mlx_loop_hook(cls.mlx_ptr, callback, data)

    @classmethod
    def loop_exit(cls) -> None:
        """Request exit from the MLX main loop."""
        cls.mlx.mlx_loop_exit(cls.mlx_ptr)

    @classmethod
    def key_hook(cls, callback: Any, data: Any) -> None:
        """Register a key press callback for the current window."""
        cls.mlx.mlx_key_hook(cls.win_ptr, callback, data)

    @classmethod
    def xpm_file_to_image(cls, filename: str) -> Any:
        """Load an XPM image file into an MLX image object."""
        return cls.mlx.mlx_xpm_file_to_image(cls.mlx_ptr, filename)

    @classmethod
    def png_file_to_image(cls, filename: str) -> Any:
        """Load a PNG image file into an MLX image object."""
        return cls.mlx.mlx_png_file_to_image(cls.mlx_ptr, filename)
