from generators.maze_generator_algo import MazeGeneratorAlgo
from mlx.mlx.mlx import Mlx
from renderer.images.cellImg import CellsImage
from random import choice

class WilsonMazeGenerator(MazeGeneratorAlgo):
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

        super().__init__(mlx,
            mlx_ptr,
            win_ptr,
            cells_img,
            cells_grid,
            vertical_cells,
            horizontal_cells,
        )
        self.unvisited = set()
        for cell_row in self.cells_grid:
            for cell in cell_row:
                self.unvisited.add(cell)
        self.visited = set()
        self.current_cell = None
        self.next = None

    def check_neighbors(self):
        if self.current_cell:
            x = self.current_cell.x
            y = self.current_cell.y
            neighbors = []
            if y - 1 >= 0:
                north = self.cells_grid[y - 1][x]
                neighbors.append(north)
            if y + 1 < self.vertical_cells:
                south = self.cells_grid[y + 1][x]
                neighbors.append(south)
            if x + 1 < self.horizontal_cells:
                east = self.cells_grid[y][x + 1]
                neighbors.append(east)
            if x - 1 >= 0:
                west = self.cells_grid[y][x - 1]
                neighbors.append(west)
            if len(neighbors) != 0:
                return choice(neighbors)

    def generate(self):
        target_cell = choice(list(self.unvisited))
        self.visited.add(target_cell)
        self.unvisited.remove(target_cell)
        self.generate_wilson_animations(None)
        # self.mlx.mlx_loop_hook(self.mlx_ptr, self.generate_wilson_animations, None)
    def remove_wall(self, current_cell, next_cell):
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
                 
    def generate_wilson_animations(self, _):
        while len(self.unvisited) > 0:
            path = []
            self.current_cell = choice(list(self.unvisited))
            while self.current_cell not in self.visited:
                path.append(self.current_cell)
                self.next = self.check_neighbors()
                try:
                    loop_index = path.index(self.next)
                    path = path[:loop_index + 1]
                except:
                    path.append(self.next)
                self.current_cell = self.next
                for cell in path:
                    print(cell.x, cell. y)
            print("")
            for i in range(len(path) - 1):
                self.remove_wall(path[i], path[i + 1])
                self.cells_img.clear_cell(path[i])
                self.cells_img.clear_cell(path[i + 1])
                self.cells_img.draw_cell(path[i])
                self.cells_img.draw_cell(path[i + 1])
                self.visited.add(path[i])
                if path[i] in self.unvisited:
                    self.unvisited.remove(path[i])
            self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr,
                                             self.cells_img.ptr, 0, 0)
