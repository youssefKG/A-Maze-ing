from generators.maze_generator_algo import MazeGeneratorAlgo
from mlx.mlx.mlx import Mlx
from renderer.images.cellImg import CellsImage
from random import choice
from maze.cell import Cell

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
        self.invisited = set((cell for cell_row in self.cells_grid for cell in cell_row))
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
        target_cell = choice(list(self.invisited))
        self.visited.add(target_cell)
        self.invisited.remove(target_cell)
        self.generate_wilson_animations(None)
        # self.mlx.mlx_loop_hook(self.mlx_ptr, self.generate_wilson_animations, None)
                 
    def generate_wilson_animations(self, _):
        while len(self.invisited) > 0:
            path = []
            self.current_cell = choice(list(self.invisited))
            print(dir(self.current_cell))
            while self.current_cell not in self.visited:
                path.append(self.current_cell)
                self.next = self.check_neighbors()
                try:
                    loop_index = path.index(next)
                    path = path[:loop_index + 1]
                except:
                    if next != None:
                        path.append(next)
                for cell in path:
                    print(cell.x, cell.y)
                self.current = next
            for cell in path:
                print(cell.x, cell.y)
                self.cells_img.clear_cell(cell)
                self.cells_img.draw_cell(cell)
                self.visited.add(cell)
                self.visited.remove(cell)
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr,
                                         self.cells_img.ptr, 0, 0)
