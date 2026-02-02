from abc import ABC
from my_mlx.my_mlx import MyMlx
from renderer.colors import Colors
from random import choice, seed
from maze.maze_state import MazeState
from renderer.themes import Theme

class MazeGeneratorAlgo(ABC):
    def __init__(self):
        self.current_cell = None
        self.frames = 0
        self.is_finished = False
        self.maze_state = MazeState()
        self.is_running = False
        seed(22)

    def generate(self) -> None:
        self.is_running = True
        i = 0
        while i < self.maze_state.vertical_cells:
            j = 0
            while j < self.maze_state.horizontal_cells:
                self.cells_img.draw_cell(
                        self.maze_state.cells_grid[i][j],
                        Theme.background
                        )
                j += 1
            i += 1
        if self.maze_state.vertical_cells > 5 and self.maze_state.horizontal_cells > 7:
            self.draw_42(Colors.WHITE)
        self.put_cells_img_to_window()

    def put_cells_img_to_window(self) -> None:
        x = int((MyMlx.screen_width * 0.8) / 2 - self.cells_img.width / 2)
        y = int(MyMlx.screen_height / 2 - self.cells_img.height / 2)
        MyMlx.put_image_to_window(self.cells_img.ptr, x, y)

    def set_cells_img(self, cells_img):
        self.cells_img = cells_img
        return self

    def set_speed(self, speed):
        self.speed = speed
        return self

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
        self.cells_img.draw_wall_between_two_cell(
                current_cell,
                next_cell,
                Theme.background
                )

    def check_neighbors(self):
        if self.current_cell:
            x = self.current_cell.x
            y = self.current_cell.y
            neighbors = []
            if y - 1 >= 0:
                north = self.maze_state.cells_grid[y - 1][x]
                if not north.is_visited:
                    neighbors.append(north)
            if y + 1 < self.maze_state.vertical_cells:
                south = self.maze_state.cells_grid[y + 1][x]
                if not south.is_visited:
                    neighbors.append(south)
            if x + 1 < self.maze_state.horizontal_cells:
                east = self.maze_state.cells_grid[y][x + 1]
                if not east.is_visited:
                    neighbors.append(east)
            if x - 1 >= 0:
                west = self.maze_state.cells_grid[y][x - 1]
                if not west.is_visited:
                    neighbors.append(west)
            if len(neighbors) != 0:
                return choice(neighbors)
            return None

    def redraw_maze(self) -> None:
        #self.cells_img.draw_background()
        for row_cells in self.maze_state.cells_grid:
            for cell in row_cells:
                if cell.is_42_cell:
                    self.cells_img.draw_cell(cell, Theme.cell_42)
                else:
                    self.cells_img.draw_cell(cell, Theme.background)

        self.put_cells_img_to_window()

    def draw_42(self, color=Colors.YELLOW) -> None:
        y = int(((self.maze_state.vertical_cells) / 2) - 2)
        x = int(((self.maze_state.horizontal_cells) / 2) - 3)
        # drw 4
        for i in range(y, y + 3):
            self.maze_state.cells_grid[i][x].is_visited = True
            self.maze_state.cells_grid[i][x].is_42_cell = True
            self.cells_img.draw_cell(self.maze_state.cells_grid[i][x], color)
        for i in range(x + 1, x + 3):
            self.maze_state.cells_grid[y + 2][i].is_visited = True
            self.maze_state.cells_grid[y + 2][i].is_42_cell = True
            self.cells_img.draw_cell(self.maze_state.cells_grid[y + 2][i], color)
        for i in range(y + 3, y + 5):
            self.maze_state.cells_grid[i][x + 2].is_visited = True
            self.maze_state.cells_grid[i][x + 2].is_42_cell = True
            self.cells_img.draw_cell(self.maze_state.cells_grid[i][x + 2], color)

        # Draw 2
        for i in range(x + 4, x + 7):
            self.maze_state.cells_grid[y][i].is_visited = True
            self.maze_state.cells_grid[y][i].is_42_cell = True
            self.cells_img.draw_cell(self.maze_state.cells_grid[y][i], color)
        for i in range(y + 1, y + 3):
            self.maze_state.cells_grid[i][x + 6].is_visited = True
            self.maze_state.cells_grid[i][x + 6].is_42_cell = True
            self.cells_img.draw_cell(self.maze_state.cells_grid[i][x + 6], color)
        for i in range(x + 4, x + 7):
            self.maze_state.cells_grid[y + 2][i].is_visited = True
            self.maze_state.cells_grid[y + 2][i].is_42_cell = True
            self.cells_img.draw_cell(self.maze_state.cells_grid[y + 2][i], color)
        for i in range(y + 3, y + 5):
            self.maze_state.cells_grid[i][x + 4].is_visited = True
            self.maze_state.cells_grid[i][x + 4].is_42_cell = True
            self.cells_img.draw_cell(self.maze_state.cells_grid[i][x + 4], color)
        for i in range(y + 3, y + 5):
            self.maze_state.cells_grid[i][x + 4].is_visited = True
            self.maze_state.cells_grid[i][x + 4].is_42_cell = True
            self.cells_img.draw_cell(self.maze_state.cells_grid[i][x + 4], color)
        for i in range(x + 4, x + 7):
            self.maze_state.cells_grid[y + 4][i].is_visited = True
            self.maze_state.cells_grid[y + 4][i].is_42_cell = True
            self.cells_img.draw_cell(self.maze_state.cells_grid[y + 4][i], color)
             
    def run(self):
        self.is_running = True

    def stop(self):
        self.isw_running = False
