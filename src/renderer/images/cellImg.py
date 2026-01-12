from mlx.mlx import Mlx
from maze.cell import Cell
from renderer.images.image import Image

class CellsImage(Image):
    def __init__(
        self,
        mlx: Mlx,
        mlx_ptr,
        width: int,
        height: int,
        cell_width: int = 30,
        cell_height: int = 30,
    ):
        super().__init__(mlx, mlx_ptr, width, height)
        self.cellWidth = cell_width
        self.cellHeight = cell_height
        self.cellBorder = int(self.cellHeight * 0.15)

    def draw_cell(self, i, j, cell: Cell, backgroundColor=None):
        # draw north wall
        if backgroundColor is not None:
            for x in range(self.cellBorder, self.cellWidth):
                for y in range(self.cellBorder, self.cellHeight):
                    x_axis = i * self.cellWidth + x
                    y_axis = j * self.cellHeight + y
                    self.put_pixel(x_axis, y_axis, backgroundColor)
        if cell.north:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i)
                    y_axis = (j * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)
        else:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i)
                    y_axis = (j * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0x0000000)

        # draw south wall
        if cell.south:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i)
                    y_axis = (j * self.cellHeight) + y + self.cellHeight
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)
        else:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i)
                    y_axis = (j * self.cellHeight) + y + self.cellHeight
                    self.put_pixel(x_axis, y_axis, 0x0000000)

        # draw west wall
        if cell.west:
            for y in range(self.cellHeight):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i)
                    y_axis = (j * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)
        else:
            for y in range(self.cellHeight):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i)
                    y_axis = (j * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0x00000000)

        # draw east wall
        if cell.east:
            for y in range(self.cellHeight):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i) + self.cellWidth
                    y_axis = (j * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)
        else:
            for y in range(self.cellHeight):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i) + self.cellWidth
                    y_axis = (j * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0x00000000)
