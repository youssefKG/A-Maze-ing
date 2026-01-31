from maze.maze_state import MazeState
from mlx.mlx import Mlx
from maze.cell import Cell
from renderer.images.image import Image
from renderer.colors import Colors

class Border:
    _colors = [Colors.RED, Colors.BLUE, Colors.GREEN, Colors.PURPLE, Colors.ORANGE]
    _current_color_index = 0
    color = _colors[_current_color_index]

    @classmethod
    def change_color(cls):
        if cls._current_color_index + 1 < len(cls._colors):
            cls._current_color_index += 1
        else:
            cls._current_color_index = 0
        cls.color = cls._colors[cls._current_color_index]

class CellsImage(Image):
    def __init__(self, vertical_cells, horizontal_cells):
        super().__init__()
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.cellWidth = self.set_cell_width()
        self.cellHeight = self.set_cell_height()
        self.cellBorder = int(self.cellHeight * 0.15)
        self.maze_state = MazeState()

    def set_cell_width(self):
        cell_width = int(self.width / self.horizontal_cells)
        return int(cell_width - cell_width / 4)

    def set_cell_height(self):
        cell_height = int(self.height / self.vertical_cells)
        return int(cell_height - cell_height / 4)

    def draw_cell(self, cell: Cell,  backgroundColor=None):
        # draw north wall
        if backgroundColor is not None:
            for y in range(self.cellBorder, self.cellHeight):
                for x in range(self.cellBorder, self.cellWidth ):
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

    def draw_north_wall(self, cell: Cell, color):
        x = cell.x
        y = cell.y
        start = x * self.cellWidth
        end  = (x + 1) * self.cellWidth 
        if not cell.north:
            # west cell
            if x - 1 >= 0:
                west_cell_north_wall = self.maze_state.cells_grid[y][x - 1].west
                if west_cell_north_wall:
                    start += self.cellBorder
            if x + 1 < self.maze_state.vertical_cells:
                east_cell_north_wall = self.maze_state.cells_grid[y][x + 1].east
                if east_cell_north_wall:
                    end -= self.cellBorder
        else:
            color = Colors.GRAY
        for y in range(self.cellBorder):
            for x in range(start, end):
                self.put_pixel(x, y, color)


    def set_border(self, color):
        self.border_color = color
    def set_cell_img(self, cells_img: list[Cell]):
        self.cell_img = cells_img
        return self
