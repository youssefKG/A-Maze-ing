"""Application entry point for the A-Maze-Ing maze visualizer.

This module wires together argument parsing, maze generation, and
rendering, then starts the main event loop.
"""

from renderer.renderer import Renderer
from mazegen.MazeGenerator import MazeGenerator
from sys import argv
from parser.Parser import Parser
from typing import Any


class Amazeing:
    """High-level application object responsible for setup and wiring."""

    def __init__(self) -> None:
        """Parse CLI arguments, build the maze generator, and renderer."""
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
    """Create the application object and start rendering the maze."""
    amazeing = Amazeing()
    amazeing.renderer.render()


if __name__ == "__main__":
    main()
