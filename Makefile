VENV = venv
PYTHON = $(VENV)/bin/python
SYS_PYTHON = python3
PIP = $(VENV)/bin/pip
FILES = parser/Parser.py \
		mazegen/MazeGenerator.py \
		controll_pannel/controll_pannel.py \
		generators/algo_factory.py \
		generators/dfs_maze_generator.py \
		generators/maze_generator_algo.py \
		generators/wilson_maze_generator.py \
		maze/cell.py \
		maze/maze_state.py \
		renderer/colors.py \
		renderer/renderer.py \
		renderer/themes.py \
		solver/bfs_solver.py \
		solver/solver.py \
		a_maze_ing.py \
		my_mlx

install: $(VENV)
	$(PIP) install flake8
	$(PIP) install mypy
	$(PIP) install ./mazegen-*.whl

run: 
	$(PYTHON) a_maze_ing.py config.txt
	
$(VENV):
	$(SYS_PYTHON) -m $(VENV) $(VENV)

clean:
	rm -rf  __pycache__ */__pycache__ */*/__pycache__
	rm -rf $(VENV) dist/ *egg-info build *dist-info

lint:
	$(VENV)/bin/flake8 $(FILES) 
	$(VENV)/bin/mypy $(FILES) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs	


pdb:
	$(PYTHON) -m pdb a_maze_ing.py config.txt

.PHONY: dependecies clean lint install
