class Cell:
    def __init__(self, x: int, y: int, north=True, south=True, east=True,
            west=True) -> None:
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.is_visited = False
        self.x = x
        self.y = y

    def remove_wall(self, wall: str, value: bool) -> None:
        match wall:
            case "north":
                self.north = value
            case "south":
                self.south = value
            case "east":
                self.east = value
            case "west":
                self.west = value
