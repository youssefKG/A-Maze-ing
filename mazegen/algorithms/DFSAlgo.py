import random
from typing import Any, Dict, List, Tuple
from mazegen.algorithms.Algo import Algo


class DFSAlgo(Algo):
    #  the constructor of class
    def __init__(self, materials: Dict[str, Any]) -> None:
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
        if not self.materials['perfect']:
            self.remove_for_imperfect()
        for row in self.materials['map']:
            print(row)
        return []

    # for imperfect maze:
    def remove_for_imperfect(self) -> None:
        for y in range(1, self.materials['height']):
            for x in range(1, self.materials['width']):
                walls: list[bool, bool, bool, bool] = self.get_walls_of_cell(x, y)
                number_of_walls = len([wall for wall in walls if wall == True])
                if number_of_walls == 3:
                    self.remove_between_them(walls, x, y)
                    return

    def remove_between_them(self, walls: list[bool, bool, bool, bool], x: int, y: int) -> None:
        i = 0
        while i < 4:
            if self.im_between_them(walls, i, x, y):
                index = self.get_index_of_position(x, y)
                if i == 0:
                    index -= 1
                elif i == 1:
                    index -= 2
                elif i == 2:
                    index -= 4
                else:
                    index -= 8
                print(self.hexa[index], "hexa[index]")
                print(f"{self.materials['map'][y][x]}, {index}")
                self.materials['map'][y][x] = self.hexa[index]
                for row in self.materials['map']:
                    print(row)

                print("---------------------")
                return
            i += 1
        
    def im_between_them(self, walls: list[bool, bool, bool, bool], index: int, x: int, y: int) -> None:
        if index < 3:
            if walls[index - 1] and walls[index + 1]:
                return True
        else:
            if walls[index - 1] and walls[0]:
                return True
        return False

    def get_walls_of_cell(self, x: int, y: int) -> list[bool, bool, bool, bool]:
        walls: list[bool, bool, bool, bool] = [False, False, False, False] 
        index = self.get_index_of_position(x, y)
        for i in range(4):
            if index >> i & 1:
                walls[i] = True
            i += 1
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
