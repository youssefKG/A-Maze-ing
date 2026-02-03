import random
from typing import Any, Dict, List, Tuple
from src.algorithms.Algo import Algo


class DFSAlgo(Algo):
    # the constructor of class
    def __init__(self, materials: Dict[str, Any]) -> None:
        super().__init__(materials)
        self.materials['map'] = self.create_map()
        self.unvisited = self.get_all_cells()
        random.seed(self.materials['seed'])

    def get_all_cells(self) -> List[Tuple]:
        unvisited = list()
        for y in range(0, self.materials['height']):
            for x in range(0, self.materials['width']):
                unvisited.append((x, y))
        return unvisited

    # DFS is executed to to made  perfect map
    def algo_run(self) -> None:

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
            y = 0
            for row in self.materials['map']:
                x = 0
                while x < len(row):
                    index = self.get_index_of_position(x, 0)
                    if index >> 2 & 1:
                        cell = (x, y)
                        neighboor = (x, y + 1)
                        self.remove_walls(cell, neighboor)
                        return
                    x += 1
                y += 1

    # remove walls between two cells (cell, neighbor)
    def remove_walls(self, cell, neighboor):
        cell_x, cell_y = cell
        neighboor_x, neighboor_y = neighboor

        index_cell = self.get_index_of_position(cell_x, cell_y)
        index_neighboor = self.get_index_of_position(neighboor_x, neighboor_y)

        if cell_x > neighboor_x:
            self.materials['map'][cell_y][cell_x] = self.hexa[index_cell - 8]
            self.materials['map'][neighboor_y][neighboor_x] = self.hexa[index_neighboor - 2]
        elif cell_x < neighboor_x:
            self.materials['map'][cell_y][cell_x] = self.hexa[index_cell - 2]
            self.materials['map'][neighboor_y][neighboor_x] = self.hexa[index_neighboor - 8]            
        else:
            if cell_y > neighboor_y:
                self.materials['map'][cell_y][cell_x] = self.hexa[index_cell - 1]
                self.materials['map'][neighboor_y][neighboor_x] = self.hexa[index_neighboor - 4]
            else:
                self.materials['map'][cell_y][cell_x] = self.hexa[index_cell - 4]
                self.materials['map'][neighboor_y][neighboor_x] = self.hexa[index_neighboor - 1]

    # get neighboors from unvisited only valid 
    def get_neighboors_from_unvisited(self, position: Tuple) -> Tuple[int, int]:
        # dirs = {(0, -1), (0, 1), (1, 0), (-1, 0)}
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

    # if map has 42 set cells as visited and rmeove it from unvisited
    def put_cells_42_as_visited(self) -> None:
        for y in range(self.materials['height']):
            for x in range(self.materials['width']):
                if self.in_map_quarante_deux(x, y):
                    self.visited.append((x, y))
                    self.unvisited.remove((x, y))

    # check if this direction go throw the map 42 in middle map
    def in_map_quarante_deux(self, new_x: int, new_y: int) -> bool:
        return super().in_map_quarante_deux(new_x, new_y)

    # get index from map
    def get_index_of_position(self, x: int, y: int) -> int:
        return super().get_index_of_position(x, y)

    # create new_map with walls
    def create_map(self) -> List[str]:
        return super().create_map()


if __name__ == '__main__':
    dfs = DFSAlgo("DFS", {
        'width': 10,
        'height': 10,
        'entry': (1, 1),
        'exit': (-1, 0),
        'directions': ['north', 'east', 'south', 'west']})
    # grid = dfs.create_map()
    random.seed(11)
    dfs.algo_run(dfs.materials['entry'][0], dfs.materials['entry'][1])
    for row in dfs.materials['map']:
        print(row)



    # map = [[9,1,]]
    # materials = {'width': 4, 'height': 3, 'entry': (0, 0), 'exit': (1, 2), 'directions': ['north', 'east', 'south', 'west'], 'map': map}
    # bfs = BFSAlgo("BFS", materials)
