from maze.cell import Cell
from collections import deque
from solver.solver import Solver
from renderer.colors import Colors
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

    def get_neighboors(self) -> list[Cell]:
        neighboors = []
        x = self.current_cell.x
        y = self.current_cell.y
        # west
        if x > 0:
            neighboor = self.cells_grid[y][x - 1]
            if not self.current_cell.west:
                neighboors.append(neighboor)
        # east
        if x + 1 < self.horizontal_cells:
            neighboor = self.cells_grid[y][x + 1]
            if not self.current_cell.east:
                neighboors.append(neighboor)
        # north
        if y > 0:
            neighboor = self.cells_grid[y - 1][x]
            if not self.current_cell.north:
                neighboors.append(neighboor)
        # south
        if y + 1 < self.vertical_cells:
            neighboor = self.cells_grid[y + 1][x]
            if not self.current_cell.south:
                neighboors.append(neighboor)
        #return neighboors
        # for neighboor in neighboors:
        #     if neighboor not in self.visited and neighboor not in self.bfs_queue:
        #         self.bfs_queue.append(neighboor)
        #         self.visited.append(neighboor)
        #         self.path[neighboor] = self.current_cell
        return neighboors

    def find_path(self):
        self.current_cell = self.entry_cell
        self.bfs_queue.appendleft(self.entry_cell)
        while len(self.bfs_queue):
            self.current_cell = self.bfs_queue.popleft()
            if self.current_cell is self.exit_cell:
                print("solution", self.current_cell.x, self.current_cell.y)
                break
            self.get_neighboors()
        self.print_solution()


    def generate(self):
        self.current_cell = self.entry_cell
        self.bfs_queue.appendleft(self.entry_cell)
        self.next_cell = self.exit_cell
        MyMlx.loop_hook(self.generate_solution_path_with_animation, None)


    def generate_solution_path_with_animation(self, _):
        self.frames += 1
        if self.frames % 1 != 0:
            return
        if self.is_finished:
            return
        if self.is_running:
            self.is_running = True
        if len(self.bfs_queue) and not self.is_solution_found:
            self.current_cell = self.bfs_queue.popleft()
            if self.current_cell is self.exit_cell:
                self.is_solution_found = True
                self.redraw_maze()
            else:
                neighboors = self.get_neighboors()
                self.draw_neighboors(neighboors)

        elif self.is_solution_found and self.next_cell is not self.entry_cell:
            print("hello wolrd")
            self.cells_img.clear_cell(self.next_cell, Colors.BLUE)
            self.cells_img.draw_cell(self.next_cell)
            self.next_cell = self.path[self.next_cell]
            self.put_cells_img_to_window()

        elif self.is_solution_found and self.next_cell is self.entry_cell:
            self.cells_img.draw_cell(self.entry_cell, Colors.WHITE)
            self.cells_img.draw_cell(self.exit_cell, Colors.ORANGE)
            self.is_finished = True
            self.put_cells_img_to_window()


    def draw_neighboors(self, neighboors: list[Cell]):
        for neighboor in neighboors:
            if neighboor not in self.visited and neighboor not in self.bfs_queue:
                self.bfs_queue.append(neighboor)
                self.visited.append(neighboor)
                self.path[neighboor] = self.current_cell
                self.cells_img.clear_cell(neighboor, Colors.YELLOW)
                self.cells_img.draw_cell(neighboor)
                self.put_cells_img_to_window()

    def redraw_maze(self) -> None:
        for row_cells in self.cells_grid:
            for cell in row_cells:
                if not cell.is_42_cell:
                    self.cells_img.draw_cell(cell, Colors.GRAY)
                    self.cells_img.draw_cell(cell)
        self.put_cells_img_to_window()

    def print_solution(self):
        self.next_cell = self.exit_cell
        while self.next_cell is not self.entry_cell:
            self.cells_img.clear_cell(self.next_cell, Colors.BLUE)
            self.cells_img.draw_cell(self.next_cell)
            print(self.next_cell.x, self.next_cell.y)
            self.next_cell = self.path[self.next_cell]
        self.cells_img.clear_cell(self.entry_cell, Colors.WHITE)
        self.cells_img.draw_cell(self.entry_cell)
        self.cells_img.clear_cell(self.exit_cell, Colors.ORANGE)
        self.cells_img.draw_cell(self.exit_cell)
        self.put_cells_img_to_window()
