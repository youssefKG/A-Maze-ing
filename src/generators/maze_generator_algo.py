from abc import ABC
from renderer.images.image import Image
from random import choice

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
        self.current_cell = None
        self.frames = 0
        self.is_finished = False

    def generate(self):
        pass

    def put_cells_img_to_window(self):
        x = int((self.screen_width * 0.8) / 2 - self.cells_img.width / 2)
        y = int(self.screen_height / 2 - self.cells_img.height / 2)
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr, self.cells_img.ptr, x, 80)

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

    def remove_wall(self, current_cell, next_cell):
        if next_cell:
            x = current_cell.x - next_cell.x
            y = current_cell.y - next_cell.y
            if y == 1:
                current_cell.north = False
                next_cell.south = False
            if y == -1:
                current_cell.south = False
                next_cell.north = False
            if x == 1:
                current_cell.west = False
                next_cell.east = False
            if x == -1:
                current_cell.east = False
                next_cell.west = False

    def check_neighbors(self):
        if (self.current_cell):
            x = self.current_cell.x
            y = self.current_cell.y
            neighbors = []
            if y - 1 >= 0:
                north = self.cells_grid[y - 1][x]
                if not north.is_visited:
                    neighbors.append(north)
            if y + 1 < self.vertical_cells:
                south = self.cells_grid[y + 1][x]
                if not south.is_visited:
                    neighbors.append(south)
            if x + 1 < self.horizontal_cells:
                east = self.cells_grid[y][x + 1]
                if not east.is_visited:
                    neighbors.append(east)
            if x - 1 >= 0:
                west = self.cells_grid[y][x - 1]
                if not west.is_visited:
                    neighbors.append(west)
            if len(neighbors) != 0:
                return choice(neighbors)
            return None

    def redraw_maze(self):
        for row_cells in self.cells_grid:
            for cell in row_cells:
                self.cells_img.draw_cell(cell)
        self.put_cells_img_to_window()
