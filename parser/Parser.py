from typing import Any, Dict
import sys


class Parser:
    """
    Configuration file parser for the maze generator.

    This class reads and validates a configuration file,
    extracts all maze parameters, performs consistency checks,
    and builds a materials dictionary used by the maze algorithms.
    """
    def __init__(self, argv: list[str]) -> None:
        """
        Initialize the parser using command-line arguments.

        Args:
            argv (list[str]): Command-line arguments.
                Expected format:
                ["program_name", "config.txt"]

        Raises:
            SystemExit: If the number of arguments is invalid.
        """
        try:
            if len(argv) != 2:
                e = "Usage: python3 a_maze_ing.py config.txt"
                raise ValueError(e)
        except ValueError as e:
            print(e)
            sys.exit(42)
        self.filename = argv[1]
        self.width = 11
        self.height = 11
        self.entry = (0, 0)
        self.exit = (10, 10)
        self.output_file = ""
        self.perfect = False
        self.content_file = ""
        self.is_42_cells = False
        self.seed = 0

    def parse(self) -> Dict[str, Any]:
        """
        Parse the configuration file and return validated materials.

        Returns:
            Dict[str, Any]: Dictionary containing all validated
                configuration parameters for maze generation.

        Raises:
            SystemExit: If parsing fails.
        """
        self.read_file()
        if not self.parse_content_file():
            sys.exit(42)
        return self.create_materials()

    def read_file(self) -> None:
        """
        Read the configuration file content.

        Raises:
            SystemExit: If the file cannot be opened or read.
        """
        try:
            with open(self.filename, "r") as file:
                self.content_file = file.read()
        except Exception as e:
            print(e)
            sys.exit(42)

    def parse_content_file(self) -> bool:
        """
        Parse and validate configuration file content.

        Supported keys:
            - WIDTH
            - HEIGHT
            - ENTRY (format: x,y)
            - EXIT (format: x,y)
            - OUTPUT_FILE
            - PERFECT (True or False)
            - SEED

        Validation includes:
            - Positive dimensions
            - Entry and exit inside bounds
            - Entry and exit not overlapping
            - Entry/exit not inside reserved "42" logo area
              (if applicable)

        Returns:
            bool: True if parsing succeeds, False otherwise.
        """
        try:
            lines = self.content_file.split("\n")
            for line in lines:
                line = line.strip()
                if line == "" or line[0] == "#":
                    continue
                splitted = line.split("=")
                if splitted[0] in "WIDTH":
                    self.width = int(splitted[1])
                    if self.width <= 0:
                        raise Exception("Width must be greather than 0")
                elif splitted[0] == "HEIGHT":
                    self.height = int(splitted[1])
                    if self.height <= 0:
                        raise Exception("height must be greather than 0")
                elif splitted[0] == "ENTRY":
                    coord = splitted[1].split(",")
                    if len(coord) != 2:
                        raise ValueError("incorrect tuple of entry!")
                    self.entry = (int(coord[0]), int(coord[1]))
                    if self.entry[0] < 0 or self.entry[0] >= self.width:
                        raise Exception("entry must be inside the map")
                    elif self.entry[1] < 0 or self.entry[1] >= self.height:
                        raise Exception("entry must be inside the map")
                elif splitted[0] == "EXIT":
                    coord = splitted[1].split(",")
                    if len(coord) != 2:
                        raise ValueError("incorrect tuple of exit")
                    self.exit = (int(coord[0]), int(coord[1]))
                    if self.exit[0] < 0 or self.exit[0] >= self.width:
                        raise Exception("exit must be inside the map")
                    elif self.exit[1] < 0 or self.exit[1] >= self.height:
                        raise Exception("exit must be inside the map")
                elif splitted[0] == "OUTPUT_FILE":
                    self.output_file = splitted[1].strip("'")
                    self.output_file = splitted[1].strip('"')
                elif splitted[0] == "PERFECT":
                    if splitted[1] == "True":
                        self.perfect = True
                    elif splitted[1] == "False":
                        self.perfect = False
                    else:
                        e = "perfect must be boolean True or False"
                        raise Exception(e)
                elif splitted[0] == "SEED":
                    self.seed = int(splitted[1])
                else:
                    e = "Invalid key!!, please check config file!"
                    raise Exception(e)
            if self.height > 6 and self.width > 8:
                self.is_42_cells = True

            x, y = self.entry
            if self.in_map_quarante_deux(x, y) and self.is_42_cells:
                raise Exception("coordinates entry is inside The 42")
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                raise ValueError("entry must be inside the map")

            x, y = self.exit
            if self.in_map_quarante_deux(x, y) and self.is_42_cells:
                raise Exception("coordinates exit is inside the 42")
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                raise ValueError("exit must be inside the map")
            if self.entry[0] == self.exit[0] and self.entry[1] == self.exit[1]:
                raise ValueError("exit and entry in same cell")
            return True
        except Exception as e:
            print(e)
            return False

    # check if this direction go throw the map 42 in middle map
    def in_map_quarante_deux(self, x: int, y: int) -> bool:
        """
            Check whether a coordinate belongs to the reserved "42" logo area.

            The logo is dynamically centered in the maze grid.

            Args:
                x (int): X-coordinate.
                y (int): Y-coordinate.

            Returns:
                bool: True if the position is inside the 42 logo area.
        """
        mid_h = int((self.height / 2)) - 2
        mid_w = int((self.width / 2)) - 3
        row_2 = [mid_w, mid_w + 1, mid_w + 2, mid_w + 4, mid_w + 5, mid_w + 6]
        row_4 = [mid_w + 2, mid_w + 4, mid_w + 5, mid_w + 6]

        if y == mid_h and x in [mid_w, mid_w + 4, mid_w + 5, mid_w + 6]:
            return True
        elif y == mid_h + 1 and x in [mid_w, mid_w + 6]:
            return True
        elif y == mid_h + 2 and x in row_2:
            return True
        elif y == mid_h + 3 and x in [mid_w + 2, mid_w + 4]:
            return True
        elif y == mid_h + 4 and x in row_4:
            return True
        else:
            return False

    def create_materials(self) -> Dict[str, Any]:
        """
        Build the materials dictionary used by maze algorithms.

        Returns:
            Dict[str, Any]: Fully prepared configuration dictionary.
        """
        return {
            "width": self.width,
            "height": self.height,
            "entry": self.entry,
            "exit": self.exit,
            "seed": self.seed,
            "is_42": self.is_42_cells,
            "output_file": self.output_file,
            "perfect": self.perfect,
            "hexa": "0123456789ABCEDF",
            "directions": ["north", "east", "south", "west"],
        }
