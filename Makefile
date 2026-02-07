VENV = venv
PYTHON = $(VENV)/bin/python3
SYS_PYTHON = python3
PIP = $(VENV)/bin/pip
FILES = parser/Parser.py \
		mazegen/algorithms/Algo.py \
		mazegen/algorithms/BFSAlgo.py \
		mazegen/algorithms/DFSAlgo.py \
		mazegen/algorithms/WilsonAlgo.py \

install: $(VENV)
	$(PIP) install ./mazegen-*.whl

run: 
	$(PYTHON) a_maze_ing.py config.txt
	
dependecies: $(VENV)
	$(PIP) install ./mazegen-*.whl

$(VENV):
	$(SYS_PYTHON) -m $(VENV) $(VENV)

clean:
	rm -rf  __pycache__ */__pycache__ */*/__pycache__
	rm -rf $(VENV) dist/ *egg-info

lint:
	flake8 $(FILES) 
	#&& mypy $(FILES) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs	

.PHONY: dependecies clean lint install
