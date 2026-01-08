from mlx.mlx import Mlx
from maze.cell import Cell
from renderer.images.image import Image

class CellImage(Image):
    def __init__(
            self, mlx: Mlx,
            mlx_ptr, 
            width: int,
            height: int,
            cell: Cell
            ) -> None:
        super().__init__(mlx, mlx_ptr, width, height)
        self.cell = cell
        self.draw_west_wall()
        self.draw_south_wall()
        self.draw_east_wall()
        self.draw_north_wall()


    def draw_north_wall(self):
        if self.cell.north:
            for x in range(self.width):
                for y in range(4):
                    self.put_pixel(x, y)

    def draw_south_wall(self):
        if self.cell.south:
            for x in range(self.width):
                for y in range(4):
                    self.put_pixel(x, self.height + y - 4)

    def draw_west_wall(self):
        if self.cell.west:
            for y in range(self.height):
                for x in range(4):
                    self.put_pixel(x, y)

    def draw_east_wall(self):
        if self.cell.east:
            for y in range(self.height):
                for x in range(4):
                    self.put_pixel(self.width - 4 + x, y)
