from abc import ABC

class MazeGeneratorAlgo(ABC):
    def __init__(
        self,
        mlx,
        mlx_ptr,
        win_ptr,
    ):
        self.mlx = mlx
        self.mlx_ptr = mlx_ptr
        self.win_ptr = win_ptr

    def generate(self):
        pass

    def put_cells_img_to_window(self):
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0)

    def set_horizontal_cells(self, horizontal_cells):
        self.horizontal_cells = horizontal_cells
        return self

    def set_vertical_cells(self, vertical_cells):
        self.vertical_cells = vertical_cells
        return self
    
    def set_screen_dimentions(self, width, height):
        self.screen_width = width
        self.screen_height = height
        return self

    def set_cells_img(self, cells_img):
        self.cells_img = cells_img
        return self

    def set_cells_grid(self, cells_grid):
        self.cells_grid = cells_grid
        return self

    def set_speed(self, speed): 
        self.speed = speed

