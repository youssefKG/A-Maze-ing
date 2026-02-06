from maze.cell import Cell
from renderer.themes import Theme
from my_mlx.my_mlx import MyMlx


def image_dimension(vertical_cells: int, horizontal_cells: int):
    max_cell = int(max(vertical_cells, horizontal_cells))
    min_screen = int(min(MyMlx.screen_width, MyMlx.screen_height * 0.8))
    cell_dim = int(min_screen / max_cell)
    return ((cell_dim * horizontal_cells) - 4, (cell_dim * vertical_cells) - 4)


class CellsImage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_cells(self, vertical_cells: int, horizontal_cells: int):
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.set_image_dimension()
        self.set_cell_width()
        self.set_cell_height()
        self.set_border()
        self.ptr = MyMlx.new_image(self.width + 10, self.height + 10)
        self.data, self.bpp, self.sl, self.format = MyMlx.get_data_addr(self.ptr)
        self.clear_image()
        return self

    def set_cell_width(self):
        self.cell_width = int((self.width / self.horizontal_cells) * 0.8)
        return self

    def set_cell_height(self):
        self.cell_height = int((self.height / self.vertical_cells) * 0.8)
        return self

    def set_border(self):
        self.cell_border = int((self.width / self.vertical_cells) * 0.20)
        return self

    def set_image_dimension(self):
        max_cell = int(max(self.vertical_cells, self.horizontal_cells))
        min_screen = int(min(MyMlx.screen_width, MyMlx.screen_height * 0.8))
        cell_dim = int(min_screen / max_cell)
        self.width = int(cell_dim * self.vertical_cells - 4)
        self.height = int(cell_dim * self.horizontal_cells - 4)
        self.width, self.height = image_dimension(
            self.vertical_cells, self.horizontal_cells
        )
        return self

    def draw_cell(self, cell: Cell, backgroundColor: int | None = None) -> None:
        border_color: int = Theme.border
        if backgroundColor is not None:
            for y in range(self.cell_border, self.cell_height):
                for x in range(self.cell_border, self.cell_width):
                    x_axis = cell.x * self.cell_width + x
                    y_axis = cell.y * self.cell_height + y
                    self.put_pixel(x_axis, y_axis, backgroundColor)

        # draw north wall
        if cell.north:
            for x in range(self.cell_width + self.cell_border):
                for y in range(self.cell_border):
                    x_axis = x + (self.cell_width * cell.x)
                    y_axis = (cell.y * self.cell_height) + y
                    self.put_pixel(x_axis, y_axis, border_color)

        # draw south wall
        if cell.south:
            for x in range(self.cell_width + self.cell_border):
                for y in range(self.cell_border):
                    x_axis = x + (self.cell_width * cell.x)
                    y_axis = (cell.y * self.cell_height) + y + self.cell_height
                    self.put_pixel(x_axis, y_axis, border_color)

        # draw west wall
        if cell.west:
            for y in range(self.cell_height + self.cell_border):
                for x in range(self.cell_border):
                    x_axis = x + (self.cell_width * cell.x)
                    y_axis = (cell.y * self.cell_width) + y
                    self.put_pixel(x_axis, y_axis, border_color)
        # draw east wall
        if cell.east:
            for y in range(self.cell_width + self.cell_border):
                for x in range(self.cell_border):
                    x_axis = x + (self.cell_width * cell.x) + self.cell_height
                    y_axis = (cell.y * self.cell_height) + y
                    self.put_pixel(x_axis, y_axis, border_color)

    def draw_wall_between_two_cell(
        self, cell_one: Cell, cell_two: Cell, color: int
    ) -> None:
        x_axis = cell_one.x - cell_two.x
        y_axis = cell_one.y - cell_two.y

        if x_axis == 1:  # west wall
            start_x = self.cell_width * cell_one.x
            end_x = start_x + self.cell_height - self.cell_border
            start_y = (self.cell_height) * cell_two.y + self.cell_border
            end_y = start_y + self.cell_height - self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

        if x_axis == -1:  # east wall
            start_x = self.cell_width * cell_two.x
            end_x = start_x + self.cell_width - self.cell_border
            start_y = (self.cell_height) * cell_two.y + self.cell_border
            end_y = start_y + self.cell_height - self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

        if y_axis == 1:  # draw noth wall
            start_x = self.cell_width * cell_one.x + self.cell_border
            end_x = start_x + self.cell_width - self.cell_border
            start_y = self.cell_height * cell_one.y
            end_y = start_y + self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

        if y_axis == -1:  # draw noth wall
            start_x = self.cell_width * cell_two.x + self.cell_border
            end_x = start_x + self.cell_width - self.cell_border
            start_y = self.cell_height * cell_two.y
            end_y = start_y + self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

    def put_pixel(self, x: int, y: int, color: int) -> None:
        offset = int((y * self.sl) + (x * (self.bpp / 8)))
        self.data[offset : offset + 4] = (color).to_bytes(4, "little")

    def clear_image(self):
        for i in range(0, len(self.data), 4):
            self.data[i : i + 4] = (0x0000000).to_bytes(4, "little")
