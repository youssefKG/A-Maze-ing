"""Control panel for handling user input and maze actions.

This module wires keyboard events to maze generation, solving, and
rendering actions. It does not contain the actual algorithms; instead it
coordinates between the generator, solver, renderer, and global state
objects.
"""

from generators.algo_factory import AlgoFactory
from mazegen.MazeGenerator import MazeGenerator
from random import seed
from my_mlx.my_mlx import MyMlx
from renderer.themes import Theme
from solver.solver import Solver
from renderer.images.background.background_img import BackgroundImg
from maze.maze_state import MazeState


class ControllPannel:
    """High-level controller that reacts to keyboard input.

    An instance of this class registers a key hook and then delegates
    actions such as maze generation, solving, and color/theme changes
    to other components in the application.
    """

    def __init__(self, maze_gen: MazeGenerator) -> None:
        """Initialize the control panel and register key handlers.

        Parameters
        ----------
        maze_gen:
            The maze generator backend used to build maze layouts.
        """
        self.algo = AlgoFactory.create()
        self.is_started = False
        self.solver = Solver()
        start_image = BackgroundImg("karim.png", "png")
        start_image.put_image_to_window()
        MyMlx.key_hook(self.on_press, None)
        self.maze_state = MazeState()
        self.maze_gen = maze_gen

    def draw(self) -> None:
        """Redraw the control panel.

        Currently this is a placeholder; drawing is handled elsewhere
        in the rendering layer.
        """
        pass

    def on_press(self, keynum: int, _: object) -> None:
        """Handle a key press event.

        Parameters
        ----------
        keynum:
            Numeric key code from the underlying windowing system.
        _:
            Unused event payload passed by the key hook.
        """

        self.start_maze(keynum)
        if self.is_started:
            self.run_dfs(keynum)
            self.run_wilson(keynum)
            self.run_bfs(keynum)
            self.toggle_path(keynum)
            self.change_color(keynum)
        if keynum == 65307:  # esc key
            MyMlx.loop_exit()

    def run_bfs(self, keynum: int) -> None:
        """Trigger BFS solving when the appropriate key is pressed.

        Starts a breadth-first search solver if the generation
        algorithm has finished and the user presses the BFS key.
        """
        if keynum == 115:
            if self.algo.is_finished:
                self.solver.redraw_maze()
                self.solver = AlgoFactory.create_solver("bfs")
                self.solver.hide_path()
                self.solver.generate()

    def run_wilson(self, keynum: int) -> None:
        """Regenerate the maze using Wilson's algorithm on key press."""
        if keynum == 98:  # B key
            self.solver.hide_path()
            seed(self.maze_state.seed)
            self.maze_gen.generate("wilson")
            self.maze_state.set_cells_grid()
            self.algo = AlgoFactory.create("wilson")
            seed(self.maze_state.seed)
            self.algo.generate()

    def run_dfs(self, keynum: int) -> None:
        """Regenerate the maze using a DFS-based algorithm on key press."""
        if keynum == 113:  # q key
            self.solver.hide_path()
            seed(self.maze_state.seed)
            self.maze_gen.generate("dfs")
            self.maze_state.set_cells_grid()
            self.algo = AlgoFactory.create("dfs")
            seed(self.maze_state.seed)
            self.algo.generate()

    def start_maze(self, keynum: int) -> None:
        """Start the initial maze animation when Enter is pressed."""
        if keynum == 65293:  # enter key
            if not self.is_started:
                self.is_started = True
                Theme.background_img.put_image_to_window()
                self.algo.generate()

    def toggle_path(self, keynum: int) -> None:
        """Toggle display of the solver path when the toggle key is pressed."""
        if keynum == 104:  # toogle path on press H
            if (
                self.algo.is_finished
                and self.solver.is_finished
                and not self.algo.is_running
            ):
                self.algo.redraw_maze()
                self.solver.toggle_path()
                self.algo.draw_entry_exit_cells()

    def change_color(self, keynum: int) -> None:
        """Change the maze color theme when the color key is pressed."""
        if keynum == 99:  # C key
            if not self.solver.is_running:
                if (
                    self.algo.is_running
                    and AlgoFactory.generator_name == "wilson"
                ):
                    return
                Theme.change()
                Theme.background_img.put_image_to_window()
                self.algo.redraw_maze()
                if self.solver.is_path_shown:
                    self.solver.draw_path()
                self.algo.draw_entry_exit_cells()
