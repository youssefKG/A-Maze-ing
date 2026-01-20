from my_mlx.my_mlx import MyMlx
from generators.maze_generator_algo import MazeGeneratorAlgo
from random import choice
from time import sleep
from renderer.colors import Colors

class WilsonMazeGenerator(MazeGeneratorAlgo):
    def __init__(self):
        self.unvisited = set()
        self.visited = set()
        self.next = None
        self.path_start = 0
        self.path = []
        self.frames = 0


    def generate(self):
        self._init_unvisited()
        target_cell = choice(list(self.unvisited))
        self.current_cell = choice(list(self.unvisited))
        self.cells_img.clear_cell(target_cell, Colors.WHITE)
        self.cells_img.draw_cell(target_cell, Colors.WHITE)
        self.put_cells_img_to_window()
        self.visited.add(target_cell)
        self.unvisited.remove(target_cell)
        MyMlx.loop_hook(self.generate_wilson_animations, None)

    def _init_unvisited(self):
        for cell_row in self.cells_grid:
            for cell in cell_row:
                if not cell.is_42_cell:
                    self.unvisited.add(cell)

    def generate_wilson_animations(self, _):
        if self.frames % 12 != 0:
            return 
        if len(self.unvisited) == 0:
            return 
        if self.current_cell not in self.visited:
            self.path.append(self.current_cell)
            self.next = self.check_neighbors()
            try:
                loop_index = self.path.index(self.next)
                for cell in self.path[loop_index + 1:]:
                    self.cells_img.clear_cell(cell, Colors.WHITE)
                    self.cells_img.draw_cell(cell, Colors.GRAY)
                self.path = self.path[:loop_index + 1]
            except:
                self.path.append(self.next)
            self.current_cell = self.next
            self.cells_img.clear_cell(self.current_cell, Colors.WHITE)
            self.cells_img.draw_cell(self.current_cell, Colors.WHITE)
            self.put_cells_img_to_window()
            sleep(0.021)
        elif self.path_start < len(self.path) - 1:
                self.remove_wall(self.path[self.path_start], self.path[self.path_start + 1])
                self.cells_img.clear_cell(self.path[self.path_start], Colors.GRAY)
                self.cells_img.clear_cell(self.path[self.path_start + 1], Colors.GRAY)
                self.cells_img.draw_cell(self.path[self.path_start], Colors.GRAY)
                self.cells_img.draw_cell(self.path[self.path_start + 1], Colors.GRAY)
                self.put_cells_img_to_window()
                self.visited.add(self.path[self.path_start])
                if self.path[self.path_start] in self.unvisited:
                    self.unvisited.remove(self.path[self.path_start])
                self.path_start += 1
        else:
            self.current_cell = choice(list(self.unvisited))
            self.path_start = 0
            self.path = []
            return
