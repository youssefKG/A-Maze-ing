"""Factory helpers for creating maze generators and solvers.

This module centralizes construction of algorithm implementations and
their corresponding solver objects so the rest of the codebase can work
with a simple, high-level API.
"""

from typing import Any
from generators.dfs_maze_generator import DfsMazeGenerator
from generators.maze_generator_algo import MazeGeneratorAlgo
from generators.wilson_maze_generator import WilsonMazeGenerator
from renderer.images.cellImg import CellsImage
from solver.bfs_solver import BfsSolver
from solver.solver import Solver


class AlgoFactory:
    """Factory for maze generation algorithms and solver instances."""

    generator_name = "default"

    @classmethod
    def create(cls, name: str | None = None) -> Any:
        """Create a maze generator algorithm instance.

        Parameters
        ----------
        name:
            Optional name of the generator algorithm (for example,
            ``"wilson"`` or ``"dfs"``). When omitted, the default
            generator is used.

        Returns
        -------
        Any
            A configured maze generator with its cell image attached.
        """
        if name:
            cls.generator_name = name
        algo_generator = MazeGeneratorAlgo()
        if name == "wilson":
            algo_generator = WilsonMazeGenerator()
        elif name == "dfs":
            algo_generator = DfsMazeGenerator()
        return algo_generator.set_cells_img(CellsImage())

    @classmethod
    def create_solver(cls, name: str) -> Solver:
        """Create a solver instance for the given algorithm name.

        Parameters
        ----------
        name:
            Name of the solver algorithm to use (currently ``"bfs"``
            is supported).

        Returns
        -------
        Solver
            A solver implementation compatible with the maze
            generators.
        """
        solver = Solver()
        if name == "bfs":
            solver = BfsSolver()
        return solver
