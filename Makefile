VENV = venv
PYTHON = $(VENV)/bin/python3
SYS_PYTHON = python3
PIP = $(VENV)/bin/pip
FILES = parser/Parser.py \
		mazegen/algorithms/Algo.py \
		mazegen/algorithms/BFSAlgo.py \
		mazegen/algorithms/DFSAlgo.py \
		mazegen/algorithms/WilsonAlgo.py \

run: dependecies
	$(PYTHON) a_maze_ing.py config.txt

dependecies: $(VENV)/bin/activate 
	$(PIP) install build 
	$(PIP) install flake8
	$(PYTHON) -m build
	cp dist/*.whl .
	$(PIP) install ./mazegen-*.whl

$(VENV)/bin/activate:
	$(SYS_PYTHON) -m $(VENV) $(VENV)

clean:
	rm -rf  __pycache__ */__pycache__ */*/__pycache__
	rm -rf $(VENV) dist/ *.whl *egg-info 

lint:
	flake8 $(FILES) 
	#&& mypy $(FILES) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs	

.PHONY: dependecies clean lint 
