from mlx.mlx.mlx import Mlx
from renderer.images.cellImg import CellsImage
from random import choice
from time import sleep
from generators.maze_generator_algo import MazeGeneratorAlgo


class DfsMazeGenerator(MazeGeneratorAlgo):
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
        self.next_cell = None
        self.current_cell = self.cells_grid[0][0]
        self.stack = []
        self.frames = 0
        self.is_finished = False

    def generate(self):
        self.current_cell.is_visited = True
        self.stack.append(self.current_cell)
        self.mlx.mlx_loop_hook(self.mlx_ptr, self.generate_DFS_animation, None)

    def remove_wall(self):
        if self.next_cell:
            x = self.current_cell.x - self.next_cell.x
            y = self.current_cell.y - self.next_cell.y
            if y == 1:
                self.current_cell.north = False
                self.next_cell.south = False
            if y == -1:
                self.current_cell.south = False
                self.next_cell.north = False
            if x == 1:
                self.current_cell.west = False
                self.next_cell.east = False
            if x == -1:
                self.current_cell.east = False
                self.next_cell.west = False

    def check_neighbors(self):
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

    def generate_DFS_animation(self, _):
        if self.is_finished:
            return
        if not len(self.stack):
            self.is_finished = True
            self.cells_img.clear_cell(self.current_cell)
            self.cells_img.draw_cell(self.current_cell)
            self.mlx.mlx_put_image_to_window(
                self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0
            )
            self.cells_img.clear_cell(self.current_cell)
            self.cells_img.draw_cell(self.current_cell)
            self.mlx.mlx_put_image_to_window(
                self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0
            )
            return
        self.cells_img.clear_cell(self.current_cell)
        self.cells_img.draw_cell(self.current_cell)
        self.current_cell = self.stack[-1]
        self.cells_img.clear_cell(self.current_cell)
        self.cells_img.draw_cell(self.current_cell)
        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0
        )
        self.next_cell = self.check_neighbors()
        if self.next_cell:
            self.remove_wall()
            self.cells_img.clear_cell(self.current_cell)
            self.cells_img.draw_cell(self.current_cell)
            self.cells_img.draw_cell(self.next_cell, 0x895DF000)
            self.next_cell.is_visited = True
            self.stack.append(self.next_cell)
        else:
            self.current = self.stack.pop()
            # self.cells_img.clear_cell(self.current_cell)
            self.cells_img.draw_cell(self.current_cell, 0x895DF000)
        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0)
        sleep(0.052)
