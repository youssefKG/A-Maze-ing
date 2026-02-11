from my_mlx.my_mlx import MyMlx
from generators.maze_generator_algo import MazeGeneratorAlgo
from random import choice
from time import sleep
from renderer.colors import Colors
from renderer.themes import Theme


class WilsonMazeGenerator(MazeGeneratorAlgo):
    def __init__(self) -> None:
        super().__init__()
        self.unvisited: list[Cell] = []
        self.visited: list[Cell] = []
        self.next = None
        self.path_start = 0
        self.path: list[Cell] = []
        self.frames = 0

    def generate(self) -> None:
        super().generate()
        self._init_unvisited()
        target_cell = choice(list(self.unvisited))
        self.is_running = True
        self.visited.append(target_cell)
        self.unvisited.remove(target_cell)
        self.cells_img.draw_cell(target_cell, Colors.ORANGE)
        self.put_cells_img_to_window()
        self.current_cell = choice(list(self.unvisited))
        MyMlx.loop_hook(self.generate_wilson_animations, None)

    def _init_unvisited(self) -> None:
        for cell_row in self.maze_state.cells_grid:
            for cell in cell_row:
                if not cell.is_42_cell:
                    self.unvisited.append(cell)

    def generate_wilson_animations(self, _) -> None:
        self.frames += 1
        if self.frames % 1 != 0:
            return
        if self.is_finished:
            return
        if not self.is_running:
            return
        print("infinite loop")
        if len(self.unvisited) == 0:
            self.redraw_maze()
            self.break_wall_in_imperfect()
            self.put_cells_img_to_window()
            self.is_finished = True
            self.is_running = False
            return
        if self.current_cell not in self.visited:
            self.path.append(self.current_cell)
            self.next = self.check_neighbors()
            try:
                loop_index = self.path.index(self.next)
                for cell in self.path[loop_index + 1:]:
                    self.cells_img.draw_cell(cell, Theme.background)
                self.path = self.path[: loop_index + 1]
            except ValueError:
                self.path.append(self.next)
            if self.next:
                self.current_cell = self.next
                self.cells_img.draw_cell(self.current_cell, Theme.tracker)
            self.put_cells_img_to_window()
            sleep(0.021)
        elif self.path_start < len(self.path) - 1:
            self.cells_img.draw_cell(
                self.path[self.path_start], Theme.background
            )
            self.cells_img.draw_cell(
                self.path[self.path_start + 1], Theme.background
            )
            self.remove_wall(
                self.path[self.path_start], self.path[self.path_start + 1]
            )
            self.put_cells_img_to_window()
            self.visited.append(self.path[self.path_start])
            if self.path[self.path_start] in self.unvisited:
                self.unvisited.remove(self.path[self.path_start])
            self.path_start += 1
        else:
            for cell in self.path:
                self.cells_img.draw_cell(cell, Theme.background)
            self.put_cells_img_to_window()
            self.current_cell = choice(list(self.unvisited))
            self.path_start = 0
            self.path = []
            return
