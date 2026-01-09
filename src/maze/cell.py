class Cell:
    def __init__(self, north=True, south=True, east=True, west=True) -> None:
        self.north = north
        self.south = south
        self.east = east
        self.west = west
