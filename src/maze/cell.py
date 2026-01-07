class CellWalls:
    def __init__(self, north, south, east, west) -> None:
        self.north = north
        self.south = south
        self.east = east
        self.west = west

class Cell:
    def __init__(self, width: int, height: int, walls: CellWalls) -> None:
        self.width = width
        self.height =height
        self.walls  = walls
