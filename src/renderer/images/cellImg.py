from typing import Self
from maze.cell import Cell
from renderer.images.image import Image
from renderer.themes import Theme
from my_mlx.my_mlx import MyMlx


def image_dimension(vertical_cells: int, horizontal_cells: int):
    max_cell = int(max(vertical_cells, horizontal_cells))
    min_screen = int(min(MyMlx.screen_width * 0.8, MyMlx.screen_height * 0.8))
    cell_dim = int(min_screen / max_cell)
    return ((cell_dim * horizontal_cells) - 4, (cell_dim * vertical_cells) - 4)


class CellsImage(Image):
    def __init__(self, vertical_cells: int, horizontal_cells: int) -> None:
        width, height = image_dimension(vertical_cells, horizontal_cells)
        super().__init__(width, height)
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.cellWidth = self.set_cell_width()
        self.cellHeight = self.set_cell_height()
        self.cellBorder = int((self.width / self.vertical_cells) * 0.20)

    def set_cell_width(self) -> int:
        cell_width = int(self.width / self.horizontal_cells)
        print(cell_width)
        return int(cell_width * 0.8)

    def set_cell_height(self) -> int:
        cell_height = int(self.height / self.vertical_cells)
        return int(cell_height * 0.8)

    def set_border(self, color: int) -> Self:
        self.border_color = color
        return self

    def set_cell_img(self, cells_img: list[Cell]) -> Self:
        self.cell_img = cells_img
        return self

    def draw_cell(self, cell: Cell, backgroundColor: int | None = None) -> None:
        # draw north wall
        border_color: int = Theme.border
        if backgroundColor is not None:
            for y in range(self.cellBorder, self.cellHeight):
                for x in range(self.cellBorder, self.cellWidth):
                    x_axis = cell.x * self.cellWidth + x
                    y_axis = cell.y * self.cellHeight + y
                    self.put_pixel(x_axis, y_axis, backgroundColor)

        if cell.north:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x)
                    y_axis = (cell.y * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, border_color)

        # draw south wall
        if cell.south:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x)
                    y_axis = (cell.y * self.cellHeight) + y + self.cellHeight
                    self.put_pixel(x_axis, y_axis, border_color)

        # draw west wall
        if cell.west:
            for y in range(self.cellHeight + self.cellBorder):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x)
                    y_axis = (cell.y * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, border_color)
        # draw east wall
        if cell.east:
            for y in range(self.cellHeight + self.cellBorder):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x) + self.cellWidth
                    y_axis = (cell.y * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, border_color)

    def draw_wall_between_two_cell(
        self, cell_one: Cell, cell_two: Cell, color: int
    ) -> None:
        x_axis = cell_one.x - cell_two.x
        y_axis = cell_one.y - cell_two.y

        if x_axis == 1:  # west wall
            start_x = self.cellWidth * cell_one.x
            end_x = start_x + self.cellWidth - self.cellBorder
            start_y = (self.cellHeight) * cell_two.y + self.cellBorder
            end_y = start_y + self.cellHeight - self.cellBorder
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

        if x_axis == -1:  # east wall
            start_x = self.cellWidth * cell_two.x
            end_x = start_x + self.cellWidth - self.cellBorder
            start_y = (self.cellHeight) * cell_two.y + self.cellBorder
            end_y = start_y + self.cellHeight - self.cellBorder
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

        if y_axis == 1:  # draw noth wall
            start_x = self.cellWidth * cell_one.x + self.cellBorder
            end_x = start_x + self.cellWidth - self.cellBorder
            start_y = self.cellHeight * cell_one.y
            end_y = start_y + self.cellBorder
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)

        if y_axis == -1:  # draw noth wall
            start_x = self.cellWidth * cell_two.x + self.cellBorder
            end_x = start_x + self.cellWidth - self.cellBorder
            start_y = self.cellHeight * cell_two.y
            end_y = start_y + self.cellBorder
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    self.put_pixel(x, y, color)
