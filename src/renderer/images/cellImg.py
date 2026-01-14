from mlx.mlx import Mlx
from maze.cell import Cell
from renderer.images.image import Image
from random import choice

class CellsImage(Image):
    def __init__(self, mlx: Mlx, mlx_ptr, width=1200, height=1200):
        super().__init__(mlx, mlx_ptr, width, height)
        self.vertical_cells = 10
        self.horizontal_cells = 10
        self.cellWidth = self.set_cell_width()
        self.cellHeight = self.set_cell_height()
        self.cellBorder = int(self.cellHeight * 0.15)
        self.color = choice([ 0x1E1E1EFF, 0x2C2C54FF,  0x3B2F2FFF, 0x1B3A4BFF, 0x2F3E2EFF, 0x3A1F2BFF, 0x4B3621FF, 0x262626FF])

    def set_cell_width(self):
        cell_width = int(self.width / self.horizontal_cells)
        return int(cell_width - cell_width / 4)

    def set_cell_height(self):
        cell_height = int(self.height / self.vertical_cells)
        return int(cell_height - cell_height / 4)

    def draw_cell(self, cell: Cell, backgroundColor=None):
        # draw north wall
        if backgroundColor is not None:
            for y in range(self.cellHeight):
                for x in range(self.cellBorder, self.cellWidth):
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

    def clear_cell(self, cell: Cell):
        for x in range(self.cellWidth):
            for y in range(self.cellHeight):
                x_axis = cell.y * self.cellWidth + x
                y_axis = cell.x * self.cellHeight + y
                self.put_pixel(x_axis, y_axis, self.color)
