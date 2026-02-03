from my_mlx.my_mlx import MyMlx
import os


class BackgroundImg:
    def __init__(self, filename: str, format_type: str) -> None:
        self.ptr = None
        if format_type == "xpm":
            self.ptr, self.width, self.height = MyMlx.xpm_file_to_image(
                os.path.abspath(".") + "/assets/" + filename
            )
        elif format_type == "png":
            self.ptr, self.width, self.height = MyMlx.png_file_to_image(os.path.abspath(".") + "/assets/" + filename)

    def put_image_to_window(self):
        if self.ptr is not None:
            MyMlx.put_image_to_window(self.ptr, 0, 0)
