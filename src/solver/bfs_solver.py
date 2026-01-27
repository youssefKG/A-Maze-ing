from maze.cell import Cell
from my_mlx.my_mlx import MyMlx
from collections import deque
from solver.solver import Solver

class BfsSolver(Solver):

    def get_neighboors(self):
        self.neighboors = []
        x = self.current_cell.x
        y = self.current_cell.y
        # west
        if x > 0:
            if not self.current_cell.west:
                neighboor = self.cells_grid[x - 1][y]
                self.visited.add(neighboor)
        # east
        if x + 1 < self.horizontal_cell:
            if not self.current_cell.east:
                neighboor = self.cells_grid[x + 1][y]
                self.visited.add(neighboor)
        # north
        if y > 0:
            if not self.current_cell.north:
                neighboor = self.cells_grid[x][y - 1]
                self.neighboors.append(neighboor)
        # south
        if y + 1 < self.vertical_cell:
            if not self.current_cell.south:
                neighboor = self.cells_grid[x][y + 1]
                self.neighboors.append(neighboor)

        for neighboor in neighboors:
            if neighboor not in self.visisted:
                self.visited.append(neighboor)
                self.bfs_queue.append(neighboor)
                self.path_bfs[neighboor] = self.current_cell

    def find_path(self):
        self.bfs_queue = [self.entry_cell]
        self.visited = [self.entry_cell]
        self.path_bfs = []
        while not len(self.bfs_queue):
            self.current_cell = self.bfs_queue.pop(0)
            if self.current_cell == self.exit_cell:
                break
            get_neighboors()


    def print_solution:
