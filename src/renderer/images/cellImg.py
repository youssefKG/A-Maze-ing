from mlx.mlx import Mlx
from maze.cell import Cell
from renderer.images.image import Image
import random

cellsData = []

for x in range(10):
    cells_row = []
    for y in range(10):
        north = random.choice([True, False])
        south = random.choice([True, False])
        west = random.choice([True, False])
        east = random.choice([True, False])
        cells_row.append(Cell(north, west, south, east))
    cellsData.append(cells_row)


class CellsImage(Image):
    def __init__(
            self, mlx: Mlx,
            mlx_ptr, 
            width: int,
            height: int,
            ):
        super().__init__(mlx, mlx_ptr, width, height)
        self.cellWidth = int(self.width / 10 - 10)
        self.cellHeight = int(self.height / 10 - 10)
        print(self.width, self.height)
        self.draw_cells()

    def draw_cells(self):
        for i in range(10):
            for j  in range(10):
                self.draw_walls(i, j)

    def draw_walls(self, i, j):
        if cellsData[i][j].north:
            for x in range(self.cellWidth):
                for y in range(6):
                    self.put_pixel(x + (self.cellWidth * i), (j *
                                                              self.cellHeight)
                                   + y, 0xFFFF0000)
        if cellsData[i][j].south:
            for x in range(self.cellWidth):
                for y in range(6):
                    self.put_pixel(x + (self.cellWidth * i), (j *
                                                              self.cellHeight)
                                   + y + self.cellHeight, 0xFFFF0000)
        if cellsData[i][j].west:
            for y in range(self.cellHeight):
                for x in range(6):
                    self.put_pixel(x + (self.cellWidth * i), (j *
                                                              self.cellHeight)
                                   + y, 0xFFFFFFFF)
        if cellsData[i][j].east:
            for y in range(self.cellHeight):
                for x in range(6):
                    self.put_pixel(x + (self.cellWidth * i) + self.cellWidth ,
                                   (j * self.cellHeight) + y , 0xFFFF0000)
