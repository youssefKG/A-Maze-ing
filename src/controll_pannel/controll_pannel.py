from renderer.images.cellImg import Border
from renderer.images.image import Image
from renderer.colors import Colors
from generators.algo_factory import AlgoFactory
from my_mlx.my_mlx import MyMlx
from renderer.images.cellImg import Border
from solver.bfs_solver import BfsSolver

class ControllPannel(Image):
    def __init__(self) -> None:
        super().__init__(int(MyMlx.screen_width * 0.2), MyMlx.screen_height)
        MyMlx.key_hook(self.on_press, None)
        self.algo = AlgoFactory.create()
        self.solver = None

    def draw(self) -> None:
        x_start = int(MyMlx.screen_width * 0.8)
        y = int(MyMlx.screen_height / 2)
        self.draw_background_color()
        self.draw_descriptions(y, x_start)
        self.algo.generate()

    def on_press(self, keynum: int, _) -> None:
        if keynum == 65307:
            MyMlx.loop_exit()
        if keynum == 113:
            self.algo = AlgoFactory.create("dfs")
            self.algo.generate()
        if keynum == 98:
            self.algo = AlgoFactory.create("wilson")
            self.algo.generate()
        if keynum == 99:
            self.change_color()
        if keynum == 115:
            print("toogle solution")
            self.solver = AlgoFactory.create_solver("bfs", self.algo.cells_grid)
            self.solver.find_path()

    def draw_descriptions(self, y: int, x_start: int) -> None:
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
        for row in range(int(MyMlx.screen_width * 0.2)):
            for col in range(y + 30, y + 32):
                self.put_pixel(row, col, 0xFFFFF000)
        MyMlx.put_image_to_window(self.ptr, x_start, 0)
        MyMlx.put_string(title, 10 + x_start, y, Colors.WHITE)
        for i in range(len(descriptions)):
            MyMlx.put_string(
                    descriptions[i],
                    10 + x_start,
                    line_height * (i + 2) + y,
                    Colors.WHITE
                    )

    def draw_background_color(self) -> None:
        for y in range(MyMlx.screen_height):
            for x in range(self.width - 4):
                self.put_pixel(x, y, Colors.GRAY)

    def change_color(self):
        if self.algo is not None:
            self.algo.stop()
            Border.change_color()
            self.algo.redraw_maze()
            self.algo.run()
