from mlx.mlx import Mlx
from maze.cell import Cell
from renderer.images.image import Image

class CellsImage(Image):
    def __init__(
            self, mlx: Mlx,
            mlx_ptr, 
            width: int,
            height: int,
            cell_width: int = 30,
            cell_height: int = 30
            ):
        super().__init__(mlx, mlx_ptr, width, height)
        self.cellWidth = cell_width
        self.cellHeight = cell_height
        self.cellBorder = int(self.cellHeight * 0.20)


    def draw_walls(self, i, j, cell: Cell):
        # draw north wall
        if cell.north:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i)
                    y_axis = (j * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)

        #draw south wall
        if cell.south:
            for x in range(self.cellWidth + self.cellBorder):
                for y in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i)
                    y_axis =(j * self.cellHeight)+ y + self.cellHeight
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)

        #draw west wall
        if cell.west:
            for y in range(self.cellHeight):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i)
                    y_axis = (j * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)

        # draw east wall
        if cell.east:
            for y in range(self.cellHeight):
                for x in range(self.cellBorder):
                    x_axis = x + (self.cellWidth * i) + self.cellWidth
                    y_axis = (j * self.cellHeight) + y
                    self.put_pixel(x_axis, y_axis, 0xFFFFFFFF)
