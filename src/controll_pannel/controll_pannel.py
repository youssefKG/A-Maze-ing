from renderer.images.cellImg import Border
from renderer.images.image import Image
from renderer.colors import Colors
from generators.mazeGenerator import MazeGenerator

class ControllPannel(Image):
    def __init__(self, mlx, mlx_ptr, win_ptr, screen_dimension):
        self.screen_width, self.screen_height = screen_dimension
        super().__init__(mlx, mlx_ptr, int(self.screen_width * 0.2), self.screen_height)
        self.win_ptr = win_ptr
        self.maze_generator = MazeGenerator(self.mlx, self.mlx_ptr,
                                            self.win_ptr, (self.screen_width,
                                                           self.screen_height))
        self.mlx.mlx_key_hook(self.win_ptr, self.onPress, None)

    def draw_pannel_controll(self):
        print(self.height, self.width)
        start = int(self.screen_width * 0.8)
        line_height = 40
        self.mlx.mlx_clear_window(self.mlx_ptr, self.win_ptr)
        for y in range(self.height):
            for x in range(self.width):
                self.put_pixel(x, y, Colors.GRAY)
        x = int(self.screen_width * 0.8 + (self.screen_width * 0.2) / 2)
        y = int(self.screen_height  / 2)
        for row in range(int(self.screen_width * 0.2)):
            for col in range(y + 30, y + 32):
                self.put_pixel(row, col, 0xFFFFF000)
        line_height = 20
        title = "A_MAZE_ING"
        descriptions = [
                "(Press A) to generate the maze using Depth-First Search (DFS)",
                "(Press B) to generate the maze using Wilson algorithm",
                "(Press R) to regenerate maze", "(Press C) to change color",
                "(Press S) to toggle solution path visibility"]
        self.mlx.mlx_clear_window(self.mlx_ptr, self.win_ptr)
        self.mlx.mlx_clear_window(self.mlx_ptr, self.win_ptr)
        self.mlx.mlx_clear_window(self.mlx_ptr, self.win_ptr)
        self.mlx.mlx_put_image_to_window(self.mlx_ptr, self.win_ptr, self.ptr, start, 0)
        self.mlx.mlx_string_put(self.mlx_ptr, self.win_ptr, x, y, Colors.WHITE, title)
        for i in range(len(descriptions)):
            self.mlx.mlx_string_put(self.mlx_ptr, self.win_ptr, 10 + start,
                                    line_height * (i + 2) + y, Colors.WHITE,
                                    descriptions[i])
    def onPress(self, keynum:int, _):
        print(keynum)
        if keynum == 65307:
            self.mlx.mlx_loop_exit(self.mlx_ptr)
        if keynum == 113:
            self.maze_generator.init_grid_cells()
            self.maze_generator.generate("dfs")
        if keynum == 98:
            self.maze_generator.init_grid_cells()
            self.maze_generator.generate("wilson")
        if keynum == 99:
            Border.change_color()
            self.maze_generator.redraw_maze()
