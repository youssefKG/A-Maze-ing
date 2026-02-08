from my_mlx.my_mlx import MyMlx
import os


class BackgroundImg:
    def __init__(self, filename: str, format_type: str) -> None:
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
        if self.ptr is not None:
            MyMlx.put_image_to_window(self.ptr, 0, 0)
