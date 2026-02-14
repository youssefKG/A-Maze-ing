"""Breadth-first search maze solver with animation support."""

from typing import Any
from maze.cell import Cell
from solver.solver import Solver
from renderer.themes import Theme
from collections import deque
from my_mlx.my_mlx import MyMlx


class BfsSolver(Solver):
    """Solve the maze using BFS and animate the search and path."""

    def __init__(self) -> None:
        """Initialize BFS data structures and derive entry/exit cells."""
        super().__init__()
        self.visited: list[Cell] = []
        self.bfs_queue: deque[Cell] = deque()
        self.path: dict[Cell, Cell] = {}
        self.is_solution_found = False
        self.is_running = False
        self.set_entry_cell()
        self.set_exit_cell()
        self.meeting_points: list[tuple[Cell, Cell]] = []

    def get_neighboors(self) -> list[Cell]:
        """Return all reachable neighboring cells of the current cell.

        While doing so, this method also highlights neighbor walls and
        records any meeting points with already-visited cells.
        """
        neighboors = []
        x = self.current_cell.x
        y = self.current_cell.y
        # west
        if x - 1 >= 0:
            neighboor = self.maze_state.cells_grid[y][x - 1]
            if not self.current_cell.west:
                if neighboor in self.visited:
                    self.meeting_points.append((self.current_cell, neighboor))
                neighboors.append(neighboor)
                self.cells_img.draw_wall_between_two_cell(
                    self.current_cell, neighboor, Theme.neighboor
                )
        # east
        if x + 1 < self.maze_state.horizontal_cells:
            neighboor = self.maze_state.cells_grid[y][x + 1]
            if not self.current_cell.east:
                neighboors.append(neighboor)
                if neighboor in self.visited:
                    self.meeting_points.append((self.current_cell, neighboor))
                self.cells_img.draw_wall_between_two_cell(
                    self.current_cell, neighboor, Theme.neighboor
                )
        # north
        if y - 1 >= 0:
            neighboor = self.maze_state.cells_grid[y - 1][x]
            if not self.current_cell.north:
                if neighboor in self.visited:
                    self.meeting_points.append((self.current_cell, neighboor))
                neighboors.append(neighboor)
                self.cells_img.draw_wall_between_two_cell(
                    self.current_cell, neighboor, Theme.neighboor
                )
            # south
        if y + 1 < self.maze_state.vertical_cells:
            neighboor = self.maze_state.cells_grid[y + 1][x]
            if not self.current_cell.south:
                if neighboor in self.visited:
                    self.meeting_points.append((self.current_cell, neighboor))
                neighboors.append(neighboor)
                self.cells_img.draw_wall_between_two_cell(
                    self.current_cell, neighboor, Theme.neighboor
                )
        return neighboors

    def generate(self) -> None:
        """Kick off the BFS process and register the animation hook."""
        if not self.is_running:

            self.current_cell = self.entry_cell
            self.bfs_queue.appendleft(self.entry_cell)
            self.next_cell = self.exit_cell
            self.is_running = True
            MyMlx.loop_hook(self.generate_solution_path_with_animation, None)

    def generate_solution_path_with_animation(self, _: Any) -> None:
        """Advance the BFS search or draw the final path one step."""
        self.frames += 1

        if self.frames % 1 != 0:
            return

        if self.is_finished:
            return

        if not self.is_running:
            return

        if len(self.bfs_queue) and not self.is_solution_found:
            self.current_cell = self.bfs_queue.popleft()
            if self.current_cell is self.exit_cell:
                self.is_solution_found = True
                self.redraw_maze()
            else:
                neighboors = self.get_neighboors()
                self.draw_neighboors(neighboors)

        elif self.is_solution_found and self.next_cell is not self.entry_cell:
            self.cells_img.draw_cell(self.next_cell, Theme.path)
            self.cells_img.draw_wall_between_two_cell(
                self.next_cell, self.path[self.next_cell], Theme.path
            )
            self.next_cell = self.path[self.next_cell]
            self.put_cells_img_to_window()
        elif self.is_solution_found and self.next_cell is self.entry_cell:
            self.cells_img.draw_cell(self.entry_cell, Theme.entry_cell)
            self.cells_img.draw_cell(self.exit_cell, Theme.exit_cell)
            self.is_finished = True
            self.is_running = False
            self.is_path_shown = True
            self.put_cells_img_to_window()

    # draw neightboors
    def draw_neighboors(self, neighboors: list[Cell]) -> None:
        """Enqueue neighbors, record parents, and color them on screen."""
        # get neighboors
        for neighboor in neighboors:
            if (
                neighboor not in self.visited
                and neighboor not in self.bfs_queue
            ):
                self.bfs_queue.append(neighboor)
                self.visited.append(neighboor)
                self.path[neighboor] = self.current_cell
                self.cells_img.draw_cell(neighboor, Theme.neighboor)
            self.put_cells_img_to_window()

    def redraw_maze(self) -> None:
        """Redraw the maze and remove any temporary BFS highlights."""
        for row_cells in self.maze_state.cells_grid:
            for cell in row_cells:
                if not cell.is_42_cell:
                    self.cells_img.draw_cell(cell, Theme.background)
                else:
                    self.cells_img.draw_cell(cell, Theme.cell_42)

        for cell in self.visited:
            if cell in self.path:
                self.cells_img.draw_wall_between_two_cell(
                    cell, self.path[cell], Theme.background
                )
        for points in self.meeting_points:
            cell, next_cell = points
            self.cells_img.draw_wall_between_two_cell(
                cell, next_cell, Theme.background
            )

        self.put_cells_img_to_window()

    def toggle_path(self) -> None:
        """Toggle visibility of the already-computed BFS solution path."""
        # if the path is found and the algo is finished
        if not self.is_path_shown and self.is_finished:
            self.draw_path()
            self.is_path_shown = True
        elif self.is_finished:
            self.hide_path()
            self.is_path_shown = False

    def hide_path(self) -> None:
        """Erase the drawn solution path while keeping the maze structure."""
        cell = self.exit_cell
        if self.is_solution_found and self.is_finished:
            while cell is not self.entry_cell:
                self.cells_img.draw_cell(cell, Theme.background)
                self.cells_img.draw_wall_between_two_cell(
                    cell, self.path[cell], Theme.background
                )
                cell = self.path[cell]
            self.put_cells_img_to_window()
            self.is_path_shown = False

    def draw_path(self) -> None:
        """Draw the full BFS solution path from exit back to entry."""
        cell = self.exit_cell
        if self.is_solution_found and self.is_finished:
            while cell is not self.entry_cell:
                self.cells_img.draw_cell(cell, Theme.path)
                self.cells_img.draw_wall_between_two_cell(
                    cell, self.path[cell], Theme.path
                )
                cell = self.path[cell]
            self.is_path_shown = True
            self.put_cells_img_to_window()

    def set_entry_cell(self) -> None:
        """Cache the maze's entry cell from shared maze state."""
        self.entry_cell = self.maze_state.get_entry_cell()

    def set_exit_cell(self) -> None:
        """Cache the maze's exit cell from shared maze state."""
        self.exit_cell = self.maze_state.get_exit_cell()
