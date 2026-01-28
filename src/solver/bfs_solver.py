from maze.cell import Cell
from my_mlx.my_mlx import MyMlx
from collections import deque
from solver.solver import Solver
from my_mlx.my_mlx import MyMlx
from renderer.colors import Colors
from collections import deque

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

    def get_neighboors(self):
        neighboors = []
        x = self.current_cell.x
        y = self.current_cell.y
        # west
        if x > 0:
            neighboor = self.cells_grid[x - 1][y]
            if not self.current_cell.west:
                neighboors.append(neighboor)
        # east
        if x + 1 < self.horizontal_cells:
            neighboor = self.cells_grid[x + 1][y]
            if not self.current_cell.east:
                neighboors.append(neighboor)
        # north
        if y > 0:
            neighboor = self.cells_grid[x][y - 1]
            if not self.current_cell.north:
                neighboors.append(neighboor)
        # south
        if y + 1 < self.vertical_cells:
            neighboor = self.cells_grid[x][y + 1]
            if not self.current_cell.south:
                neighboors.append(neighboor)

        for neighboor in neighboors:
            if neighboor not in self.visited and neighboor not in self.bfs_queue:
                self.visited.append(neighboor)
                self.bfs_queue.append(neighboor)
                self.path[neighboor] = self.current_cell

    def find_path(self):
        self.current_cell = self.entry_cell
        self.bfs_queue.appendleft(self.entry_cell)
        while True:
            if not len(self.bfs_queue):
                print("solution not found")
                break
            self.current_cell = self.bfs_queue.popleft()
            self.visited.append(self.current_cell)
            if self.current_cell is self.exit_cell:
                print("solution", self.current_cell.x, self.current_cell.y)
                break
            self.get_neighboors()
            self.print_solution()

    def print_solution(self):
        next_cell = self.exit_cell
        while next_cell is not self.entry_cell:
            self.cells_img.clear_cell(next_cell, Colors.YELLOW)
            print(next_cell.x, next_cell.y)
            self.cells_img.draw_cell(next_cell)
            next_cell = self.path[next_cell]
        print(next_cell.x, next_cell.y)
        self.put_cells_img_to_window()
