from mlx.mlx import Mlx
from maze.cell import Cell
from renderer.images.image import Image
from renderer.colors import Colors

class Border:
    _colors = [Colors.RED, Colors.BLUE, Colors.YELLOW, Colors.GRAY,
                Colors.GREEN]
    _current_color_index = 0
    color = _colors[_current_color_index]

    @classmethod
    def change_color(cls):
        if cls._current_color_index + 1 < len(cls._colors):
            cls._current_color_index += 1
        else:
            cls._current_color_index = 0
        cls._color = cls._colors[cls._current_color_index]

class CellsImage(Image):
    def __init__(self, vertical_cells, horizontal_cells):
        super().__init__()
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.cellWidth = self.set_cell_width()
        self.cellHeight = self.set_cell_height()
        self.cellBorder = int(self.cellHeight * 0.15)

    def set_cell_width(self):
        cell_width = int(self.width / self.horizontal_cells)
        return int(cell_width - cell_width / 4)

    def set_cell_height(self):
        cell_height = int(self.height / self.vertical_cells)
        return int(cell_height - cell_height / 4)

    def draw_cell(self, cell: Cell,  backgroundColor=None):
        # draw north wall
        if backgroundColor is not None:
            for y in range(self.cellHeight):
                for x in range(self.cellWidth):
                    x_axis = cell.x * self.cellWidth + x
                    y_axis = cell.y * self.cellHeight + y
                    self.put_pixel(x_axis, y_axis, backgroundColor)
                    
        if cell.north:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x)
                    y_axis = (cell.y * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, Border.color)

        # draw south wall
        if cell.south:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x)
                    y_axis = (cell.y * self.cellHeight) + y + self.cellHeight
                    self.put_pixel(x_axis, y_axis, Border.color)

        # draw west wall
        if cell.west:
            for y in range(self.cellHeight + self.cellBorder):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x)
                    y_axis = (cell.y * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, Border.color)
        # draw east wall
        if cell.east:
            for y in range(self.cellHeight + self.cellBorder):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x) + self.cellWidth
                    y_axis = (cell.y * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, Border.color)

    def clear_cell(self, cell: Cell, color=0x98340EAB):
        for y in range(self.cellHeight):
            for x in range(self.cellWidth):
                y_axis = cell.y * self.cellHeight + y
                x_axis = cell.x * self.cellWidth + x
                self.put_pixel(x_axis, y_axis, color)
    def set_border(self, color):
        self.border_color = color
