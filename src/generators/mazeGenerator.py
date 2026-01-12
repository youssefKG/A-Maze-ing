from maze.cell import Cell
from mlx.mlx.mlx import Mlx
from renderer.images.cellImg import CellsImage
from random import choice

class MazeGenerator:
    def __init__(
        self, mlx: Mlx, mlx_ptr: int, win_ptr, height: int, width: int
    ) -> None:
        self.mlx = mlx
        self.mlx_ptr = mlx_ptr
        self.width = width
        self.height = height
        self.win_ptr = win_ptr
        self.vertical_cells = 15
        self.horizontal_cells = 15
        self.cell_width = self.get_cell_width()
        self.cell_height = self.get_cell_height()
        self.cells_img = CellsImage(
            self.mlx,
            self.mlx_ptr,
            self.width,
            self.height,
            self.cell_width,
            self.cell_height,
        )
        self.cells_grid = []
        self.stack = []
        self.solution = []
        self.is_finished = False
        self.frames = 0
        self.next_cell = None

    def get_cell_width(self):
        return int((self.width / self.vertical_cells)) - 4

    def get_cell_height(self):
        return int((self.height / self.horizontal_cells)) - 4

    def init_grid_cells(self):
        for i in range(self.vertical_cells):
            row = []
            for j in range(self.horizontal_cells):
                row.append(Cell(i, j))
            self.cells_grid.append(row)
        i = 0
        while i < self.vertical_cells:
            j = 0
            while j < self.horizontal_cells:
                self.cells_img.draw_cell(i, j, self.cells_grid[i][j])
                j += 1
            i += 1
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0)

    def generate(self):
        self.init_grid_cells()
        i = 0
        self.current_cell = self.cells_grid[0][0]
        self.current_cell.is_visited = True
        """
        self.next_cell = self.cells_grid[0][1]
        self.cells_img.draw_cell(self.current_cell.x, self.current_cell.y, self.current_cell)
        self.cells_img.draw_cell(self.next_cell.x, self.next_cell.y, self.next_cell)
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0)
        self.remove_wall()
        self.cells_img.draw_cell(self.current_cell.x, self.current_cell.y, self.current_cell)
        self.cells_img.draw_cell(self.next_cell.x, self.next_cell.y, self.next_cell)
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0)
        """
        self.stack.append(self.current_cell)
        self.mlx.mlx_loop_hook(self.mlx_ptr, self.generate_DFS_animation, None)

    def remove_wall(self):
        if (self.next_cell):
            x = self.current_cell.x - self.next_cell.x
            y = self.current_cell.y - self.next_cell.y
            if y == 1:
                self.current_cell.north= False
                self.next_cell.south = False
            if y == -1:
                self.current_cell.south = False
                self.next_cell.north =  False
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
        if x - 1 >= 0:
            north = self.cells_grid[x - 1][y]
            if not north.is_visited:
                neighbors.append(north)
        if x + 1 < self.vertical_cells:
            south = self.cells_grid[x + 1][y]
            if not south.is_visited:
                neighbors.append(south) 
        if y + 1 < self.horizontal_cells:
            east = self.cells_grid[x][y + 1]
            if not east.is_visited:
                neighbors.append(east)
        if y - 1 >= 0:
            west = self.cells_grid[x][y - 1]
            if not west.is_visited:
                neighbors.append(west)
        if len(neighbors) != 0:
            return choice(neighbors)
        return None

    def generate_DFS_animation(self, _):
        self.frames += 1
        if self.frames % 5 != 0:
            return
        if self.is_finished:
            return
        if not len(self.stack):
            print("end")
            self.is_finished = True
            return
        self.current_cell = self.stack[-1]
        self.next_cell = self.check_neighbors()
        if self.next_cell:
            self.cells_img.clear_cell(self.current_cell)
            self.remove_wall()
            self.cells_img.clear_cell(self.next_cell)
            self.cells_img.draw_cell(self.current_cell.x, self.current_cell.y, self.current_cell)
            self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0)
            self.next_cell.is_visited = True
            self.stack.append(self.next_cell)
        else:
            self.current = self.stack.pop()
            self.cells_img.draw_cell(self.current_cell.x, self.current_cell.y, self.current_cell)
            self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr, self.cells_img.ptr, 0, 0)
