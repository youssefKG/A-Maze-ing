import random
from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Union
from collections import deque


class Algo(ABC):
    """
        Abstract base class for maze algorithms.

        This class defines the common interface and shared utility methods
        used by all maze generation and solving algorithms.

        Attributes:
            materials (dict): Configuration dictionary containing maze
                parameters such as width, height, map, entry, exit, etc.
            hexa (str): String of hexadecimal characters used to encode walls.
    """
    def __init__(self, materials: dict[str, Any]) -> None:
        """
            Initialize the algorithm with configuration materials.

            Args:
                materials (dict[str, Any]): Dictionary containing maze metadata
                    and runtime parameters.
        """
        self.materials = materials
        self.hexa = "0123456789ABCDEF"

    @abstractmethod
    def algo_run(self) -> list[tuple[int, int]] | None:
        """
            Execute the algorithm.

            Returns:
                list[tuple[int, int]] | None:
                    Path of coordinates if applicable, otherwise None.
        """
        pass

    @abstractmethod
    def get_index_of_position(self, x: int, y: int) -> int:
        """
            Return the wall-encoding index of a cell at position (x, y).

            Each cell stores walls encoded as a hexadecimal character.
            This method converts that character into its integer value.

            Args:
                x (int): X-coordinate.
                y (int): Y-coordinate.

            Returns:
                int: Integer representation of the cell's wall encoding.
        """
        if self.materials["map"][y][x] == "0":
            return 0
        elif self.materials["map"][y][x] == "1":
            return 1
        elif self.materials["map"][y][x] == "2":
            return 2
        elif self.materials["map"][y][x] == "3":
            return 3
        elif self.materials["map"][y][x] == "4":
            return 4
        elif self.materials["map"][y][x] == "5":
            return 5
        elif self.materials["map"][y][x] == "6":
            return 6
        elif self.materials["map"][y][x] == "7":
            return 7
        elif self.materials["map"][y][x] == "8":
            return 8
        elif self.materials["map"][y][x] == "9":
            return 9
        elif self.materials["map"][y][x] == "A":
            return 10
        elif self.materials["map"][y][x] == "B":
            return 11
        elif self.materials["map"][y][x] == "C":
            return 12
        elif self.materials["map"][y][x] == "D":
            return 13
        elif self.materials["map"][y][x] == "E":
            return 14
        elif self.materials["map"][y][x] == "F":
            return 15
        else:
            return -1

    def in_map_quarante_deux(self, x: int, y: int) -> bool:
        """
            Determine whether a coordinate belongs to the embedded "42" logo
            shape located at the center of the maze.

            Args:
                x (int): X-coordinate.
                y (int): Y-coordinate.

            Returns:
                bool: True if the position belongs to the logo shape.
        """
        r = int((self.materials["height"] / 2)) - 2
        c = int((self.materials["width"] / 2)) - 3
        if y == r and x in [c, c + 4, c + 5, c + 6]:
            return True
        elif y == r + 1 and x in [c, c + 6]:
            return True
        elif y == r + 2 and x in [c, c + 1, c + 2, c + 4, c + 5, c + 6]:
            return True
        elif y == r + 3 and x in [c + 2, c + 4]:
            return True
        elif y == r + 4 and x in [c + 2, c + 4, c + 5, c + 6]:
            return True
        else:
            return False

    @abstractmethod
    def create_map(self) -> List[list[str]]:
        """
            Create an initialized maze map filled with walls ('F').

            Returns:
                List[list[str]]: 2D grid representing the maze.
        """
        my_map: List[Any] = []
        for i in range(self.materials["height"]):
            cols = []
            for j in range(self.materials["width"]):
                cols.append("F")
            my_map.append(cols)
        return my_map


class BFSAlgo(Algo):
    """
        Breadth-First Search algorithm used to compute
        the shortest path between entry and exit in the maze.
    """
    def __init__(
        self, materials: dict[str, Union[Tuple, int, str, bool]]
    ) -> None:
        """
            Initialize BFS solver.

            Args:
                materials (dict): Maze configuration and generated map.
        """
        super().__init__(materials)
        self.shortest_path = ""
        self.visited: list[tuple[int, int]] = []

    def get_shortest_path(self, path: List[tuple[int, int]]) -> str:
        """
            Convert a coordinate path into directional notation (N/E/S/W).

            Args:
                path (List[tuple[int, int]]): Ordered list of positions.

            Returns:
                str: String representing movement directions.
        """
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
                    self.shortest_path += "N"
                elif res_x == 1 and res_y == 0:
                    self.shortest_path += "E"
                elif res_x == 0 and res_y == 1:
                    self.shortest_path += "S"
                else:
                    self.shortest_path += "W"
        return self.shortest_path

    def algo_run(self) -> Any:
        """
            Perform Breadth-First Search to find the shortest path.

            Returns:
                list[tuple[int, int]]: Path from entry to exit.
        """
        queue: deque = deque()
        queue.append((self.materials["entry"], [self.materials["entry"]]))
        self.visited.append(self.materials["entry"])
        while len(queue):
            current, path = queue.popleft()
            if current == self.materials["exit"]:
                self.get_shortest_path(path)
                return path
            dirs = self.get_valid_neighboors(current)
            for dir in dirs:
                if dir == "north":
                    new_x = current[0]
                    new_y = current[1] - 1
                elif dir == "east":
                    new_x = current[0] + 1
                    new_y = current[1]
                elif dir == "south":
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
        """
            Retrieve all valid movement directions from a given cell.

            A direction is considered valid if there is no wall blocking it,
            based on the cell's wall encoding index.

            Args:
                position (Tuple): (x, y) coordinates of the current cell.

            Returns:
                List[str]: List of accessible directions
                    (e.g., 'north', 'east', 'south', 'west').
        """
        directions = list(self.materials["directions"])
        x, y = position
        index = self.get_index_of_position(x, y)
        return self.remove_direction_to_wall(directions, index)

    def remove_direction_to_wall(
        self, directions: List[str], index: int
    ) -> List[str]:
        """
            Remove directions blocked by walls from a direction list.

            The wall configuration is encoded as a bitmask where:
                - 1 represents a north wall
                - 2 represents an east wall
                - 4 represents a south wall
                - 8 represents a west wall

            If a bit is set in the index, the corresponding direction
            is removed from the available directions list.

            Args:
                directions (List[str]): List of potential movement directions.
                index (int): Bitmask representing wall configuration.

            Returns:
                List[str]: Filtered list of directions not blocked by walls.
        """
        if index >= 8:
            index -= 8
            directions.remove("west")
        if index >= 4:
            index -= 4
            directions.remove("south")
        if index >= 2:
            index -= 2
            directions.remove("east")
        if index >= 1:
            index -= 1
            directions.remove("north")
        return directions

    def get_index_of_position(self, x: int, y: int) -> int:
        """
            Retrieve the wall encoding index of a cell.

            Args:
                x (int): X-coordinate.
                y (int): Y-coordinate.

            Returns:
                int: Integer wall encoding.
        """
        return super().get_index_of_position(x, y)

    def create_map(self) -> list[list[str]]:
        """
            Create a new maze grid initialized with full walls.

            Returns:
                List[List[str]]: 2D grid filled with 'F'.
        """
        return super().create_map()


class DFSAlgo(Algo):
    """
        Depth-First Search algorithm used to generate a maze.

        This implementation produces a perfect maze unless the
        'perfect' flag is set to False.
    """
    def __init__(self, materials: dict[str, Any]) -> None:
        """
            Initialize DFS generator.

            Args:
                materials (dict): Maze configuration.
        """
        super().__init__(materials)
        self.materials["map"] = self.create_map()
        self.unvisited = self.get_all_cells()
        self.visited: list[tuple[int, int]] = []

    def get_all_cells(self) -> List[Tuple]:
        unvisited = list()
        for y in range(0, self.materials["height"]):
            for x in range(0, self.materials["width"]):
                unvisited.append((x, y))
        return unvisited

    #  DFS is executed to to made  perfect map
    def algo_run(self) -> list[Any]:
        """
            Execute DFS maze generation.

            Returns:
                list[Any]: Empty list (generation modifies map in-place).
        """
        if self.materials["is_42"] is True:
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
        if (
            not self.materials["perfect"]
            and self.materials["height"] > 1
            and self.materials["width"] > 1
        ):
            self.remove_for_imperfect()

        return []

    # for imperfect maze:
    def remove_for_imperfect(self) -> None:
        """
            Randomly remove additional walls to create an imperfect maze.

            This introduces cycles by selectively removing certain
            remaining walls based on predefined wall-encoding indices.
        """
        for y in range(0, self.materials["height"]):
            for x in range(0, self.materials["width"]):
                index: int = self.get_index_of_position(x, y)
                walls: list[Any] = self.get_walls_of_index(index, x, y)
                if index in [14, 13, 11, 7] and len(walls):
                    wall = random.choice(walls)
                    if wall == "north":
                        self.materials["map"][y][x] = self.hexa[index - 1]
                        index_2 = self.get_index_of_position(x, y - 1)
                        self.materials["map"][y - 1][x] = self.hexa[
                            index_2 - 4
                        ]
                    elif wall == "east":
                        self.materials["map"][y][x] = self.hexa[index - 2]
                        index_2 = self.get_index_of_position(x + 1, y)
                        self.materials["map"][y][x + 1] = self.hexa[
                            index_2 - 8
                        ]
                    elif wall == "south":
                        self.materials["map"][y][x] = self.hexa[index - 4]
                        index_2 = self.get_index_of_position(x, y + 1)
                        self.materials["map"][y + 1][x] = self.hexa[
                            index_2 - 1
                        ]
                    else:
                        self.materials["map"][y][x] = self.hexa[index - 8]
                        index_2 = self.get_index_of_position(x - 1, y)
                        self.materials["map"][y][x - 1] = self.hexa[
                            index_2 - 2
                        ]
                    return

    def get_walls_of_index(self, index: int, x: int, y: int) -> list[Any]:
        """
            Retrieve removable walls for a given cell.

            The wall configuration is encoded as a bitmask.
            This method extracts which walls can be removed
            without leaving the grid boundaries.

            Args:
                index (int): Integer wall encoding.
                x (int): X-coordinate.
                y (int): Y-coordinate.

            Returns:
                list[Any]: List of removable wall directions
                    ('north', 'east', 'south', 'west').
        """
        walls: list[Any] = []

        for i in range(4):
            if index >> i & 1:
                if i == 0 and y != 0:
                    walls.append("north")
                elif i == 1 and x != self.materials["width"] - 1:
                    walls.append("east")
                elif i == 2 and y != self.materials["height"] - 1:
                    walls.append("south")
                elif i == 3 and x != 0:
                    walls.append("west")
        return walls

    #  remove walls between two cells (cell, neighbor)
    def remove_walls(
        self, cell: Tuple[int, int], neighboor: Tuple[int, int]
    ) -> None:
        """
            Remove walls between two adjacent cells.

            Args:
                cell (Tuple[int, int]): Current cell.
                neighboor (Tuple[int, int]): Adjacent neighbor cell.
        """
        cell_x, cell_y = cell
        neigh_x, neigh_y = neighboor

        idx_c = self.get_index_of_position(cell_x, cell_y)
        idx_n = self.get_index_of_position(neigh_x, neigh_y)

        if cell_x > neigh_x:
            self.materials["map"][cell_y][cell_x] = self.hexa[idx_c - 8]
            self.materials["map"][neigh_y][neigh_x] = self.hexa[idx_n - 2]
        elif cell_x < neigh_x:
            self.materials["map"][cell_y][cell_x] = self.hexa[idx_c - 2]
            self.materials["map"][neigh_y][neigh_x] = self.hexa[idx_n - 8]
        else:
            if cell_y > neigh_y:
                self.materials["map"][cell_y][cell_x] = self.hexa[idx_c - 1]
                self.materials["map"][neigh_y][neigh_x] = self.hexa[idx_n - 4]
            else:
                self.materials["map"][cell_y][cell_x] = self.hexa[idx_c - 4]
                self.materials["map"][neigh_y][neigh_x] = self.hexa[idx_n - 1]

    #  get neighboors from unvisited only valid
    def get_neighboors_from_unvisited(
        self, position: Tuple
    ) -> Tuple[int, int] | None:
        """
            Select a random unvisited neighbor of a cell.

            Args:
                position (Tuple): Current cell coordinates.

            Returns:
                Tuple[int, int] | None:
                    Random unvisited neighbor if available,
                    otherwise None.
        """
        neighboors = list()
        x, y = position

        if y - 1 >= 0:
            north = (x, y - 1)
            if north not in self.visited:
                neighboors.append(north)
        if y + 1 < self.materials["height"]:
            south = (x, y + 1)
            if south not in self.visited:
                neighboors.append(south)
        if x + 1 < self.materials["width"]:
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
        """
            Mark the predefined "42" logo cells as visited.

            This prevents DFS from generating paths through
            the reserved logo area in the center of the maze.
        """
        for y in range(self.materials["height"]):
            for x in range(self.materials["width"]):
                if self.in_map_quarante_deux(x, y):
                    self.visited.append((x, y))
                    self.unvisited.remove((x, y))

    #  check if this direction go throw the map 42 in middle map
    def in_map_quarante_deux(self, new_x: int, new_y: int) -> bool:
        """
            Check whether a coordinate belongs to the reserved "42" logo area.

            Args:
                new_x (int): X-coordinate.
                new_y (int): Y-coordinate.

            Returns:
                bool: True if inside the logo region.
        """
        return super().in_map_quarante_deux(new_x, new_y)

    #  get index from map
    def get_index_of_position(self, x: int, y: int) -> int:
        """
            Retrieve the wall encoding index of a cell.

            Args:
                x (int): X-coordinate.
                y (int): Y-coordinate.

            Returns:
                int: Integer wall encoding.
        """
        return super().get_index_of_position(x, y)

    #  create new_map with walls
    def create_map(self) -> List[list[str]]:
        """
            Create a new maze grid initialized with full walls.

            Returns:
                List[List[str]]: 2D grid filled with 'F'.
        """
        return super().create_map()


class WilsonAlgo(Algo):
    """
        Wilson's algorithm for generating a uniform spanning tree maze.

        This algorithm produces an unbiased perfect maze using
        loop-erased random walks.
    """
    def __init__(
        self, materials: dict[str, Union[Tuple, int, str, bool]]
    ) -> None:
        """
            Initialize Wilson maze generator.

            Args:
                materials (dict): Maze configuration.
        """
        super().__init__(materials)
        self.materials["map"] = self.create_map()
        self.visited: list[tuple[int, int]] = list()
        self.unvisited = self.get_all_cells()

    def create_map(self) -> List[List[str]]:
        """
            Create a new maze grid initialized with full walls.

            Returns:
                List[List[str]]: 2D maze grid filled with 'F'.
        """
        return super().create_map()

    def remove_map_quarante_deux(self) -> None:
        """
            Remove the predefined "42" logo cells from the unvisited set.

            This ensures that Wilson's random walk does not generate
            paths through the reserved logo area when the feature
            is enabled.
        """
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
        """
            Execute Wilson's maze generation algorithm.

            Process:
                1. Select an initial random cell and mark it visited.
                2. While unvisited cells remain:
                    - Perform a loop-erased random walk from a random
                      unvisited cell until reaching a visited cell.
                    - Carve the path into the maze.
                3. Optionally remove additional walls if the maze
                   is not required to be perfect.

            Returns:
                list[tuple[int, int]] | None:
                    Empty list after successful generation,
                    or empty list if an unexpected condition occurs.
        """
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
                next: tuple[int, int] | None = self.get_rand_valid_neighboors(
                    current
                )
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

        if (
            not self.materials["perfect"]
            and self.materials["height"] > 1
            and self.materials["width"] > 1
        ):
            self.remove_for_imperfect()

        return []

    def remove_for_imperfect(self) -> None:
        """
            Randomly remove additional walls to create an imperfect maze.

            This introduces cycles into the maze by selectively
            removing certain walls based on predefined index values.
        """
        for y in range(0, self.materials["height"]):
            for x in range(0, self.materials["width"]):
                index: int = self.get_index_of_position(x, y)
                walls: list[Any] = self.get_walls_of_index(index, x, y)
                if index in [14, 13, 11, 7] and len(walls):
                    wall = random.choice(walls)
                    if wall == "north":
                        self.materials["map"][y][x] = self.hexa[index - 1]
                        index_2 = self.get_index_of_position(x, y - 1)
                        self.materials["map"][y - 1][x] = self.hexa[
                            index_2 - 4
                        ]
                    elif wall == "east":
                        self.materials["map"][y][x] = self.hexa[index - 2]
                        index_2 = self.get_index_of_position(x + 1, y)
                        self.materials["map"][y][x + 1] = self.hexa[
                            index_2 - 8
                        ]
                    elif wall == "south":
                        self.materials["map"][y][x] = self.hexa[index - 4]
                        index_2 = self.get_index_of_position(x, y + 1)
                        self.materials["map"][y + 1][x] = self.hexa[
                            index_2 - 1
                        ]
                    else:
                        self.materials["map"][y][x] = self.hexa[index - 8]
                        index_2 = self.get_index_of_position(x - 1, y)
                        self.materials["map"][y][x - 1] = self.hexa[
                            index_2 - 2
                        ]
                    return

    def get_walls_of_index(self, index: int, x: int, y: int) -> list[Any]:
        """
            Retrieve removable walls for a given cell.

            Args:
                index (int): Wall encoding index.
                x (int): X-coordinate.
                y (int): Y-coordinate.

            Returns:
                list[Any]: List of removable wall directions.
        """
        walls: list[Any] = []

        for i in range(4):
            if index >> i & 1:
                if i == 0 and y != 0:
                    walls.append("north")
                elif i == 1 and x != self.materials["width"] - 1:
                    walls.append("east")
                elif i == 2 and y != self.materials["height"] - 1:
                    walls.append("south")
                elif i == 3 and x != 0:
                    walls.append("west")
        return walls

    def remove_walls_of_path(self, path: List[tuple]) -> None:
        """
            Remove walls along a generated path.

            Args:
                path (List[tuple]): Ordered list of coordinates
                    representing a valid path.
        """
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
        self, position: Tuple
    ) -> Tuple[int, int] | None:
        """
            Select a random valid neighboring cell.

            The neighbor must:
                - Be inside the grid bounds
                - Not violate the "42" logo constraint (if enabled)

            Args:
                position (Tuple): Current cell position.

            Returns:
                Tuple[int, int] | None:
                    Random valid neighbor or None if none exist.
        """
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
        """
        Check whether a coordinate belongs to the reserved "42" logo area.

        Args:
            new_x (int): X-coordinate.
            new_y (int): Y-coordinate.

        Returns:
            bool: True if inside the logo region.
        """
        return super().in_map_quarante_deux(new_x, new_y)

    def get_all_cells(self) -> List[Tuple]:
        """
            Generate a list of all grid coordinates.

            Returns:
                List[Tuple]: List of all (x, y) positions.
        """
        not_visited = list()
        for y in range(0, self.materials["height"]):
            for x in range(0, self.materials["width"]):
                not_visited.append((x, y))
        return not_visited

    def get_index_of_position(self, x: int, y: int) -> int:
        """
            Retrieve the wall encoding index of a cell.

            Args:
                x (int): X-coordinate.
                y (int): Y-coordinate.

            Returns:
                int: Integer wall encoding.
        """
        return super().get_index_of_position(x, y)


class MazeGenerator:
    """
        Main interface class for generating mazes.

        Supports:
            - DFS maze generation
            - Wilson's algorithm maze generation
            - BFS shortest path solving

        After generation, the maze and its solution can be exported
        to a file.
    """
    def __init__(
        self,
        width: int,
        height: int,
        entry: Tuple[int, int],
        exit: Tuple[int, int],
        seed: int,
        filename: str,
        perfect: bool,
    ) -> None:
        """
            Initialize maze generator configuration.

            Args:
                width (int): Maze width.
                height (int): Maze height.
                entry (Tuple[int, int]): Entry coordinate.
                exit (Tuple[int, int]): Exit coordinate.
                seed (int): Random seed.
                filename (str): Output file name.
            perfect (bool): Whether the maze is perfect.
        """

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

    def logo_in_map(self) -> bool:
        """
            Determine whether the maze is large enough to embed
            the predefined "42" logo shape in its center.

            Returns:
                bool: True if the maze dimensions allow embedding
                the logo, otherwise False.
        """
        if self.height > 6 and self.width > 8:
            return True
        return False

    def create_map(self) -> List[str]:
        """
            Create a new maze grid initialized with full walls ('F').

            Returns:
                List[List[str]]: A 2D list representing the maze grid.
        """
        my_map: List[Any] = []
        for i in range(self.height):
            cols = []
            for j in range(self.width):
                cols.append("F")
            my_map.append(cols)
        return my_map

    def generate(self, name_algo: str) -> None:
        """
            Generate the maze using the selected algorithm.

            Supported algorithms:
                - "dfs": Depth-First Search maze generation
                - "wilson": Wilson's algorithm maze generation

            After generation:
                - The maze grid is stored in self.map
                - The shortest path is computed using BFS
                - The result is written to the output file

            Args:
                name_algo (str): Algorithm identifier ("dfs" or "wilson").
        """
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
        """
            Write the generated maze and its solution to the output file.

            The file contains:
                - The maze grid (one row per line)
                - Entry coordinates
                - Exit coordinates
                - Shortest path as a direction string (N/E/S/W)
        """
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
        """
            Retrieve the generated maze grid.

            Returns:
                List[List[str]]: The maze representation.
        """
        return self.map

    def get_solution(self) -> str:
        """
            Retrieve the computed shortest path.

            Returns:
                str: Direction string representing the solution path.
        """
        return self.shortest_path
