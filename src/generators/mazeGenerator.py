from generators.wilson_maze_generator import WilsonMazeGenerator
from maze.cell import Cell
from mlx.mlx.mlx import Mlx
from renderer.images.cellImg import CellsImage
from generators.dfs_maze_generator import DfsMazeGenerator

class MazeGenerator:
    def __init__(self, mlx: Mlx, mlx_ptr: int, win_ptr) -> None:
        self.mlx = mlx
        self.mlx_ptr = mlx_ptr
        self.win_ptr = win_ptr
        self.vertical_cells = 15
        self.horizontal_cells = 15
        self.cells_img = CellsImage(self.mlx, self.mlx_ptr, self.vertical_cells, self.horizontal_cells)
        self.cells_grid = []
        self.init_grid_cells()
        self.dfs_maze_generator = DfsMazeGenerator(
               self.mlx,
               self.mlx_ptr,
               self.win_ptr,
               self.cells_img,
               self.cells_grid,
               self.vertical_cells,
               self.horizontal_cells
               )
        self.wilson_maze_generator = WilsonMazeGenerator(
                self.mlx,
                self.mlx_ptr,
                self.win_ptr,
                self.cells_img,
                self.cells_grid,
                self.vertical_cells,
                self.horizontal_cells
                )

    def init_grid_cells(self):
        for i in range(self.vertical_cells):
            row = []
            for j in range(self.horizontal_cells):
                row.append(Cell(j, i))
            self.cells_grid.append(row)
        i = 0
        while i < self.vertical_cells:
            j = 0
            while j < self.horizontal_cells:
                self.cells_img.draw_cell(self.cells_grid[i][j])
                j += 1
            i += 1
        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0
        )
        if self.vertical_cells > 5 and self.horizontal_cells > 7:
            self.draw_42()

    def draw_42(self):
        y = int(((self.vertical_cells) / 2) - 2)
        x = int(((self.horizontal_cells) / 2) - 3)
        # draw 4
        for i in range(y, y + 3):
            self.cells_grid[i][x].is_visited = True
            self.cells_grid[i][x].is_42_cell =  True
            self.cells_img.draw_cell(self.cells_grid[i][x], 0xFFF00000)
        for i in range(x + 1, x + 3):
            self.cells_grid[y + 2][i].is_visited = True
            self.cells_grid[y + 2][i].is_42_cell =  True
            self.cells_img.draw_cell(self.cells_grid[y + 2][i], 0xFFF00000)
        for i in range(y + 3, y + 5):
            self.cells_grid[i][x + 2].is_visited = True
            self.cells_grid[i][x + 2].is_42_cell =  True
            self.cells_img.draw_cell(self.cells_grid[i][x + 2], 0xFFF00000)
        # Draw 2
        for i in range(x + 4, x + 7):
            self.cells_grid[y][i].is_visited = True
            self.cells_img.draw_cell(self.cells_grid[y][i], 0xFFF00000)
        for i in range(y + 1, y + 3):
            self.cells_grid[i][x + 6].is_visited = True
            self.cells_grid[i][x + 6].is_42_cell =  True
            self.cells_img.draw_cell(self.cells_grid[i][x + 6], 0xFFF00000)
        for i in range(x + 4, x + 7):
            self.cells_grid[y + 2][i].is_visited = True
            self.cells_grid[y + 2][i].is_42_cell =  True
            self.cells_img.draw_cell(self.cells_grid[y + 2][i], 0xFFF00000)
        for i in range(y + 3, y + 5):
            self.cells_grid[i][x + 4].is_visited = True
            self.cells_grid[i][x + 4].is_42_cell =  True
            self.cells_img.draw_cell(self.cells_grid[i][x + 4], 0xFFF00000)
        for i in range(y + 3, y + 5):
            self.cells_grid[i][x + 4].is_visited = True
            self.cells_grid[i][x + 4].is_42_cell =  True
            self.cells_img.draw_cell(self.cells_grid[i][x + 4], 0xFFF00000)
        for i in range(x + 4, x + 7):
            self.cells_grid[y + 4][i].is_visited = True
            self.cells_grid[y + 4][i].is_42_cell =  True
            self.cells_img.draw_cell(self.cells_grid[y + 4][i], 0xFFF00000)

    def generate(self):
        self.dfs_maze_generator.generate()
        # self.wilson_maze_generator.generate()
