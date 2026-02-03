from src.algorithms.Algo import Algo
from typing import Dict, Tuple, Union, List
from collections import deque


class BFSAlgo(Algo):
    def __init__(self, algo_name: str, materials: Dict[str, Union[Tuple, int, str, bool]]) -> None:
        super().__init__(algo_name, materials)
        self.shortest_path = ''

    def get_shortest_path(self, path: List[Tuple]) -> None:
        x = -1
        y = -1
        for t in path:
            current_x, current_y = t
            if x < 0 or y < 0:
                x, y = current_x, current_y
            else:
                res_x, res_y = current_x - x, current_y - y
                x, y = current_x, current_y
                if res_x == 0 and res_y == -1: # north
                    self.shortest_path += 'N'
                elif res_x == 1 and res_y == 0: # east
                    self.shortest_path += 'E'
                elif res_x == 0 and res_y == 1: # south
                    self.shortest_path += 'S'
                else:                           # west
                    self.shortest_path += 'W'
        print(self.shortest_path)

    def algo_run(self) -> None:
        queue = deque()
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

    def get_valid_neighboors(self, position: Tuple) -> List[str]:
        directions = list(self.materials['directions'])
        x, y = position
        index = self.get_index_of_position(x, y)
        return self.remove_direction_to_wall(directions, index)

    def create_map(self) -> List[List[str]]:
        pass

    def remove_direction_to_wall(self, directions: List[str], index: int) -> List[str]:
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

    def get_index_of_position(self, x: int, y: int):
        return super().get_index_of_position(x, y)
