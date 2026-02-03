from typing import Any, List, Dict
import sys


class Parser:
    def __init__(self, argv: str) -> None:
        self.filename = argv
        self.width = 0
        self.height = 0
        self.entry = tuple()
        self.exit = tuple()
        self.output_file = ''
        self.perfect = False
        self.content_file = ''
        self.is_42_cells = False
        self.seed = 0

    def read_file(self) -> None:
        try:
            with open(self.filename, 'r') as file:
                self.content_file = file.read()
        except Exception as e:
            print(e)
            sys.exit(42)

    def parse_content_file(self) -> bool:
        try:
            lines = self.content_file.split('\n')
            for line in lines:
                if line == '' or line[0] == '#':
                    continue
                splitted = line.strip().split('=')
                if splitted[0] in 'WIDTH':
                    self.width = int(splitted[1])
                    if self.width <= 0:
                        raise Exception("Width must be greather than 0")
                elif splitted[0] == 'HEIGHT':
                    self.height = int(splitted[1])
                    if self.height <= 0:
                        raise Exception("height must be greather than 0")
                elif splitted[0] == 'ENTRY':
                    coord = splitted[1].split(',')
                    self.entry = (int(coord[0]), int(coord[1]))
                    if self.entry[0] < 0 or self.entry[0] >= self.width:
                        raise Exception("entry must be inside the map")
                    elif self.entry[1] < 0 or self.entry[1] >= self.height:
                        raise Exception("entry must be inside the map")
                elif splitted[0] == 'EXIT':
                    coord = splitted[1].split(',')
                    self.exit = (int(coord[0]), int(coord[1]))
                    if self.exit[0] < 0 or self.exit[0] >= self.width:
                        raise Exception("exit must be inside the map")
                    elif self.exit[1] < 0 or self.exit[1] >= self.height:
                        raise Exception("exit must be inside the map")
                elif splitted[0] == 'OUTPUT_FILE':
                    self.output_file = splitted[1]
                elif splitted[0] == 'PERFECT':
                    if splitted[1] == 'True':
                        self.perfect = True
                    elif splitted[1] == 'False':
                        self.perfect = False
                    else:
                        raise Exception("perfect muse be boolean True or False")
                elif splitted[0] == 'SEED':
                    self.seed = int(splitted[1])
                else:
                    raise Exception("Invalid key!!, please check config file!")
            if self.height > 6 and self.width > 8:
                self.is_42_cells = True
            x, y = self.entry
            if self.in_map_quarante_deux(x, y) and self.is_42_cells:
                raise Exception("coordinates entry is inside The 42")
            x, y = self.exit
            if self.in_map_quarante_deux(x, y) and self.is_42_cells:
                raise Exception("coordinates exit is inside the 42")
            return True
        except Exception as e:
            print(e)
            return False

    # check if this direction go throw the map 42 in middle map
    def in_map_quarante_deux(self, x: int, y: int) -> bool:
        middle_height = int((self.height / 2)) - 2
        middle_width = int((self.width / 2)) - 3
        if y == middle_height and x in [middle_width, middle_width + 4, middle_width + 5, middle_width + 6]:
            return True
        elif y == middle_height + 1 and x in [middle_width, middle_width + 6]:
            return True
        elif y == middle_height + 2 and x in [middle_width, middle_width + 1, middle_width + 2,  middle_width + 4, middle_width + 5, middle_width + 6]:
            return True
        elif y == middle_height + 3 and x in [middle_width + 2, middle_width + 4]:
            return True
        elif y == middle_height + 4 and x in [middle_width + 2, middle_width + 4, middle_width + 5, middle_width + 6]:
            return True
        else:
            return False

    def create_materials(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
            'entry': self.entry,
            'exit': self.exit,
            'seed': self.seed,
            "is_42": self.is_42_cells,
            'perfect': self.perfect,
            'hexa': "0123456789ABCEDF",
            'directions': ['north', 'east', 'south', 'west']
        }

    def create_output_file(self, map: List[Any], shortest_path) -> None:
        try:
            with open(self.output_file, 'w') as file:
                for row in map:
                    for col in row:
                        file.write(col)
                    file.write('\n')
                file.write('\n(')
                file.write(str(self.entry[0]))
                file.write(',')
                file.write(str(self.entry[1]))
                file.write(')\n(')
                file.write(str(self.exit[0]))
                file.write(',')
                file.write(str(self.exit[1]))
                file.write(')\n')
                file.write(shortest_path)
                file.write('\n')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    parser = Parser(sys.argv[1])
    # print(parser.filename, "\n00000000000000")
    parser.read_file()
    if not parser.parse_content_file():
        sys.exit(1)
    materials = parser.create_materials()
    for k, v in materials.items():
        print(k, ":", v)
