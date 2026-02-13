"""Maze cell model.

Each cell knows its grid position, wall configuration, and a few flags
used by generation and solving algorithms.
"""


class Cell:
    """Represent a single cell in the maze grid."""

    def __init__(
        self,
        x: int,
        y: int,
        north: bool = True,
        south: bool = True,
        east: bool = True,
        west: bool = True,
    ) -> None:
        """Initialize a cell with coordinates and optional wall states.

        Parameters
        ----------
        x, y:
            Grid coordinates of the cell.
        north, south, east, west:
            Initial presence of each wall; ``True`` means the wall is
            present.
        """
        self.north: bool = north
        self.south: bool = south
        self.east: bool = east
        self.west: bool = west
        self.x: int = x
        self.y: int = y
        self.is_visited: bool = False
        self.is_42_cell: bool = False
