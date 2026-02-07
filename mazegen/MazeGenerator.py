import random
from typing import Any, List, Tuple
from .algorithms.DFSAlgo import DFSAlgo
from .algorithms.WilsonAlgo import WilsonAlgo
from .algorithms.BFSAlgo import BFSAlgo


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
                    "hexa": "0123456789ABCEDF",
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
                    "hexa": "0123456789ABCEDF",
                    "directions": ("north", "east", "south", "west"),
                }
            )
            bfs.algo_run()
            self.shortest_path = bfs.shortest_path
            self.create_output_file()

    def create_output_file(self) -> None:
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

    def get_map(self) -> List[Any]:
        return self.map

    def get_solution(self) -> str:
        return self.shortest_path
