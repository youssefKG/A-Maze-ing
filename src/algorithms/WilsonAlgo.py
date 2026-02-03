import random
from typing import Dict, List, Union, Tuple
from src.algorithms.Algo import Algo


class WilsonAlgo(Algo):
    def __init__(
        self,
        materials: Dict[str, Union[Tuple, int, str, bool]]
    ) -> None:
        super().__init__(materials)
        self.materials['map'] = self.create_map()
        self.visited = list()
        self.unvisited = self.get_all_cells()
        random.seed(self.materials['seed'])

    def create_map(self) -> List[List[str]]:
        return super().create_map()

    def remove_map_quarante_deux(self) -> None:
        if self.materials['height'] < 6 or self.materials['width'] < 8:
            return
        i = 0
        while i < self.materials['height']:
            j = 0
            while j < self.materials['width']:
                if self.in_map_quarante_deux(j, i):
                    self.unvisited.remove((j, i))
                j += 1
            i += 1

    def algo_run(self) -> None:
        if self.materials['is_42']:
            self.remove_map_quarante_deux()
        # take a target cell for search about cell
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
        if not self.materials['perfect']:
            y = 0
            for row in self.materials['map']:
                x = 0
                while x < len(row):
                    index = self.get_index_of_position(x, y)
                    if index >> 2 & 1:
                        cell = (x, y)
                        neighboor = (x, y + 1)
                        self.non_perfect_maze(cell, neighboor)
                        return
                    x += 1
                y += 1

    def non_perfect_maze(self, cell, neighbor):
        curr_x, curr_y = cell
        next_x, next_y = neighbor
        index_curr = self.get_index_of_position(curr_x, curr_y)
        index_next = self.get_index_of_position(next_x, next_y)
        self.materials['map'][curr_y][curr_x] = self.hexa[index_curr - 4]
        self.materials['map'][next_y][next_x] = self.hexa[index_next - 1]

    def remove_walls_of_path(self, path: List[tuple]) -> None:
        i = 0
        for i in range(0, len(path) - 1):
            c_x, c_y = path[i]
            n_x, n_y = path[i + 1]
            index_curr = self.get_index_of_position(c_x, c_y)
            index_next = self.get_index_of_position(n_x, n_y)
            if c_x > n_x:
                self.materials['map'][c_y][c_x] = self.hexa[index_curr - 8]
                self.materials['map'][n_y][n_x] = self.hexa[index_next - 2]
            elif c_x < n_x:
                self.materials['map'][c_y][c_x] = self.hexa[index_curr - 2]
                self.materials['map'][n_y][n_x] = self.hexa[index_next - 8]
            else:
                if c_y > n_y:
                    self.materials['map'][c_y][c_x] = self.hexa[index_curr - 1]
                    self.materials['map'][n_y][n_x] = self.hexa[index_next - 4]
                else:
                    self.materials['map'][c_y][c_x] = self.hexa[index_curr - 4]
                    self.materials['map'][n_y][n_x] = self.hexa[index_next - 1]

    def get_random_valid_neighboors(self, position: Tuple) -> Tuple:
        x, y = position
        directions = list()

        if y - 1 >= 0:
            if not self.materials['is_42']:
                north = (x, y - 1)
                directions.append(north)
            else:
                if not self.in_map_quarante_deux(x, y - 1):
                    north = (x, y - 1)
                    directions.append(north)
        if y + 1 < self.materials['height']:
            if not self.materials['is_42']:
                south = (x, y + 1)
                directions.append(south)
            else:
                if not self.in_map_quarante_deux(x, y + 1):
                    south = (x, y + 1)
                    directions.append(south)
        if x + 1 < self.materials['width']:
            if not self.materials['is_42']:
                east = (x + 1, y)
                directions.append(east)
            else:
                if not self.in_map_quarante_deux(x + 1, y):
                    east = (x + 1, y)
                    directions.append(east)
        if x - 1 >= 0:
            if not self.materials['is_42']:
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
        for y in range(0, self.materials['height']):
            for x in range(0, self.materials['width']):
                not_visited.append((x, y))
        return not_visited

    def get_index_of_position(self, x: int, y: int) -> int:
        return super().get_index_of_position(x, y)


################################################
if __name__ == '__main__':

    materials = {
        'width': 9,
        'height': 7,
        'entry': (0, 0),
        'exit': (3, 1),
        'directions': ['north', 'east', 'south', 'west']
    }

    random.seed(7)
    wilson = WilsonAlgo("Wilson", materials)
    wilson.algo_run()
    for row in wilson.materials['map']:
        print(row)
