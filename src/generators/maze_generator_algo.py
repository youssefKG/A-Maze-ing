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

    def generate(self):
        pass



