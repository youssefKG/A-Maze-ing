from mlx.mlx.mlx import Mlx
from time import sleep
from generators.maze_generator_algo import MazeGeneratorAlgo
from renderer.colors import Colors


class DfsMazeGenerator(MazeGeneratorAlgo):
    def __init__(
        self,
        mlx: Mlx,
        mlx_ptr: int,
        win_ptr,
    ):
        super().__init__(
            mlx,
            mlx_ptr,
            win_ptr,
        )
        self.next_cell = None
        self.stack = []
        self.frames = 0
        self.is_finished = False

    def generate(self):
        self.current_cell = self.cells_grid[0][0]
        self.current_cell.is_visited = True
        self.stack.append(self.current_cell)
        self.mlx.mlx_loop_hook(self.mlx_ptr, self.generate_DFS_animation, None)

    def generate_DFS_animation(self, _):
        if self.is_finished:
            return
        if not len(self.stack):
            self.is_finished = True
            self.cells_img.clear_cell(self.current_cell, Colors.GRAY)
            self.cells_img.draw_cell(self.current_cell)
            self.put_cells_img_to_window()
            self.cells_img.clear_cell(self.current_cell, Colors.GRAY)
            self.cells_img.draw_cell(self.current_cell)
            self.put_cells_img_to_window()
            return
        self.cells_img.clear_cell(self.current_cell, Colors.GRAY)
        self.cells_img.draw_cell(self.current_cell)
        self.current_cell = self.stack[-1]
        self.cells_img.clear_cell(self.current_cell, Colors.GRAY)
        self.cells_img.draw_cell(self.current_cell)
        self.put_cells_img_to_window()
        self.next_cell = self.check_neighbors()
        if self.next_cell:
            self.remove_wall(self.current_cell, self.next_cell)
            self.cells_img.clear_cell(self.current_cell, Colors.GRAY)
            self.cells_img.draw_cell(self.current_cell)
            self.cells_img.draw_cell(self.next_cell, Colors.YELLOW)
            self.next_cell.is_visited = True
            self.stack.append(self.next_cell)
        else:
            self.current = self.stack.pop()
            self.cells_img.clear_cell(self.current_cell, Colors.GRAY)
            self.cells_img.draw_cell(self.current_cell, Colors.YELLOW)
        self.put_cells_img_to_window()
        sleep(0.052)
