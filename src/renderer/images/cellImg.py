from mlx.mlx import Mlx
from maze.cell import Cell
from renderer.images.image import Image

class CellsImage(Image):
    def __init__(self, mlx: Mlx, mlx_ptr, vertical_cells, horizontal_cells):
        super().__init__(mlx, mlx_ptr)
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.cellWidth = self.set_cell_width()
        self.cellHeight = self.set_cell_height()
        self.cellBorder = int(self.cellHeight * 0.15)

    def set_cell_width(self):
        cell_width = int(Image.width / self.horizontal_cells)
        return int(cell_width - cell_width / 4)

    def set_cell_height(self):
        cell_height = int(Image.height / self.vertical_cells)
        return int(cell_height - cell_height / 4)

    def draw_cell(self, cell: Cell, backgroundColor=None):
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
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)

        # draw south wall
        if cell.south:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x)
                    y_axis = (cell.y * self.cellHeight) + y + self.cellHeight
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)

        # draw west wall
        if cell.west:
            for y in range(self.cellHeight + self.cellBorder):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x)
                    y_axis = (cell.y * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)
        # draw east wall
        if cell.east:
            for y in range(self.cellHeight + self.cellBorder):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * cell.x) + self.cellWidth
                    y_axis = (cell.y * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)

    def clear_cell(self, cell: Cell, color=0x98340EAB):
        for y in range(self.cellHeight):
            for x in range(self.cellWidth):
                y_axis = cell.y * self.cellHeight + y
                x_axis = cell.x * self.cellWidth + x
                self.put_pixel(x_axis, y_axis, color)
