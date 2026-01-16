class WilsonMazeGenerator:
    def __init__(
        self,
        mlx: Mlx,
        mlx_ptr: int,
        win_ptr,
        cells_img: CellsImage,
        cells_grid,
        vertical_cells,
        horizontal_cells,
    ):

        super().__init__(
            mlx,
            mlx_ptr,
            win_ptr,
            cells_img,
            cells_grid,
            vertical_cells,
            horizontal_cells,
        )
