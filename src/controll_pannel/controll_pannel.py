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
        self.solver = Solver()
        start_image = BackgroundImg("karim.png", "png")
        start_image.put_image_to_window()
        MyMlx.key_hook(self.on_press, None)

    def draw(self) -> None:
        pass
        """

        """

    def on_press(self, keynum: int, _) -> None:
        print(keynum)
        if keynum == 65307: # esc key
            MyMlx.loop_exit()
        elif keynum == 113: # q key
            self.algo = AlgoFactory.create("dfs")
            self.algo.generate()
        elif keynum == 98: # B key
            self.algo = AlgoFactory.create("wilson")
            self.algo.generate()
        elif keynum == 99: # C key
            self.change_color()
        elif keynum == 115: # s key
            if self.algo.is_finished:
                if self.solver.is_finished:
                    self.solver.hide_path()
                self.algo.redraw_maze()
                self.solver = AlgoFactory.create_solver("bfs")
                self.solver.generate()
        elif keynum == 104: # toogle path on press H
            if self.algo.is_finished and self.solver.is_finished and not self.algo.is_running:
                self.algo.redraw_maze()
                self.solver.toggle_path()
        elif keynum == 65293: # enter key
            self.draw_descriptions()
            self.algo.generate()


    def draw_background_color(self) -> None:
        for y in range(MyMlx.screen_height):
            for x in range(self.width - 4):
                self.put_pixel(x, y, Colors.GRAY)

    def change_color(self):
        if self.algo is not None:
            # if  solution algo running you cannot change theme
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
            "(Press R) to regenerate maze",
            "(Press C) to change color",
            "(Press S) to toggle solution path visibility",
        ]
        for _ in range(4):
            MyMlx.clear_window()
        Theme.background_img.put_image_to_window()
        for row in range(int(MyMlx.screen_width * 0.3)):
            for col in range(y + 30, y + 32):
                self.put_pixel(row, col, Theme.border)
        MyMlx.put_image_to_window(self.ptr, x_start, 0)
        MyMlx.put_string(title, 10 + x_start, y, Colors.WHITE)
        for i in range(len(descriptions)):
            MyMlx.put_string(
                    descriptions[i],
                    x_start,
                    line_height * (i + 2) + y,
                    Colors.WHITE
                    )
