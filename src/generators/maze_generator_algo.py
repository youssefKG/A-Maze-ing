from abc import ABC
from my_mlx.my_mlx import MyMlx
from renderer.images.image import Image
from random import choice
from maze.cell import Cell
from renderer.colors import Colors

class MazeGeneratorAlgo(ABC):
    def __init__(self):
        self.current_cell = None
        self.frames = 0
        self.is_finished = False
        self.cells_grid = []
        self_is_algo_running = False

    def generate(self) -> None:
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

    def put_cells_img_to_window(self) -> None:
        x = int((MyMlx.screen_width * 0.8) / 2 - self.cells_img.width / 2)
        y = int(MyMlx.screen_height / 2 - self.cells_img.height / 2)
        MyMlx.put_image_to_window(self.cells_img.ptr, x, y)

    def set_horizontal_cells(self, horizontal_cells) -> None:
        self.horizontal_cells = horizontal_cells
        return self

    def set_vertical_cells(self, vertical_cells) -> None:
        self.vertical_cells = vertical_cells
        return self

    def set_cells_img(self, cells_img) -> None:
        self.cells_img = cells_img
        return self

    def set_cells_grid(self, cells_grid) -> None:
        self.cells_grid = cells_grid
        return self

    def set_speed(self, speed) -> None:
        self.speed = speed
        return self

    def remove_wall(self, current_cell, next_cell) -> None:
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

    def check_neighbors(self) -> None:
        if self.current_cell:
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

    def redraw_maze(self) -> None:
        for row_cells in self.cells_grid:
            for cell in row_cells:
                self.cells_img.draw_cell(cell)
        self.put_cells_img_to_window()

    def draw_42(self, color=Colors.YELLOW) -> None:
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
