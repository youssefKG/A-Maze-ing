_This project has been created as part of the 42 curriculum by <login1>, <login2>._

# A-Maze-ing: This is the way

## Description

A-Maze-ing is a 2D maze generator and solver with real-time visualization using a custom MLX wrapper. The goal is to generate a maze, visualize its construction, and solve it using BFS while displaying the shortest path.

## Features

- Animated maze generation (DFS and Wilson)
- BFS solver with path visualization
- Interactive keyboard controls
- Deterministic runs using `SEED`
- Optional output file export of maze + solution path

## Instructions

### Requirements

- Python 3.8+
- MLX shared library at mlx/libmlx.so (provided in this repo or built for your system)
- SDL2/X11 dependencies required by MLX on Linux

### Build and Run

Build the Python wheel and run:

- make dependecies
- make run

Or run directly:

- python3 a_maze_ing.py config.txt

## Configuration

The application reads a single config file passed as the only argument.

### Complete config format (case-sensitive)

```
WIDTH=20
HEIGHT=20
ENTRY=0,0
EXIT=19,19
SEED=22
OUTPUT_FILE=maze.txt
PERFECT=False
```

#### Field meanings

- `WIDTH`: maze width, integer > 0
- `HEIGHT`: maze height, integer > 0
- `ENTRY`: start cell, format `x,y`
- `EXIT`: end cell, format `x,y`
- `SEED`: integer seed for deterministic generation
- `OUTPUT_FILE`: output path for the generated maze file
- `PERFECT`: `True` or `False`

Notes:

- If `WIDTH > 8` and `HEIGHT > 6`, a “42” logo is reserved in the center. `ENTRY` and `EXIT` cannot be inside that area.
- Invalid keys or malformed values will stop the program with an error.

## Usage

### Controls

- Enter: start generation
- Q: generate with DFS
- B: generate with Wilson
- S: solve with BFS (after generation is finished)
- H: toggle solution path (after BFS finishes)
- C: change theme
- Esc: exit

### Output File

When generation runs, the maze is written to `OUTPUT_FILE` in this format:

1. Maze grid (each row on its own line)
2. Blank line
3. Entry coordinate line: `(x,y)`
4. Exit coordinate line: `(x,y)`
5. Shortest path string from BFS

## Maze Generation Algorithm

### Chosen algorithms

- DFS (recursive backtracking)
- Wilson (loop-erased random walk)

### Why these algorithms

- DFS is simple, fast, and creates long corridors, making it ideal for a clear visual demo.
- Wilson produces unbiased mazes with uniform spanning trees, showcasing a contrasting style.

## Advanced Features

Multiple generation algorithms and theme switching are supported and can be triggered via keyboard controls.

## Reusable Code

- [mlx/mlx.py](mlx/mlx.py): Python ctypes wrapper around the MLX C library.
- [my_mlx/my_mlx.py](my_mlx/my_mlx.py): simplified MLX API wrapper (window, images, hooks).
- [renderer/images/image.py](renderer/images/image.py) and [renderer/images/cellImg.py](renderer/images/cellImg.py): generic image buffer + grid cell renderer.
- [renderer/colors.py](renderer/colors.py) and [renderer/themes.py](renderer/themes.py): color utilities and theme switching.
- [parser/Parser.py](parser/Parser.py): key/value config parser with validation.
- [maze/cell.py](maze/cell.py) and [maze/maze_state.py](maze/maze_state.py): grid cell model and singleton state container.
- [generators/maze_generator_algo.py](generators/maze_generator_algo.py): generator base class, with implementations in [generators/dfs_maze_generator.py](generators/dfs_maze_generator.py) and [generators/wilson_maze_generator.py](generators/wilson_maze_generator.py).
- [solver/solver.py](solver/solver.py) and [solver/bfs_solver.py](solver/bfs_solver.py): solver base class and BFS implementation.
- [mazegen/MazeGenerator.py](mazegen/MazeGenerator.py) and [mazegen/algorithms](mazegen/algorithms): CLI-oriented algorithm implementations and output writer.

## Team and Project Management

The project was divided between two responsibilities:

- Output/file side: creation of the output file, implementation of DFS/BFS/Wilson algorithms, and parsing.
- Rendering side: drawing with MLX, generation with animation, and reimplementation of the algorithms for visualization.

### Roles

- <login1>: algorithm design, maze generation, BFS solver
- <login2>: rendering, MLX wrapper, themes, UI controls

### Planning and evolution

- Initial plan: single DFS generator + basic renderer.
- Evolution: added Wilson algorithm, BFS solver animation, and theme switching.

### What worked well

- Clear separation between generation, rendering, and solving.
- Factory pattern for algorithm selection.

### What could be improved

- More solvers (A\*, Dijkstra)
- Additional UI controls (pause/step)
- Performance tuning for large mazes

### Strong points

- Clean separation between parsing, generation, rendering, and solving.
- Smooth real-time visualization with animation.
- Deterministic runs via `SEED` for reproducible demos.

### What we learned

- Implementing and comparing maze algorithms (DFS, Wilson, BFS).
- Designing a small architecture with clear module boundaries.
- Building a rendering loop with MLX and handling UI input.

### Tools used

- Python 3
- MLX
- Makefile
- Git

## Folder Structure

```
A-Maze-ing/
├── a_maze_ing.py                  # Main entry point (loads config, runs app)
├── config.txt                     # Sample configuration file
├── Makefile                       # Build and run helpers
├── assets/                        # Static assets (images/backgrounds)
│   └── (images and backgrounds)
├── controll_pannel/               # UI controls and input handling
│   └── controll_pannel.py         # Control panel logic
├── generators/                    # Maze generation implementations (output side)
│   ├── algo_factory.py            # Factory to select generation algorithm
│   ├── dfs_maze_generator.py      # DFS generator implementation
│   ├── maze_generator_algo.py     # Base generator interface
│   └── wilson_maze_generator.py   # Wilson generator implementation
├── maze/                          # Core maze model/state
│   ├── cell.py                    # Cell representation and helpers
│   └── maze_state.py              # Singleton maze state container
├── mazegen/                       # Alternative/CLI-oriented generator package
│   ├── MazeGenerator.py           # Maze generator orchestrator
│   └── algorithms/                # Algorithm implementations for mazegen
│       ├── Algo.py                # Base algorithm class
│       ├── BFSAlgo.py             # BFS solver algorithm
│       ├── DFSAlgo.py             # DFS generator algorithm
│       └── WilsonAlgo.py          # Wilson generator algorithm
├── mlx/                           # MLX Python bindings
│   └── mlx.py                     # MLX wrapper entry
├── my_mlx/                        # Project-specific MLX helpers
│   └── my_mlx.py                  # Higher-level MLX utilities
├── parser/                        # Config parsing and validation
│   └── Parser.py                  # Key/value config parser
├── renderer/                      # Rendering and theme system
│   ├── colors.py                  # Color constants
│   ├── renderer.py                # Renderer and draw pipeline
│   ├── themes.py                  # Theme definitions
│   └── images/                    # Image helpers and assets
│       ├── image.py               # Base image wrapper
│       ├── cellImg.py             # Cell image composition
│       └── background/            # Background images
│           └── background_img.py  # Background image loader
└── solver/                        # Solvers
    ├── solver.py                  # Solver base interface
    └── bfs_solver.py              # BFS solver implementation
```

## Resources

- MLX documentation
- SDL2 documentation
- DFS maze generation references
- Wilson’s algorithm references
- BFS shortest path references

## AI Usage

No AI was used in this project.
