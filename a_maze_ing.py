from renderer.renderer import Renderer
from mazegen.MazeGenerator import MazeGenerator
from sys import argv
from parser.Parser import Parser
from typing import Any


class Amazeing:
    def __init__(self) -> None:
        args: Any = argv
        parser = Parser(args)
        parser.parse()
        self.maze_gen: MazeGenerator = MazeGenerator(
            parser.height,
            parser.width,
            parser.entry,
            parser.exit,
            parser.seed,
            parser.output_file,
            parser.perfect,
        )
        self.renderer = Renderer(self.maze_gen, parser)


def main() -> None:
    amazeing = Amazeing()
    amazeing.renderer.render()


if __name__ == "__main__":
    main()
