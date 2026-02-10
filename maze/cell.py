class Cell:
    def __init__(
        self,
        x: int,
        y: int,
        north: bool = True,
        south: bool = True,
        east: bool = True,
        west: bool = True,
    ) -> None:
        self.north: bool = north
        self.south: bool = south
        self.east: bool = east
        self.west: bool = west
        self.x: int = x
        self.y: int = y
        self.is_visited: bool = False
        self.is_42_cell: bool = False

    def get_walls(self) -> tuple[bool, bool, bool, bool]:
        return (self.north, self.south, self.west, self.east)
