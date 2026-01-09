from renderer.images.cellImg import CellsImage


class MazeGenerator:
    def __init__(self, mlx, mlx_ptr, win_ptr, height: int, width:int) -> None:
        self.mlx = mlx
        self.mlx_ptr = mlx_ptr
        self.width = self.width
        self.height = height
        self.cell_width = self.get_cell_width()
        self.cell_height = self.get_cell_height()
        self.vertical_cells = 40
        self.horizontal_cells = 40
        self.win_ptr = win_ptr
        self.cell_img = CellsImage(self.mlx, self.mlx_ptr, self.width,
                                   self.height, self.cell_width,
                                   self.cell_height)
    
    def get_cell_width(self):
        return int(self.width / self.vertical_cells - 4)

    def get_cell_height(self):
        return int(self.height / self.horizontal_cells - 4)
