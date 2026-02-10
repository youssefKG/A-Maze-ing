from maze.cell import Cell
from renderer.themes import Theme
from renderer.colors import Colors
from my_mlx.my_mlx import MyMlx
from typing import Any


class CellsImage:
    _instance = None

    def __new__(cls) -> object:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_cells(self, vertical_cells: int, horizontal_cells: int) -> object:
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.set_image_dimension()
        self.set_cell_width()
        self.set_cell_height()
        self.set_border()
        self.ptr = MyMlx.new_image(
            self.width + self.cell_border + 4,
            self.height + self.cell_border + 4,
        )
        self.data, self.bpp, self.sl, self.format = MyMlx.get_data_addr(
            self.ptr
        )
        self.clear_image()
        return self

    def set_cell_width(self) -> Any:
        self.cell_width = int(self.cell_dim * 0.70)
        return self

    def set_cell_height(self) -> Any:
        self.cell_height = int(self.cell_dim * 0.70)
        return self

    def set_border(self) -> Any:
        self.ecart = 2 * self.cell_dim * 0.70
        self.ecart = 2 * self.cell_dim * 0.70 - int(self.ecart)
        self.cell_border = round(self.cell_dim * 0.15 + self.ecart)
        return self

    def set_image_dimension(self) -> Any:
        max_cell = int(max(self.vertical_cells, self.horizontal_cells))
        min_screen = int(
            min(MyMlx.screen_width, int(MyMlx.screen_height * 0.8))
        )
        self.cell_dim = int(min_screen / max_cell)
        self.width = int(self.cell_dim * self.horizontal_cells)
        self.height = int(self.cell_dim * self.vertical_cells)
        return self

    def draw_cell(
        self, cell: Cell, backgroundColor: int | None = None
    ) -> None:
        if backgroundColor is not None:
            start_x = self.cell_dim * cell.x + self.cell_border
            end_x = start_x + self.cell_width
            start_y = self.cell_dim * cell.y + self.cell_border
            end_y = start_y + self.cell_height
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, backgroundColor)

        # draw north wall

        if cell.north:
            start_y = cell.y * self.cell_dim
            end_y = start_y + self.cell_border
            start_x = cell.x * self.cell_dim
            end_x = start_x + self.cell_dim
            if cell.x != 0:
                start_x -= self.cell_border
            if cell.x != self.horizontal_cells - 1:
                end_x += self.cell_border
            for x in range(start_x, end_x):
                for y in range(start_y, end_y):
                    self.put_pixel(x, y, Theme.border)

        if cell.south:
            start_y = (
                cell.y * self.cell_dim + self.cell_height + self.cell_border
            )
            end_y = start_y + self.cell_border
            start_x = cell.x * self.cell_dim
            end_x = start_x + self.cell_dim
            if cell.x != 0:
                start_x -= self.cell_border
            if cell.x != self.horizontal_cells - 1:
                end_x += self.cell_border
            for x in range(start_x, end_x):
                for y in range(start_y, end_y):
                    self.put_pixel(x, y, Theme.border)

        if cell.west:
            start_y = cell.y * self.cell_dim
            end_y = start_y + (self.cell_height + 2 * self.cell_border)
            start_x = cell.x * self.cell_dim
            end_x = start_x + self.cell_border
            if cell.y != 0:
                start_y -= self.cell_border
            if cell.y != self.vertical_cells - 1:
                end_y += self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, Theme.border)
        if cell.east:
            start_y = cell.y * (self.cell_dim)
            end_y = start_y + (self.cell_height + 2 * self.cell_border)
            start_x = (
                cell.x * (self.cell_dim) + self.cell_width + self.cell_border
            )
            end_x = start_x + self.cell_border
            if cell.y != 0:
                start_y -= self.cell_border
            if cell.y != self.vertical_cells - 1:
                end_y += self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, Theme.border)

    def is_corner_cell(self, cell: Cell) -> bool:
        if (
            cell.x > 0
            and cell.x < self.horizontal_cells - 1
            and cell.y > 0
            and cell.y < self.vertical_cells - 1
        ):
            return False
        return True

    def draw_wall_between_two_cell(
        self, cell_one: Cell, cell_two: Cell, color: int
    ) -> None:
        x_axis = cell_one.x - cell_two.x
        y_axis = cell_one.y - cell_two.y

        if y_axis == 1:  # draw noth wall
            start_y = self.cell_dim * cell_one.y
            end_y = start_y + self.cell_border
            start_x = self.cell_dim * cell_one.x + self.cell_border
            end_x = start_x + self.cell_width
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

            start_y = (
                self.cell_dim * cell_two.y
                + self.cell_height
                + self.cell_border
            )
            end_y = start_y + self.cell_border
            start_x = self.cell_dim * cell_two.x + self.cell_border
            end_x = start_x + self.cell_width
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

        if y_axis == -1:  # draw noth wall
            start_y = self.cell_dim * cell_two.y
            end_y = start_y + self.cell_border
            start_x = self.cell_dim * cell_two.x + self.cell_border
            end_x = start_x + self.cell_width
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

            start_y = (
                self.cell_dim * cell_one.y
                + self.cell_height
                + self.cell_border
            )
            end_y = start_y + self.cell_border
            start_x = self.cell_dim * cell_one.x + self.cell_border
            end_x = start_x + self.cell_width
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

        if x_axis == 1:  # west wall
            start_y = self.cell_dim * cell_one.y + self.cell_border
            end_y = self.cell_height + start_y
            start_x = self.cell_dim * cell_one.x
            end_x = start_x + self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

            start_y = self.cell_dim * cell_two.y + self.cell_border
            end_y = self.cell_height + start_y
            start_x = (
                self.cell_dim * cell_two.x + self.cell_width + self.cell_border
            )
            end_x = start_x + self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

        if x_axis == -1:  # east wall
            start_y = self.cell_dim * cell_two.y + self.cell_border
            end_y = self.cell_height + start_y
            start_x = self.cell_dim * cell_two.x
            end_x = start_x + self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)
            start_y = self.cell_dim * cell_one.y + self.cell_border
            end_y = self.cell_height + start_y
            start_x = (
                self.cell_dim * cell_one.x + self.cell_width + self.cell_border
            )
            end_x = start_x + self.cell_border
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

    def put_pixel(self, x: int, y: int, color: int) -> None:
        offset = int((y * self.sl) + (x * (self.bpp / 8)))
        self.data[offset:offset + 4] = (color).to_bytes(4, "little")

    def clear_image(self):
        for i in range(0, len(self.data), 4):
            self.data[i : i + 4] = (0x0000000).to_bytes(4, "little")
