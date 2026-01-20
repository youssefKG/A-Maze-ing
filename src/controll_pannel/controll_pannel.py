from renderer.images.cellImg import Border
from renderer.images.image import Image
from renderer.colors import Colors
from generators.mazeGenerator import MazeGenerator
from my_mlx.my_mlx import MyMlx

class ControllPannel(Image):
    def __init__(self):
        super().__init__(int(MyMlx.screen_width * 0.2), MyMlx.screen_height)
        self.maze_generator = MazeGenerator()
        MyMlx.key_hook(self.on_press, None)

    def draw(self):
        start = int(MyMlx.screen_width * 0.8)
        x = int(MyMlx.screen_width * 0.8 + (MyMlx.screen_width * 0.2) / 2)
        y = int(MyMlx.screen_height  / 2)
        self.draw_background_color(x, y)
        self.draw_descriptions(x, y, start)
        MyMlx.put_image_to_window(self.ptr, start, 0)

    def on_press(self, keynum:int, _):
        print(keynum)
        if keynum == 65307:
            MyMlx.loop_exit()
        if keynum == 113:
            self.maze_generator.init_grid_cells()
            self.maze_generator.generate("dfs")
        if keynum == 98:
            self.maze_generator.init_grid_cells()
            self.maze_generator.generate("wilson")
        if keynum == 99:
            Border.change_color()
            self.maze_generator.redraw_maze()


    def draw_descriptions(self, x, y, start):
        line_height = 20
        title = "A-Maze-ing"
        descriptions = [
                "(Press A) to generate the maze using Depth-First Search (DFS)",
                "(Press B) to generate the maze using Wilson algorithm",
                "(Press R) to regenerate maze", "(Press C) to change color",
                "(Press S) to toggle solution path visibility"]
        MyMlx.put_string(x, y, Colors.WHITE, title)
        for row in range(int(MyMlx.screen_width * 0.2)):
            for col in range(y + 30, y + 32):
                self.put_pixel(row, col, 0xFFFFF000)
        for i in range(len(descriptions)):
            MyMlx.put_string(10 + start, line_height * (i + 2) + y, Colors.WHITE, descriptions[i])
        title = "A_MAZE_ING"

    def draw_background_color(self, x, y):
        for y in range(self.height):
            for x in range(self.width):
                self.put_pixel(x, y, Colors.GRAY)

