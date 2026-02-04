from renderer.images.image import Image
from renderer.colors import Colors
from generators.algo_factory import AlgoFactory
from my_mlx.my_mlx import MyMlx
from renderer.themes import Theme
from solver.solver import Solver
from renderer.images.background.background_img import BackgroundImg


class ControllPannel(Image):
    def __init__(self) -> None:
        super().__init__(int(MyMlx.screen_width * 0.4), MyMlx.screen_height)
        self.algo = AlgoFactory.create()
        self.is_started = False
        self.solver = Solver()
        start_image = BackgroundImg("karim.png", "png")
        start_image.put_image_to_window()
        MyMlx.key_hook(self.on_press, None)

    def draw(self) -> None:
        pass

    def on_press(self, keynum: int, _: object) -> None:

        self.run_dfs(keynum)

        self.run_wilson(keynum)

        self.run_bfs(keynum)

        self.toggle_path(keynum)

        self.start_maze(keynum)

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
            self.algo = AlgoFactory.create("wilson")
            self.algo.generate()

    def start_maze(self, keynum: int) -> None:
        if keynum == 65293:  # enter key
            if not self.is_started:
                self.draw_descriptions()
                self.is_started = True
                self.algo.generate()

    def run_dfs(self, keynum: int) -> None:
        if keynum == 113:  # q key
            self.algo = AlgoFactory.create("dfs")
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
                Theme.change()
                self.draw_descriptions()
                self.algo.redraw_maze()
                if self.solver.is_path_shown:
                    self.solver.draw_path()

    def draw_descriptions(self) -> None:
        x_start = int(MyMlx.screen_width * 0.7)
        y = int(MyMlx.screen_height / 2)
        line_height = 20
        title = "A-Maze-ing"
        descriptions = [
            "(Press A) to generate the maze using Depth-First Search (DFS)",
            "(Press B) to generate the maze using Wilson algorithm",
            "(Press C) to change color",
            "(Press H) to toggle solution path visibility",
            "(Press S) to run Breadth-First Search (BFS) solver",
        ]
        for _ in range(6):
            MyMlx.clear_window()
        Theme.background_img.put_image_to_window()
        for row in range(int(MyMlx.screen_width * 0.3)):
            for col in range(y + 30, y + 32):
                self.put_pixel(row, col, Theme.border)
        MyMlx.put_image_to_window(self.ptr, x_start, 0)
        MyMlx.put_string(title, 10 + x_start, y, Colors.WHITE)
        for i in range(len(descriptions)):
            MyMlx.put_string(
                descriptions[i], x_start, line_height * (i + 2) + y, Colors.WHITE
            )
