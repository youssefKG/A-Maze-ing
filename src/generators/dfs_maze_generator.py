from generators.maze_generator_algo import MazeGeneratorAlgo
from my_mlx.my_mlx import MyMlx
from renderer.colors import Colors
from renderer.themes import Theme

class DfsMazeGenerator(MazeGeneratorAlgo):
    def __init__(self):
        super().__init__()
        self.stack = []

    def generate(self) -> None:
        super().generate()
        self.current_cell = self.maze_state.cells_grid[0][0]
        self.current_cell.is_visited = True
        self.stack.append(self.current_cell)
        MyMlx.loop_hook(self.generate_DFS_animation, None)

    def generate_DFS_animation(self, _) -> None:
        if not self.is_running:
            return
        if not len(self.stack):
            self.is_running = False
            self.cells_img.draw_cell(self.current_cell, Theme.background)
            self.put_cells_img_to_window()
            return
        self.cells_img.draw_cell(self.current_cell, Theme.background)
        self.current_cell = self.stack[-1]
        self.cells_img.draw_cell(self.current_cell, Theme.background)
        self.put_cells_img_to_window()
        self.next_cell = self.check_neighbors()
        if self.next_cell:
            self.remove_wall(self.current_cell, self.next_cell)
            self.cells_img.draw_cell(self.current_cell)
            self.cells_img.draw_cell(self.next_cell, Theme.tracker)
            self.next_cell.is_visited = True
            self.stack.append(self.next_cell)
        else:
            self.current = self.stack.pop()
            self.cells_img.draw_cell(self.current_cell, Theme.tracker)
        self.put_cells_img_to_window()
