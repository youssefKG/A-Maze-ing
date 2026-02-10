import random
from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Union
from collections import deque


class Algo(ABC):
    def __init__(self, materials: dict[str, Any]) -> None:
        self.materials = materials
        self.hexa = "0123456789ABCDEF"

    @abstractmethod
    def algo_run(self) -> list[tuple[int, int]] | None:
        pass

    @abstractmethod
    def get_index_of_position(self, x: int, y: int) -> int:
        if self.materials['map'][y][x] == '0':
            return 0
        elif self.materials['map'][y][x] == '1':
            return 1
        elif self.materials['map'][y][x] == '2':
            return 2
        elif self.materials['map'][y][x] == '3':
            return 3
        elif self.materials['map'][y][x] == '4':
            return 4
        elif self.materials['map'][y][x] == '5':
            return 5
        elif self.materials['map'][y][x] == '6':
            return 6
        elif self.materials['map'][y][x] == '7':
            return 7
        elif self.materials['map'][y][x] == '8':
            return 8
        elif self.materials['map'][y][x] == '9':
            return 9
        elif self.materials['map'][y][x] == 'A':
            return 10
        elif self.materials['map'][y][x] == 'B':
            return 11
        elif self.materials['map'][y][x] == 'C':
            return 12
        elif self.materials['map'][y][x] == 'D':
            return 13
        elif self.materials['map'][y][x] == 'E':
            return 14
        elif self.materials['map'][y][x] == 'F':
            return 15
        else:
            return -1

    def in_map_quarante_deux(self, x: int, y: int) -> bool:
        r = int((self.materials['height'] / 2)) - 2
        c = int((self.materials['width'] / 2)) - 3
        if y == r and x in [c, c + 4, c + 5, c + 6]:
            return True
        elif y == r + 1 and x in [c, c + 6]:
            return True
        elif y == r + 2 and x in [c, c + 1, c + 2,  c + 4, c + 5, c + 6]:
            return True
        elif y == r + 3 and x in [c + 2, c + 4]:
            return True
        elif y == r + 4 and x in [c + 2, c + 4, c + 5, c + 6]:
            return True
        else:
            return False

    @abstractmethod
    def create_map(self) -> List[list[str]]:
        my_map: List[Any] = []
        for i in range(self.materials['height']):
            cols = []
            for j in range(self.materials['width']):
                cols.append('F')
            my_map.append(cols)
        return my_map


class BFSAlgo(Algo):
    def __init__(
            self,
            materials: dict[str, Union[Tuple, int, str, bool]]
    ) -> None:
        super().__init__(materials)
        self.shortest_path = ''
        self.visited: list[tuple[int, int]] = []

    def get_shortest_path(self, path: List[tuple[int, int]]) -> str:
        x = -1
        y = -1
        for t in path:
            current_x, current_y = t
            if x < 0 or y < 0:
                x, y = current_x, current_y
            else:
                res_x, res_y = current_x - x, current_y - y
                x, y = current_x, current_y
                if res_x == 0 and res_y == -1:
                    self.shortest_path += 'N'
                elif res_x == 1 and res_y == 0:
                    self.shortest_path += 'E'
                elif res_x == 0 and res_y == 1:
                    self.shortest_path += 'S'
                else:
                    self.shortest_path += 'W'
        return self.shortest_path

    def algo_run(self) -> Any:
        queue: deque = deque()
        queue.append((self.materials['entry'], [self.materials['entry']]))
        self.visited.append(self.materials['entry'])
        while len(queue):
            current, path = queue.popleft()
            if current == self.materials['exit']:
                self.get_shortest_path(path)
                return path
            dirs = self.get_valid_neighboors(current)
            for dir in dirs:
                if dir == 'north':
                    new_x = current[0]
                    new_y = current[1] - 1
                elif dir == 'east':
                    new_x = current[0] + 1
                    new_y = current[1]
                elif dir == 'south':
                    new_x = current[0]
                    new_y = current[1] + 1
                else:
                    new_x = current[0] - 1
                    new_y = current[1]
                if (new_x, new_y) not in self.visited:
                    self.visited.append((new_x, new_y))
                    new_path = list(path)
                    new_path.append((new_x, new_y))
                    queue.append(((new_x, new_y), new_path))
        return []

    def get_valid_neighboors(self, position: Tuple) -> List[str]:
        directions = list(self.materials['directions'])
        x, y = position
        index = self.get_index_of_position(x, y)
        return self.remove_direction_to_wall(directions, index)

    def remove_direction_to_wall(
        self,
        directions: List[str],
        index: int
    ) -> List[str]:
        if index >= 8:
            index -= 8
            directions.remove('west')
        if index >= 4:
            index -= 4
            directions.remove('south')
        if index >= 2:
            index -= 2
            directions.remove('east')
        if index >= 1:
            index -= 1
            directions.remove('north')
        return directions

    def get_index_of_position(self, x: int, y: int) -> int:
        return super().get_index_of_position(x, y)

    def create_map(self) -> list[list[str]]:
        return super().create_map()


class DFSAlgo(Algo):
    #  the constructor of class
    def __init__(self, materials: dict[str, Any]) -> None:
        super().__init__(materials)
        self.materials['map'] = self.create_map()
        self.unvisited = self.get_all_cells()
        self.visited: list[tuple[int, int]] = []

    def get_all_cells(self) -> List[Tuple]:
        unvisited = list()
        for y in range(0, self.materials['height']):
            for x in range(0, self.materials['width']):
                unvisited.append((x, y))
        return unvisited

    #  DFS is executed to to made  perfect map
    def algo_run(self) -> list[Any]:

        if self.materials['is_42'] is True:
            self.put_cells_42_as_visited()

        curr_cell = (0, 0)
        stack = [curr_cell]
        self.visited.append(curr_cell)
        self.unvisited.remove(curr_cell)

        while len(stack):
            curr_cell = stack[-1]
            neighbor = self.get_neighboors_from_unvisited(curr_cell)
            if neighbor:
                next_cell = neighbor
                self.remove_walls(curr_cell, next_cell)
                stack.append(next_cell)
                self.visited.append(next_cell)
            else:
                curr_cell = stack.pop()
        #  for imperfect maze
        if not self.materials['perfect'] \
            and self.materials['height'] > 1 and self.materials['width'] > 1:
            self.remove_for_imperfect()

        return []

    # for imperfect maze:
    def remove_for_imperfect(self) -> None:
        for y in range(0, self.materials['height']):
            for x in range(0, self.materials['width']):
                index: int = self.get_index_of_position(x, y)
                walls: list[Any] = self.get_walls_of_index(index, x, y)
                if index in [14, 13, 11, 7] and len(walls):
                    wall = random.choice(walls)
                    if wall == 'north':
                        self.materials['map'][y][x] = self.hexa[index - 1]
                        index_2 = self.get_index_of_position(x, y - 1)
                        self.materials['map'][y - 1][x] = self.hexa[index_2 - 4]
                    elif wall == 'east':
                        self.materials['map'][y][x] = self.hexa[index - 2]
                        index_2 = self.get_index_of_position(x + 1, y)
                        self.materials['map'][y][x + 1] = self.hexa[index_2 - 8]
                    elif wall == 'south':
                        self.materials['map'][y][x] = self.hexa[index - 4]
                        index_2 = self.get_index_of_position(x, y + 1)
                        self.materials['map'][y + 1][x] = self.hexa[index_2 - 1]
                    else:
                        self.materials['map'][y][x] = self.hexa[index - 8]
                        index_2 = self.get_index_of_position(x - 1, y)
                        self.materials['map'][y][x - 1] = self.hexa[index_2 - 2]
                    return
    
    def get_walls_of_index(self, index: int, x: int, y: int) -> list[Any]:
        walls: list[Any] = []

        for i in range(4):
            if index >> i & 1:
                if i == 0 and y != 0:
                    walls.append('north')
                elif i == 1 and x != self.materials['width'] - 1:
                    walls.append('east')
                elif i == 2 and y != self.materials['height'] - 1:
                    walls.append('south')
                elif i == 3 and x != 0:
                    walls.append('west')
        return walls

    #  remove walls between two cells (cell, neighbor)
    def remove_walls(
        self,
        cell: Tuple[int, int],
        neighboor: Tuple[int, int]
    ) -> None:
        cell_x, cell_y = cell
        neigh_x, neigh_y = neighboor

        idx_c = self.get_index_of_position(cell_x, cell_y)
        idx_n = self.get_index_of_position(neigh_x, neigh_y)

        if cell_x > neigh_x:
            self.materials['map'][cell_y][cell_x] = self.hexa[idx_c - 8]
            self.materials['map'][neigh_y][neigh_x] = self.hexa[idx_n - 2]
        elif cell_x < neigh_x:
            self.materials['map'][cell_y][cell_x] = self.hexa[idx_c - 2]
            self.materials['map'][neigh_y][neigh_x] = self.hexa[idx_n - 8]
        else:
            if cell_y > neigh_y:
                self.materials['map'][cell_y][cell_x] = self.hexa[idx_c - 1]
                self.materials['map'][neigh_y][neigh_x] = self.hexa[idx_n - 4]
            else:
                self.materials['map'][cell_y][cell_x] = self.hexa[idx_c - 4]
                self.materials['map'][neigh_y][neigh_x] = self.hexa[idx_n - 1]

    #  get neighboors from unvisited only valid
    def get_neighboors_from_unvisited(
        self,
        position: Tuple
    ) -> Tuple[int, int] | None:
        neighboors = list()
        x, y = position

        if y - 1 >= 0:
            north = (x, y - 1)
            if north not in self.visited:
                neighboors.append(north)
        if y + 1 < self.materials['height']:
            south = (x, y + 1)
            if south not in self.visited:
                neighboors.append(south)
        if x + 1 < self.materials['width']:
            east = (x + 1, y)
            if east not in self.visited:
                neighboors.append(east)
        if x - 1 >= 0:
            west = (x - 1, y)
            if west not in self.visited:
                neighboors.append(west)
        if len(neighboors):
            return random.choice(neighboors)
        return None

    #  if map has 42 set cells as visited and rmeove it from unvisited
    def put_cells_42_as_visited(self) -> None:
        for y in range(self.materials['height']):
            for x in range(self.materials['width']):
                if self.in_map_quarante_deux(x, y):
                    self.visited.append((x, y))
                    self.unvisited.remove((x, y))

    #  check if this direction go throw the map 42 in middle map
    def in_map_quarante_deux(self, new_x: int, new_y: int) -> bool:
        return super().in_map_quarante_deux(new_x, new_y)

    #  get index from map
    def get_index_of_position(self, x: int, y: int) -> int:
        return super().get_index_of_position(x, y)

    #  create new_map with walls
    def create_map(self) -> List[list[str]]:
        return super().create_map()


class WilsonAlgo(Algo):
    def __init__(
        self,
        materials: dict[str, Union[Tuple, int, str, bool]]
    ) -> None:
        super().__init__(materials)
        self.materials["map"] = self.create_map()
        self.visited: list[tuple[int, int]] = list()
        self.unvisited = self.get_all_cells()

    def create_map(self) -> List[List[str]]:
        return super().create_map()

    def remove_map_quarante_deux(self) -> None:
        if self.materials["height"] < 6 or self.materials["width"] < 8:
            return
        i = 0
        while i < self.materials["height"]:
            j = 0
            while j < self.materials["width"]:
                if self.in_map_quarante_deux(j, i):
                    self.unvisited.remove((j, i))
                j += 1
            i += 1

    def algo_run(self) -> list[tuple[int, int]] | None:
        if self.materials["is_42"]:
            self.remove_map_quarante_deux()
        target_cell = random.choice(self.unvisited)
        self.visited.append(target_cell)
        self.unvisited.remove(target_cell)
        while len(self.unvisited):
            path = []
            current = random.choice(self.unvisited)
            path.append(current)
            while current not in self.visited:
                next: tuple[int, int] | None = \
                    self.get_rand_valid_neighboors(current)
                if not next:
                    return []
                try:
                    loop_index: int = path.index(next)
                    path = path[: loop_index + 1]
                except Exception:
                    path.append(next)
                current = next
            self.remove_walls_of_path(path)
            for cell in path:
                self.visited.append(cell)
                if cell in self.unvisited:
                    self.unvisited.remove(cell)

        if not self.materials['perfect'] \
            and self.materials['height'] > 1 and self.materials['width'] > 1:
            self.remove_for_imperfect()

        return []

    def remove_for_imperfect(self) -> None:
        for y in range(0, self.materials['height']):
            for x in range(0, self.materials['width']):
                index: int = self.get_index_of_position(x, y)
                walls: list[Any] = self.get_walls_of_index(index, x, y)
                if index in [14, 13, 11, 7] and len(walls):
                    wall = random.choice(walls)
                    if wall == 'north':
                        self.materials['map'][y][x] = self.hexa[index - 1]
                        index_2 = self.get_index_of_position(x, y - 1)
                        self.materials['map'][y - 1][x] = self.hexa[index_2 - 4]
                    elif wall == 'east':
                        self.materials['map'][y][x] = self.hexa[index - 2]
                        index_2 = self.get_index_of_position(x + 1, y)
                        self.materials['map'][y][x + 1] = self.hexa[index_2 - 8]
                    elif wall == 'south':
                        self.materials['map'][y][x] = self.hexa[index - 4]
                        index_2 = self.get_index_of_position(x, y + 1)
                        self.materials['map'][y + 1][x] = self.hexa[index_2 - 1]
                    else:
                        self.materials['map'][y][x] = self.hexa[index - 8]
                        index_2 = self.get_index_of_position(x - 1, y)
                        self.materials['map'][y][x - 1] = self.hexa[index_2 - 2]
                    return

    def get_walls_of_index(self, index: int, x: int, y: int) -> list[Any]:
        walls: list[Any] = []

        for i in range(4):
            if index >> i & 1:
                if i == 0 and y != 0:
                    walls.append('north')
                elif i == 1 and x != self.materials['width'] - 1:
                    walls.append('east')
                elif i == 2 and y != self.materials['height'] - 1:
                    walls.append('south')
                elif i == 3 and x != 0:
                    walls.append('west')
        return walls

    def remove_walls_of_path(self, path: List[tuple]) -> None:

        map = self.materials["map"]
        for i in range(0, len(path) - 1):
            curr_x, curr_y = path[i]
            next_x, next_y = path[i + 1]
            if curr_x > next_x:
                index = self.get_index_of_position(curr_x, curr_y)
                map[curr_y][curr_x] = self.hexa[index - 8]
                index = self.get_index_of_position(next_x, next_y)
                self.materials["map"][next_y][next_x] = self.hexa[index - 2]
            elif curr_x < next_x:
                index = self.get_index_of_position(curr_x, curr_y)
                map[curr_y][curr_x] = self.hexa[index - 2]
                index = self.get_index_of_position(next_x, next_y)
                map[next_y][next_x] = self.hexa[index - 8]
            else:
                if curr_y > next_y:
                    index = self.get_index_of_position(curr_x, curr_y)
                    map[curr_y][curr_x] = self.hexa[index - 1]
                    index = self.get_index_of_position(next_x, next_y)
                    map[next_y][next_x] = self.hexa[index - 4]
                else:
                    index = self.get_index_of_position(curr_x, curr_y)
                    map[curr_y][curr_x] = self.hexa[index - 4]
                    index = self.get_index_of_position(next_x, next_y)
                    map[next_y][next_x] = self.hexa[index - 1]

    def get_rand_valid_neighboors(
        self,
        position: Tuple
    ) -> Tuple[int, int] | None:
        x, y = position
        directions = list()

        if y - 1 >= 0:
            if not self.materials["is_42"]:
                north = (x, y - 1)
                directions.append(north)
            else:
                if not self.in_map_quarante_deux(x, y - 1):
                    north = (x, y - 1)
                    directions.append(north)
        if y + 1 < self.materials["height"]:
            if not self.materials["is_42"]:
                south = (x, y + 1)
                directions.append(south)
            else:
                if not self.in_map_quarante_deux(x, y + 1):
                    south = (x, y + 1)
                    directions.append(south)
        if x + 1 < self.materials["width"]:
            if not self.materials["is_42"]:
                east = (x + 1, y)
                directions.append(east)
            else:
                if not self.in_map_quarante_deux(x + 1, y):
                    east = (x + 1, y)
                    directions.append(east)
        if x - 1 >= 0:
            if not self.materials["is_42"]:
                west = (x - 1, y)
                directions.append(west)
            else:
                if not self.in_map_quarante_deux(x - 1, y):
                    west = (x - 1, y)
                    directions.append(west)

        if len(directions):
            return random.choice(directions)
        return None

    def in_map_quarante_deux(self, new_x: int, new_y: int) -> bool:
        return super().in_map_quarante_deux(new_x, new_y)

    def get_all_cells(self) -> List[Tuple]:
        not_visited = list()
        for y in range(0, self.materials["height"]):
            for x in range(0, self.materials["width"]):
                not_visited.append((x, y))
        return not_visited

    def get_index_of_position(self, x: int, y: int) -> int:
        return super().get_index_of_position(x, y)


class MazeGenerator:
    def __init__(
        self,
        width: int,
        height: int,
        entry: Tuple[int, int],
        exit: Tuple[int, int],
        seed: int,
        filename: str,
        perfect: bool
    ) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.number_seed = seed
        self.output_file = filename
        self.is_perfect = perfect
        self.map: list[list[str]] = []
        self.shortest_path: str = ""
        self.is_42 = self.logo_in_map()
        self.hexa = "0123456789ABCEDF"
        random.seed(seed)

    def logo_in_map(self) -> bool:
        if self.height > 6 and self.width > 8:
            return True
        return False

    def create_map(self) -> List[str]:
        my_map: List[Any] = []
        for i in range(self.height):
            cols = []
            for j in range(self.width):
                cols.append("F")
            my_map.append(cols)
        return my_map

    def generate(self, name_algo: str) -> None:
        if name_algo == "dfs":
            dfs = DFSAlgo(
                {
                    "width": self.width,
                    "height": self.height,
                    "entry": self.entry,
                    "exit": self.exit,
                    "is_42": self.is_42,
                    "perfect": self.is_perfect,
                    "hexa": self.hexa,
                    "directions": ("north", "east", "south", "west"),
                }
            )

            dfs.algo_run()
            self.map = dfs.materials["map"]
            bfs = BFSAlgo(
                {
                    "width": self.width,
                    "height": self.height,
                    "entry": self.entry,
                    "exit": self.exit,
                    "is_42": self.is_42,
                    "map": dfs.materials["map"],
                    "hexa": self.hexa,
                    "directions": ("north", "east", "south", "west"),
                }
            )
            bfs.algo_run()
            self.shortest_path = bfs.shortest_path
            self.create_output_file()

        elif name_algo == "wilson":
            wilson = WilsonAlgo(
                {
                    "width": self.width,
                    "height": self.height,
                    "entry": self.entry,
                    "exit": self.exit,
                    "is_42": self.is_42,
                    "perfect": self.is_perfect,
                    "hexa": self.hexa,
                    "directions": ("north", "east", "south", "west"),
                }
            )
            wilson.algo_run()
            self.map = wilson.materials["map"]
            bfs = BFSAlgo(
                {
                    "width": self.width,
                    "height": self.height,
                    "entry": self.entry,
                    "exit": self.exit,
                    "is_42": self.is_42,
                    "map": wilson.materials["map"],
                    "hexa": self.hexa,
                    "directions": ("north", "east", "south", "west"),
                }
            )
            bfs.algo_run()
            self.shortest_path = bfs.shortest_path
            self.create_output_file()

    def create_output_file(self) -> None:
        try:
            with open(self.output_file, "w") as file:
                for row in self.map:
                    for col in row:
                        file.write(col)
                file.write("\n")
                file.write("\n(")
                file.write(str(self.entry[0]))
                file.write(",")
                file.write(str(self.entry[1]))
                file.write(")\n(")
                file.write(str(self.exit[0]))
                file.write(",")
                file.write(str(self.exit[1]))
                file.write(")\n")
                file.write(self.shortest_path)
                file.write("\n")
        except Exception as e:
            print(e)

    def get_map(self) -> List[Any]:
        return self.map

    def get_solution(self) -> str:
        return self.shortest_path
