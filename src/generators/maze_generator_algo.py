from abc import ABC
from maze.cell import Cell
from my_mlx.my_mlx import MyMlx
from random import choice, seed
from maze.maze_state import MazeState
from renderer.images.cellImg import CellsImage
from renderer.themes import Theme


class MazeGeneratorAlgo(ABC):
    def __init__(self) -> None:
        self.current_cell = None
        self.frames = 0
        self.is_finished = False
        self.maze_state = MazeState()
        self.is_running = False
        seed(22)

    def generate(self) -> None:
        self.is_running = True
        vertical_cells = self.maze_state.vertical_cells
        horizontal_cells = self.maze_state.horizontal_cells
        i = 0
        while i < self.maze_state.vertical_cells:
            j = 0
            while j < horizontal_cells:
                self.cells_img.draw_cell(
                    self.maze_state.cells_grid[i][j], Theme.background
                )
                j += 1
            i += 1
        if vertical_cells > 5 and horizontal_cells > 7:
            self.draw_42()
        self.put_cells_img_to_window()

    def put_cells_img_to_window(self) -> None:
        x = int((MyMlx.screen_width) / 2 - self.cells_img.width / 2)
        y = int(MyMlx.screen_height / 2 - self.cells_img.height / 2)
        MyMlx.put_image_to_window(self.cells_img.ptr, x, y + 80)

    def remove_wall(self, current_cell: Cell, next_cell: Cell) -> None:
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
            current_cell, next_cell, Theme.background
        )

    def check_neighbors(self) -> Cell | None:
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
        for row_cells in self.maze_state.cells_grid:
            for cell in row_cells:
                if cell.is_42_cell:
                    self.cells_img.draw_cell(cell, Theme.cell_42)
                else:
                    self.cells_img.draw_cell(cell, Theme.background)
        self.put_cells_img_to_window()

    def draw_42(self) -> None:
        y = int(((self.maze_state.vertical_cells) / 2) - 2)
        x = int(((self.maze_state.horizontal_cells) / 2) - 3)
        cells_grid = self.maze_state.cells_grid

        # drw 4
        for i in range(y, y + 3):
            self.draw_cell_42(cells_grid[i][x])
        for i in range(x + 1, x + 3):
            self.draw_cell_42(cells_grid[y + 2][i])
        for i in range(y + 3, y + 5):
            self.draw_cell_42(cells_grid[i][x + 2])

        # Draw 2
        for i in range(x + 4, x + 7):
            self.draw_cell_42(cells_grid[y][i])
        for i in range(y + 1, y + 3):
            self.draw_cell_42(cells_grid[i][x + 6])
        for i in range(x + 4, x + 7):
            self.draw_cell_42(cells_grid[y + 2][i])
        for i in range(y + 3, y + 5):
            self.draw_cell_42(cells_grid[i][x + 4])
        for i in range(y + 3, y + 5):
            self.draw_cell_42(cells_grid[i][x + 4])
        for i in range(x + 4, x + 7):
            self.draw_cell_42(cells_grid[y + 4][i])

    def draw_cell_42(self, cell: Cell) -> None:
        cell.is_visited = True
        cell.is_42_cell = True
        self.cells_img.draw_cell(cell, Theme.cell_42)

    def run(self) -> None:
        self.is_running = True

    def stop(self) -> None:
        self.is_running = False

    def set_cells_img(self, cells_img: CellsImage):
        self.cells_img = cells_img
        return self

    def count_cell_walls(self, cell: Cell) -> int:
        count = 0
        if cell.north:
            count += 1
        if cell.south:
            count += 1
        if cell.east:
            count += 1
        if cell.west:
            count += 1
        return count

    def break_wall_in_imperfect(self):
        for row in self.maze_state.cells_grid:
            for cell in row:
                if not cell.is_42_cell:
                    count_walls = self.count_cell_walls(cell)
                    if count_walls == 3:
                        if cell.west:
                            cell.west = False
                            return
