"""Background image loader and helper for maze rendering."""

from my_mlx.my_mlx import MyMlx
import os


class BackgroundImg:
    """Load and display a background image using MyMlx."""

    def __init__(self, filename: str, format_type: str) -> None:
        """Load an image file from the assets directory.

        Parameters
        ----------
        filename:
            Name of the image file stored under the assets folder.
        format_type:
            File format indicator (currently ``"xpm"`` or ``"png"``).
        """
        self.ptr = None
        self.abs_path = os.path.abspath(".") + "/assets/" + filename
        if format_type == "xpm":
            self.ptr, self.width, self.height = MyMlx.xpm_file_to_image(
                self.abs_path
            )
        elif format_type == "png":
            self.ptr, self.width, self.height = MyMlx.png_file_to_image(
                self.abs_path
            )

    def put_image_to_window(self) -> None:
        """Draw the background image at the origin if it was loaded."""
        if self.ptr is not None:
            MyMlx.put_image_to_window(self.ptr, 0, 0)
