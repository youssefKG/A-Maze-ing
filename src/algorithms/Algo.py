from abc import ABC, abstractmethod
from typing import Any, List, Dict


class Algo(ABC):
    def __init__(self, materials: Dict[str, Any]) -> None:
        self.materials = materials
        self.hexa = "0123456789ABCDEF"

    @abstractmethod
    def algo_run(self) -> None:
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
    def create_map(self) -> List[str]:
        my_map: List[Any] = []
        for i in range(self.materials['height']):
            cols = []
            for j in range(self.materials['width']):
                cols.append('F')
            my_map.append(cols)
        return my_map
