from abc import ABC


class MazeGeneratorAlgo(ABC):
    def __init__(
        self,
        mlx,
        mlx_ptr,
        win_ptr,
        cells_img,
        cells_grid,
        vertical_cells,
        horizontal_cells,
        screen_height,
        screen_width,
        speed=0.06,
    ):
        self.mlx = mlx
        self.mlx_ptr = mlx_ptr
        self.cells_img = cells_img
        self.cells_grid = cells_grid
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.win_ptr = win_ptr
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height

    def generate(self):
        pass

    def put_cells_img_to_window(self):
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0)
