from generators.algo_factory import AlgoFactory
from mazegen.MazeGenerator import MazeGenerator
from my_mlx.my_mlx import MyMlx
from renderer.themes import Theme
from solver.solver import Solver
from renderer.images.background.background_img import BackgroundImg
from maze.maze_state import MazeState


class ControllPannel:
    def __init__(self) -> None:
        self.algo = AlgoFactory.create()
        self.is_started = False
        self.solver = Solver()
        start_image = BackgroundImg("karim.png", "png")
        start_image.put_image_to_window()
        MyMlx.key_hook(self.on_press, None)
        self.maze_state = MazeState()
        self.maze_gen = MazeGenerator(
            self.maze_state.horizontal_cells,
            self.maze_state.vertical_cells,
            (self.maze_state.entry_cell.x, self.maze_state.entry_cell.y),
            (self.maze_state.exit_cell.x, self.maze_state.exit_cell.y),
            self.maze_state.seed,
            self.maze_state.filename,
            self.maze_state.is_perfect,
        )

    def draw(self) -> None:
        pass

    def on_press(self, keynum: int, _: object) -> None:

        self.start_maze(keynum)
        if self.is_started:
            self.run_dfs(keynum)
            self.run_wilson(keynum)
            self.run_bfs(keynum)
            self.toggle_path(keynum)
            self.change_color(keynum)
        if keynum == 65307:  # esc key
            MyMlx.loop_exit()

    def run_bfs(self, keynum: int) -> None:
        if keynum == 115:
            if self.algo.is_finished:
                self.solver.redraw_maze()
                self.solver = AlgoFactory.create_solver("bfs")
                self.solver.hide_path()
                self.solver.generate()

    def run_wilson(self, keynum: int) -> None:
        if keynum == 98:  # B key
            self.maze_gen.generate("wilson")
            self.maze_state.set_cells_grid()
            self.algo = AlgoFactory.create("wilson")
            self.algo.generate()
            self.solver.hide_path()

    def run_dfs(self, keynum: int) -> None:
        if keynum == 113:  # q key
            self.solver.hide_path()
            self.maze_state.set_cells_grid()
            self.algo = AlgoFactory.create("dfs")
            # self.maze_gen.generate("dfs")
            self.algo.generate()

    def start_maze(self, keynum: int) -> None:
        if keynum == 65293:  # enter key
            if not self.is_started:
                self.is_started = True
                Theme.background_img.put_image_to_window()
                self.algo.generate()

    def toggle_path(self, keynum: int) -> None:
        if keynum == 104:  # toogle path on press H
            if (
                self.algo.is_finished
                and self.solver.is_finished
                and not self.algo.is_running
            ):
                self.algo.redraw_maze()
                self.solver.toggle_path()

    def change_color(self, keynum) -> None:
        if keynum == 99:  # C key
            if not self.solver.is_running:
                if (
                    self.algo.is_running
                    and AlgoFactory.generator_name == "wilson"
                ):
                    return
                Theme.change()
                Theme.background_img.put_image_to_window()
                self.algo.redraw_maze()
                if self.solver.is_path_shown:
                    self.solver.draw_path()
