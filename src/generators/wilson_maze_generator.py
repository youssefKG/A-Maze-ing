from my_mlx.my_mlx import MyMlx
from generators.maze_generator_algo import MazeGeneratorAlgo
from random import choice
from time import sleep
from renderer.colors import Colors
from random import seed

class WilsonMazeGenerator(MazeGeneratorAlgo):
    def __init__(self):
        super().__init__()
        self.unvisited = []
        self.visited =  []
        self.next = None
        self.path_start = 0
        self.path = []
        self.frames = 0

    def generate(self) -> None:
        super().generate()
        self._init_unvisited()
        target_cell = choice(list(self.unvisited))
        self.visited.append(target_cell)
        self.unvisited.remove(target_cell)
        self.cells_img.draw_cell(target_cell, Colors.WHITE)
        self.put_cells_img_to_window()
        self.current_cell = choice(list(self.unvisited))
        MyMlx.loop_hook(self.generate_wilson_animations, None)

    def _init_unvisited(self) -> None:
        for cell_row in self.cells_grid:
            for cell in cell_row:
                if not cell.is_42_cell:
                    self.unvisited.append(cell)

    def generate_wilson_animations(self, _) -> None:
        self.frames += 1
        if self.frames % 1 != 0:
            return 
        if not self.is_running:
            return
        if len(self.unvisited) == 0:
            self.redraw_maze()
            self.is_running = False
            return 
        if self.current_cell not in self.visited:
            self.path.append(self.current_cell)
            self.next = self.check_neighbors()
            try:
                loop_index = self.path.index(self.next)
                for cell in self.path[loop_index + 1:]:
                    self.cells_img.draw_cell(cell, Colors.GRAY)
                self.path = self.path[:loop_index + 1]
            except:
                self.path.append(self.next)
            self.current_cell = self.next
            self.cells_img.draw_cell(self.current_cell, Colors.WHITE)
            self.put_cells_img_to_window()
            sleep(0.021)
        elif self.path_start < len(self.path) - 1:
                self.remove_wall(self.path[self.path_start], self.path[self.path_start + 1])
                self.cells_img.draw_cell(self.path[self.path_start], Colors.GRAY)
                self.cells_img.draw_cell(self.path[self.path_start + 1], Colors.GRAY)
                self.put_cells_img_to_window()
                self.visited.append(self.path[self.path_start])
                if self.path[self.path_start] in self.unvisited:
                    self.unvisited.remove(self.path[self.path_start])
                self.path_start += 1
        else:
            for cell in self.path:
                self.cells_img.draw_cell(cell, Colors.GRAY)
            self.put_cells_img_to_window()
            self.current_cell = choice(list(self.unvisited))
            self.path_start = 0
            self.path = []
            return
