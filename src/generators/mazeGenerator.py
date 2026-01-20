from maze.cell import Cell
from mlx.mlx.mlx import Mlx
from renderer.images.cellImg import CellsImage
from generators.algo_factory import AlgoFactory
from renderer.colors import Colors
from my_mlx.my_mlx import MyMlx


class MazeGenerator:
    def __init__(self) -> None:
        self.vertical_cells = 16
        self.horizontal_cells = 16

        self.cells_img = CellsImage(self.vertical_cells, self.horizontal_cells)

    def init_grid_cells(self):
        self.cells_grid = []
        for i in range(self.vertical_cells):
            row = []
            for j in range(self.horizontal_cells):
                row.append(Cell(j, i))
            self.cells_grid.append(row)
        i = 0
        while i < self.vertical_cells:
            j = 0
            while j < self.horizontal_cells:
                self.cells_img.draw_cell(self.cells_grid[i][j], Colors.GRAY)
                j += 1
            i += 1
        if self.vertical_cells > 5 and self.horizontal_cells > 7:
            self.draw_42()

    def draw_42(self, color=Colors.YELLOW):
        y = int(((self.vertical_cells) / 2) - 2)
        x = int(((self.horizontal_cells) / 2) - 3)
        # draw 4
        for i in range(y, y + 3):
            self.cells_grid[i][x].is_visited = True
            self.cells_grid[i][x].is_42_cell = True
            self.cells_img.draw_cell(self.cells_grid[i][x], color)
        for i in range(x + 1, x + 3):
            self.cells_grid[y + 2][i].is_visited = True
            self.cells_grid[y + 2][i].is_42_cell = True
            self.cells_img.draw_cell(self.cells_grid[y + 2][i], color)
        for i in range(y + 3, y + 5):
            self.cells_grid[i][x + 2].is_visited = True
            self.cells_grid[i][x + 2].is_42_cell = True
            self.cells_img.draw_cell(self.cells_grid[i][x + 2], color)
        # Draw 2
        for i in range(x + 4, x + 7):
            self.cells_grid[y][i].is_visited = True
            self.cells_grid[y][i].is_42_cell = True
            self.cells_img.draw_cell(self.cells_grid[y][i], color)
        for i in range(y + 1, y + 3):
            self.cells_grid[i][x + 6].is_visited = True
            self.cells_grid[i][x + 6].is_42_cell = True
            self.cells_img.draw_cell(self.cells_grid[i][x + 6], color)
        for i in range(x + 4, x + 7):
            self.cells_grid[y + 2][i].is_visited = True
            self.cells_grid[y + 2][i].is_42_cell = True
            self.cells_img.draw_cell(self.cells_grid[y + 2][i], color)
        for i in range(y + 3, y + 5):
            self.cells_grid[i][x + 4].is_visited = True
            self.cells_grid[i][x + 4].is_42_cell = True
            self.cells_img.draw_cell(self.cells_grid[i][x + 4], color)
        for i in range(y + 3, y + 5):
            self.cells_grid[i][x + 4].is_visited = True
            self.cells_grid[i][x + 4].is_42_cell = True
            self.cells_img.draw_cell(self.cells_grid[i][x + 4], color)
        for i in range(x + 4, x + 7):
            self.cells_grid[y + 4][i].is_visited = True
            self.cells_grid[y + 4][i].is_42_cell = True
            self.cells_img.draw_cell(self.cells_grid[y + 4][i], color)

    def generate(self, algo_name):
        algo = AlgoFactory().create(algo_name)
        self.init_grid_cells()
        algo.set_cells_img(self.cells_img).set_cells_grid(
            self.cells_grid
        ).set_vertical_cells(
            self.vertical_cells
        ).set_horizontal_cells(
            self.horizontal_cells
        ).generate()
        return algo
