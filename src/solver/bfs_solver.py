from maze import maze_state
from maze.cell import Cell
from collections import deque
from solver.solver import Solver
from renderer.colors import Colors
from renderer.themes import Theme
from collections import deque
from my_mlx.my_mlx import MyMlx

"""
procedure BFS_Algorithm(graph, initial_vertex):
create a queue called frontier
create a list called visited_vertex
add the initial vertex in the frontier
while True:
    if frontier is empty then
    print("No Solution Found")
    break

    selected_node = remove the first node of the frontier
    add the selected_node to the visited_vertex list

    // Check if the selected_node is the solution
    if selected_node is the solution then
    print(selected_node)
    break

    // Extend the node
    new_nodes = extend the selected_node
    // Add the extended nodes in the frontier
    for all nodes from new_nodes do
    if node not in visited_vertex and node not in frontier then
    add node at the end of the queue
"""


class BfsSolver(Solver):
    def __init__(self):
        super().__init__()
        self.visited = []
        self.bfs_queue = deque()
        self.path = {}
        self.is_solution_found = False
        self.is_running = False

    def get_neighboors(self) -> list[Cell]:
        neighboors = []
        x = self.current_cell.x
        y = self.current_cell.y
        # west
        if x > 0:
            neighboor = self.maze_state.cells_grid[y][x - 1]
            if not self.current_cell.west:
                neighboors.append(neighboor)
                self.cells_img.draw_wall_between_two_cell(
                        self.current_cell,
                        neighboor,
                        Theme.neighboor
                        )
        # east
        if x + 1 < self.maze_state.horizontal_cells:
            neighboor = self.maze_state.cells_grid[y][x + 1]
            if not self.current_cell.east:
                neighboors.append(neighboor)
                self.cells_img.draw_wall_between_two_cell(
                        self.current_cell,
                        neighboor,
                        Theme.neighboor
                        )
        # north
        if y > 0:
            neighboor = self.maze_state.cells_grid[y - 1][x]
            if not self.current_cell.north:
                neighboors.append(neighboor)
                self.cells_img.draw_wall_between_two_cell(
                        self.current_cell,
                        neighboor,
                        Theme.neighboor
                        )
        # south
        if y + 1 < self.maze_state.vertical_cells:
            neighboor = self.maze_state.cells_grid[y + 1][x]
            if not self.current_cell.south:
                neighboors.append(neighboor)
                self.cells_img.draw_wall_between_two_cell(
                        self.current_cell,
                        neighboor,
                        Theme.neighboor
                        )
        return neighboors

    def generate(self):
        self.current_cell = self.maze_state.entry_cell
        self.bfs_queue.appendleft(self.maze_state.entry_cell)
        self.next_cell = self.maze_state.exit_cell
        self.is_running = True
        MyMlx.loop_hook(self.generate_solution_path_with_animation, None)

    def generate_solution_path_with_animation(self, _):
        self.frames += 1

        if self.frames % 1 != 0:
            return

        if self.is_finished:
            return

        if not self.is_running:
            return 

        if len(self.bfs_queue) and not self.is_solution_found:
            self.current_cell = self.bfs_queue.popleft()
            if self.current_cell is self.maze_state.exit_cell:
                self.is_solution_found = True
                self.redraw_maze()
            else:
                neighboors = self.get_neighboors()
                self.draw_neighboors(neighboors)

        elif self.is_solution_found and self.next_cell is not self.maze_state.entry_cell:
            self.cells_img.draw_cell(self.next_cell, Theme.path)
            self.cells_img.draw_wall_between_two_cell(
                    self.next_cell,
                    self.path[self.next_cell],
                    Theme.path
                    )
            self.next_cell = self.path[self.next_cell]
            self.put_cells_img_to_window()

        elif self.is_solution_found and self.next_cell is self.maze_state.entry_cell:
            self.cells_img.draw_cell(self.maze_state.entry_cell, Theme.entry_cell)
            self.cells_img.draw_cell(self.maze_state.exit_cell, Theme.exit_cell)
            self.is_finished = True
            self.is_running = False
            self.is_path_shown = True
            self.put_cells_img_to_window()

    def draw_neighboors(self, neighboors: list[Cell]):
        for neighboor in neighboors:
            if neighboor not in self.visited and neighboor not in self.bfs_queue:
                self.bfs_queue.append(neighboor)
                self.visited.append(neighboor)
                self.path[neighboor] = self.current_cell
                self.cells_img.draw_cell(neighboor, Theme.neighboor)
                self.put_cells_img_to_window()

    def redraw_maze(self) -> None:
        for row_cells in self.maze_state.cells_grid:
            for cell in row_cells:
                if not cell.is_42_cell:
                    self.cells_img.draw_cell(cell, Theme.background)
                else:
                    self.cells_img.draw_cell(cell, Theme.cell_42)

        for cell in self.visited:
            self.cells_img.draw_wall_between_two_cell(
                    cell,
                    self.path[cell],
                    Theme.background
                    )   
        self.put_cells_img_to_window()
    

    def toggle_path(self) -> None:
        if not self.is_path_shown:
            if not self.is_finished:
                return 
            self.draw_path()
            self.is_path_shown = True
        else:
            if not self.is_finished:
                return 
            self.hide_path()
            self.is_path_shown = False

    def hide_path(self) -> None:
        cell = self.maze_state.exit_cell
        while cell is not self.maze_state.entry_cell:
            self.cells_img.draw_cell(cell, Theme.background)
            self.cells_img.draw_wall_between_two_cell(cell, self.path[cell], Theme.background)
            cell = self.path[cell]
        self.cells_img.draw_cell(self.maze_state.entry_cell, Theme.background)
        self.cells_img.draw_cell(self.maze_state.exit_cell, Theme.background)
        self.is_path_shown = True
        self.put_cells_img_to_window()
            

    def draw_path(self) -> None:
        cell = self.maze_state.exit_cell
        while cell is not self.maze_state.entry_cell:
            self.cells_img.draw_cell(cell, Theme.path)
            self.cells_img.draw_wall_between_two_cell(cell, self.path[cell], Theme.path)
            cell = self.path[cell]
        self.cells_img.draw_cell(self.maze_state.entry_cell, Theme.entry_cell)
        self.cells_img.draw_cell(self.maze_state.exit_cell, Theme.exit_cell)
        self.is_path_shown = True
        self.put_cells_img_to_window()
