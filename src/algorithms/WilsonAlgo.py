import random
from typing import Dict, List, Union, Tuple
from src.algorithms.Algo import Algo


class WilsonAlgo(Algo):
    def __init__(self, materials: Dict[str, Union[Tuple, int, str, bool]]) -> None:
        super().__init__(materials)
        self.materials["map"] = self.create_map()
        self.visited = list()
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

    def algo_run(self) -> None:
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
                next_cell = self.get_random_valid_neighboors(current)
                try:
                    loop_index = path.index(next_cell)
                    path = path[: loop_index + 1]
                except Exception:
                    path.append(next_cell)
                current = next_cell
            self.remove_walls_of_path(path)
            for cell in path:
                self.visited.append(cell)
                if cell in self.unvisited:
                    self.unvisited.remove(cell)

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

    def get_random_valid_neighboors(self, position: Tuple) -> Tuple:
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
